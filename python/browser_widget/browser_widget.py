"""
Copyright (c) 2012 Shotgun Software, Inc
----------------------------------------------------
"""
import os
import sys

from tank.platform.qt import QtCore, QtGui
from .ui_pyside.browser import Ui_Browser
     
from .worker import Worker

class BrowserWidget(QtGui.QWidget):
    
    ######################################################################################
    # SIGNALS
    
    # when the selection changes 
    selection_changed = QtCore.Signal()
    
    # when someone double clicks on an item
    action_requested = QtCore.Signal()
    
    # called when the list contents have been modified:
    list_modified = QtCore.Signal()
    
    
    ######################################################################################
    # Init & Destruct
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        # set up the UI
        self.ui = Ui_Browser() 
        self.ui.setupUi(self)

        # hide the overlays
        self.ui.main_pages.setCurrentWidget(self.ui.items_page)

        self._app = None
        self._worker = None
        self._current_work_id = None
        self._dynamic_widgets = []
        self._multi_select = False
        self._search = True
        
        # spinner
        self._spin_icons = []
        self._spin_icons.append(QtGui.QPixmap(":/res/progress_bar_1.png"))
        self._spin_icons.append(QtGui.QPixmap(":/res/progress_bar_2.png"))
        self._spin_icons.append(QtGui.QPixmap(":/res/progress_bar_3.png"))
        self._spin_icons.append(QtGui.QPixmap(":/res/progress_bar_4.png")) 
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect( self._update_spinner )
        self._current_spinner_index = 0
        
        # search
        self.ui.search.textEdited.connect(self._on_search_text_changed)
        
        # style:
        self._title_base_style = {
            "border":"none",
            "border-colour":"rgb(32,32,32)",
            "border-top-left-radius":"3px",
            "border-top-right-radius":"3px",
            "border-bottom-left-radius":"0px",
            "border-bottom-right-radius":"0px"
        }
        self._title_styles = {
            "gradient":{"background":"qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(97, 97, 97, 255), stop:1 rgba(49, 49, 49, 255));"},
            "none":{}
        }
        self._title_margins = {
            "gradient":[12,3,12,3],
            "none":[3,3,3,3]
        }
        
        self._current_title_style = "none"
        self.title_style = "gradient"
        
    @property
    def title_style(self):
        return self._current_title_style
    @title_style.setter
    def title_style(self, value):
        if value != self._current_title_style and value in self._title_styles.keys():
            # change style sheet:
            self._current_title_style = value
            style = self._title_base_style.copy()
            style.update(self._title_styles[self._current_title_style])
            ss = self._style_as_string("#browser_header", style)
            self.ui.browser_header.setStyleSheet(ss)
            
            # change margins:
            margins = self._title_margins.get(self._current_title_style)
            if margins:
                self.ui.browser_header.layout().setContentsMargins(margins[0], margins[1], margins[2], margins[3])
        
    def enable_multi_select(self, enable):
        """
        Should we enable multi select
        """
        self._multi_select = enable
        
    def enable_search(self, status):
        """
        Toggle the search bar (on by default)
        """
        self.ui.search.setVisible(status)
        
    def destroy(self):
        if self._worker:
            self._worker.stop()
        
    def set_app(self, app):
        """
        associate with an app object
        """
        self._app = app
        # set up worker queue
        self._worker = Worker(app)
        self._worker.work_completed.connect( self._on_worker_signal)
        self._worker.work_failure.connect( self._on_worker_failure)
        
        self._worker.start()
        
    def set_label(self, label):
        """
        Sets the text next to the search button 
        """
        self.ui.label.setText("<big>%s</big>" % label)
    ######################################################################################
    # Public Methods
    
    def load(self, data):
        """
        Loads data into the browser widget. 
        Called by outside code 
        """
        # start spinning
        self.ui.main_pages.setCurrentWidget(self.ui.loading_page)
        self._timer.start(100)
        # queue up work
        self._current_work_id = self._worker.queue_work(self.get_data, data, asap=True)
        
        self.list_modified.emit()
    
    def clear(self):
        """
        Clear widget of its contents.
        """
        # hide overlays
        self.ui.main_pages.setCurrentWidget(self.ui.items_page)
        
        # clear search box
        self.ui.search.setText("")
        
        # also reset any jobs that are processing. No point processing them
        # if their requestors are gone.
        if self._worker:
            self._worker.clear()
            
        for x in self._dynamic_widgets:
            # remove widget from layout:
            self.ui.scroll_area_layout.removeWidget(x)
            # set it's parent to None so that it is removed from the widget hierarchy
            x.setParent(None)
            # mark it to be deleted when event processing returns to the main loop
            x.deleteLater()
        self._dynamic_widgets = []
        
        # lastly, clear selection
        self.clear_selection()
        
        self.list_modified.emit()
        
            
    def set_message(self, message):
        """
        Replace the list of items with a single message
        """
        self.ui.main_pages.setCurrentWidget(self.ui.status_page)
        self.ui.status_message.setText(message)
        
    def clear_selection(self):
        """
        Clears the selection
        """
        for x in self._dynamic_widgets:
            x.set_selected(False)        
                
    def get_selected_item(self):
        """
        Gets the last selected item, None if no selection
        """
        for widget in self._dynamic_widgets:
            if widget.is_selected():
                return widget
        return None
    
    def get_selected_items(self):
        """
        Returns entire selection
        """
        selected_items = []
        for widget in self._dynamic_widgets:
            if widget.is_selected():
                selected_items.append(widget)
        return selected_items
        
    def get_items(self):
        return self._dynamic_widgets
        
    def select(self, item):
        self._on_item_clicked(item)
        # in order for the scroll to happen during load, first give
        # the scroll area  chance to resize it self by processing its event queue.
        QtCore.QCoreApplication.processEvents()
        # and focus on the selection
        self.ui.scroll_area.ensureWidgetVisible(item)
    
    ##########################################################################################
    # Protected stuff - implemented by deriving classes
    
    def get_data(self, data):
        """
        Needs to be implemented by subclasses
        """
        raise Exception("not implemented!")
    
    def process_result(self, result):
        """
        Needs to be implemented by subclasses
        """
        raise Exception("not implemented!")
    
    ##########################################################################################
    # Internals
    
    def _style_as_string(self, name, style_dict):
        style_elements = ["%s: %s;" % (key, value) for key, value in style_dict.iteritems()] 
        return "%s { %s }" % (name, "".join(style_elements)) 
    
    def _on_search_text_changed(self, text):
        """
        Cull based on search box
        """

        if text == "":
            # show all items
            for i in self._dynamic_widgets:
                i.setVisible(True)

        elif len(text) > 2: # cull by string for strings > 2 chars
            
            # if running PyQt, convert QString to str
            if not isinstance(text, basestring):
                # convert QString to str
                text = str(text)
            
            # now we have a str or unicode object which has the lower() method
            lower_text = text.lower()  
            
            for i in self._dynamic_widgets:
                
                details = i.get_details()

                # if running PyQt, convert QString to str
                details_lower = details
                if not isinstance(details_lower, basestring):
                    details_lower = str(details_lower)
                # now we have a str or unicode object which has the lower() method
                details_lower = details_lower.lower()
                
                if details is None: # header
                    i.setVisible(True)
                
                elif lower_text in details_lower: 
                    i.setVisible(True)
                    
                else:
                    i.setVisible(False)
    
    def _on_worker_failure(self, uid, msg):
        """
        The worker couldn't execute stuff
        """
        if self._current_work_id != uid:
            # not our job. ignore
            return

        # finally, turn off progress indication and turn on display
        self.ui.main_pages.setCurrentWidget(self.ui.items_page)
        self._timer.stop()
    
        # show error message
        self.set_message(msg)
        

    def _on_worker_signal(self, uid, data):
        """
        Signalled whenever the worker completes something
        """
        if self._current_work_id != uid:
            # not our job. ignore
            return

        # finally, turn off progress indication and turn on display
        self.ui.main_pages.setCurrentWidget(self.ui.items_page)
        self._timer.stop()
    
        # process!
        self.process_result(data)
        
        # and just in case the list has been modified
        self.list_modified.emit()
            
    
    def _update_spinner(self):
        """
        Animate spinner icon
        """
        self.ui.progress_bar.setPixmap(self._spin_icons[self._current_spinner_index])
        self._current_spinner_index += 1
        if self._current_spinner_index == 4:
            self._current_spinner_index = 0            
        
    def _on_item_clicked(self, item):
        
        if item.supports_selection() == False:
            # not all items are selectable
            return
        
        if self._multi_select:
            # invert selection:
            item.set_selected(not item.is_selected())
        else:
            # single select
            self.clear_selection()
            item.set_selected(True)
            
        self.selection_changed.emit()

    def _on_item_double_clicked(self, item):
        self.action_requested.emit()

    def add_item(self, item_class):
        """
        Adds a list item. Returns the created object.
        """
        widget = item_class(self._app, self._worker, self)
        self.ui.scroll_area_layout.addWidget(widget)
        self._dynamic_widgets.append(widget)   
        widget.clicked.connect( self._on_item_clicked )
        widget.double_clicked.connect( self._on_item_double_clicked )  
        
        self.list_modified.emit()
         
        return widget  




        
        
        



