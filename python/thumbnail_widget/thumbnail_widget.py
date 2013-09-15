# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import os
import sys
import tempfile
import subprocess

import tank
from tank.platform.qt import QtCore, QtGui
from .ui.thumbnail_widget import Ui_ThumbnailWidget
    
class ThumbnailWidget(QtGui.QWidget):
    """
    Thumbnail widget that provides screen capture functionality
    """
    
    thumbnail_changed = QtCore.Signal()
    
    def __init__(self, parent=None):
        """
        Construction
        """
        QtGui.QWidget.__init__(self, parent)
        
        self._ui = Ui_ThumbnailWidget()
        self._ui.setupUi(self)
        
        # create layout to control buttons frame
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self._ui.buttons_frame)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setLayout(layout)
        
        # connect to buttons:
        self._ui.camera_btn.clicked.connect(self._on_camera_clicked)

        self._btns_transition_anim = None
        self._update_ui()

    @property
    def thumbnail(self):
        pm = self._ui.thumbnail.pixmap()
        return pm if pm and not pm.isNull() else None
    
    @thumbnail.setter
    def thumbnail(self, value):
        self._ui.thumbnail.setPixmap(value if value else QtGui.QPixmap())
        self._update_ui()
        self.thumbnail_changed.emit()
        
    def enable_screen_capture(self, enable):
        self._ui.camera_btn.setVisible(enable)
        
    def resizeEvent(self, event):
        self._update_ui()

    def enterEvent(self, event):
        """
        when the cursor enters the control, show the buttons
        """
        if self.thumbnail and self._are_any_btns_enabled():
            self._ui.buttons_frame.show()
            self._run_btns_transition_anim(QtCore.QAbstractAnimation.Forward)
        
    def leaveEvent(self, event):
        """
        when the cursor leaves the control, hide the buttons
        """
        if self.thumbnail and self._are_any_btns_enabled():
            self._run_btns_transition_anim(QtCore.QAbstractAnimation.Backward)
        
    def _are_any_btns_enabled(self):
        """
        Return if any of the buttons are enabled
        """
        return not (self._ui.camera_btn.isHidden())
        
    """
    button visibility property used by QPropertyAnimation
    """        
    def get_btn_visibility(self):
        return self._btns_visibility
    def set_btn_visibility(self, value):
        self._btns_visibility = value
        self._ui.buttons_frame.setStyleSheet("#buttons_frame {border-radius: 2px; background-color: rgba(32, 32, 32, %d);}" % (64 * value))
    btn_visibility = QtCore.Property(float, get_btn_visibility, set_btn_visibility)
        
    def _run_btns_transition_anim(self, direction):
        """
        Run the transition animation for the buttons
        """
        if not self._btns_transition_anim:
            # set up anim:
            self._btns_transition_anim =  QtCore.QPropertyAnimation(self, "btn_visibility")                
            self._btns_transition_anim.setDuration(150)
            self._btns_transition_anim.setStartValue(0.0)
            self._btns_transition_anim.setEndValue(1.0)
            self._btns_transition_anim.finished.connect(self._on_btns_transition_anim_finished)
        
        if self._btns_transition_anim.state() == QtCore.QAbstractAnimation.Running:
            if self._btns_transition_anim.direction() != direction:
                self._btns_transition_anim.pause()
                self._btns_transition_anim.setDirection(direction)
                self._btns_transition_anim.resume()
            else:
                pass # just let animation continue!
        else:
            self._btns_transition_anim.setDirection(direction)
            self._btns_transition_anim.start()
        
    def _on_btns_transition_anim_finished(self):
        if self._btns_transition_anim.direction() == QtCore.QAbstractAnimation.Backward:
             self._ui.buttons_frame.hide()
    
    def _on_camera_clicked(self):
        pm = self._on_screenshot()
        if pm:
            self.thumbnail = pm
 
    def _update_ui(self):
    
        # maximum size of thumbnail is widget geom:
        thumbnail_geom = self.geometry()
        thumbnail_geom.moveTo(0,0)
        scale_contents = False
        
        pm = self.thumbnail
        if pm:
            # work out size thumbnail should be to maximize size
            # whilst retaining aspect ratio
            pm_sz = pm.size()
                
            h_scale = float(thumbnail_geom.height()-4)/float(pm_sz.height())
            w_scale = float(thumbnail_geom.width()-4)/float(pm_sz.width())
            scale = min(1.0, h_scale, w_scale)
            scale_contents = (scale < 1.0)
            
            new_height = min(int(pm_sz.height() * scale), thumbnail_geom.height())
            new_width = min(int(pm_sz.width() * scale), thumbnail_geom.width())
            
            new_geom = QtCore.QRect(thumbnail_geom)
            new_geom.moveLeft(((thumbnail_geom.width()-4)/2 - new_width/2)+2)
            new_geom.moveTop(((thumbnail_geom.height()-4)/2 - new_height/2)+2)
            new_geom.setWidth(new_width)
            new_geom.setHeight(new_height)
            thumbnail_geom = new_geom
            
        self._ui.thumbnail.setScaledContents(scale_contents)
        self._ui.thumbnail.setGeometry(thumbnail_geom)
        
        # now update buttons based on current thumbnail:
        if not self._btns_transition_anim or self._btns_transition_anim.state() == QtCore.QAbstractAnimation.Stopped:
            if self.thumbnail or not self._are_any_btns_enabled():
                self._ui.buttons_frame.hide()
                self._btns_visibility = 0.0
            else:
                self._ui.buttons_frame.show()
                self._btns_visibility = 1.0
        
    def _safe_get_dialog(self):
        """
        Get the widgets dialog parent.  
        
        just call self.window() but this is unstable in Nuke
        Previously this would
        causing a crash on exit - suspect that it's caching
        something internally which then doesn't get cleaned
        up properly...
        """
        current_widget = self
        while current_widget:
            if isinstance(current_widget, QtGui.QDialog):
                return current_widget
            
            current_widget = current_widget.parentWidget()
            
        return None
           
    class ScreenshotThread(QtCore.QThread):
        """
        Wrap screenshot call in a thread just to be on the safe side!  
        This helps avoid the os thinking the application has hung for 
        certain applications (e.g. Softimage on Windows)
        """
        def __init__(self, path):
            QtCore.QThread.__init__(self)
            self._path = path
            self._error = None
            
        def get_error(self):
            return self._error
            
        def run(self):
            try:
                if sys.platform == "darwin":
                    # use built-in screenshot command on the mac
                    os.system("screencapture -m -i -s %s" % self._path)
                elif sys.platform == "linux2":
                    # use image magick
                    os.system("import %s" % self._path)
                elif sys.platform == "win32":
                    # use external boxcutter tool
                    bc = os.path.abspath(os.path.join(__file__, "../resources/boxcutter.exe"))
                    subprocess.check_call([bc, self._path])
            except Exception, e:
                self._error = str(e)
           
    def _on_screenshot(self):
        """
        Perform the actual screenshot
        """
        
        # hide the containing window - we can't actuall hide 
        # the window as this will break modality!  Instead
        # we have to move the window off the screen:
        win = self._safe_get_dialog()
        
        win_geom = None
        if win:
            win_geom = win.geometry()
            win.setGeometry(1000000, 1000000, win_geom.width(), win_geom.height())
        
            # make sure this event is processed:
            QtCore.QCoreApplication.processEvents()

        path = None
        pm = None
        try:
            # get temporary file to use:
            with tempfile.NamedTemporaryFile(suffix=".png", prefix="tanktmp", delete=False) as temp_file:
                path = temp_file.name

            # do screenshot with thread so we don't block anything
            screenshot_thread = ThumbnailWidget.ScreenshotThread(path)
            screenshot_thread.start()
            while not screenshot_thread.isFinished():
                screenshot_thread.wait(100)
                QtGui.QApplication.processEvents()

            er = screenshot_thread.get_error()
            if er:
                raise tank.TankError("Failed to capture screenshot: %s" % er)
            
            # load into pixmap:
            pm = QtGui.QPixmap(path)
        finally:
            # restore the window:
            if win:
                win.setGeometry(win_geom)
                QtCore.QCoreApplication.processEvents()
            
            # remove the temporary file:
            if path:
                os.remove(path)

        return pm