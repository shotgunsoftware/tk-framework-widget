"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------
"""

import os
import sys
import tempfile
import subprocess

from tank.platform.qt import QtCore, QtGui
from .ui.thumbnail_widget import Ui_ThumbnailWidget
    
class ThumbnailWidget(QtGui.QWidget):
    """
    """
    
    thumbnail_changed = QtCore.Signal()
    
    def __init__(self, parent=None):
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
        return self._ui.thumbnail.pixmap()
    @thumbnail.setter
    def thumbnail(self, value):
        if not value:
            value = QtGui.QPixmap()
        self._ui.thumbnail.setPixmap(value)
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
        self._ui.buttons_frame.setStyleSheet("#buttons_frame {background-color: rgba(32, 32, 32, %d)}" % (64 * value))
    btn_visibility = QtCore.Property(float, get_btn_visibility, set_btn_visibility)
        
    def _run_btns_transition_anim(self, direction):
        """
        Run the transition animation for the buttons
        """
        if not self._btns_transition_anim:
            # set up anim:
            self._btns_transition_anim =  QtCore.QPropertyAnimation(self, "btn_visibility")                
            self._btns_transition_anim.setDuration(100)
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
                
            h_scale = float(thumbnail_geom.height())/float(pm_sz.height())
            w_scale = float(thumbnail_geom.width())/float(pm_sz.width())
            scale = min(1.0, h_scale, w_scale)
            scale_contents = (scale < 1.0)
            
            new_height = min(int(pm_sz.height() * scale), thumbnail_geom.height())
            new_width = min(int(pm_sz.width() * scale), thumbnail_geom.width())
            
            new_geom = QtCore.QRect(thumbnail_geom)
            new_geom.moveLeft(thumbnail_geom.width()/2 - new_width/2)
            new_geom.moveTop(thumbnail_geom.height()/2 - new_height/2)
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
        
    def _on_screenshot(self):
        path = None

        # hide the containing window
        # (AD) - we can't hide the window as this will break modality!  Instead
        # we have to move the window off the screen:
        win_geom = self.window().geometry()
        self.window().setGeometry(1000000, 1000000, win_geom.width(), win_geom.height())
        
        # make sure this event is processed:
        QtCore.QCoreApplication.processEvents()
        
        try:
            # screenshot            
            path = tempfile.NamedTemporaryFile(suffix=".png", prefix="tanktmp", delete=False).name
            
            if sys.platform == "darwin":
                # use built-in screenshot command on the mac
                os.system("screencapture -m -i -s %s" % path)
            elif sys.platform == "linux2":
                # use image magick
                os.system("import %s" % path)
            elif sys.platform == "win32":
                # use external boxcutter tool
                bc = os.path.abspath(os.path.join(__file__, "../resources/boxcutter.exe"))
                subprocess.check_call([bc, path])
        finally:
            # restore the window:
            #self.window().show()
            self.window().setGeometry(win_geom)
            QtCore.QCoreApplication.processEvents()

        pm = QtGui.QPixmap(path)
        return pm