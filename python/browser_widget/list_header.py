"""
Copyright (c) 2012 Shotgun Software, Inc
----------------------------------------------------
"""
import os
import sys

from tank.platform.qt import QtCore, QtGui
from .ui_pyside.header import Ui_Header

from .list_base import ListBase

class ListHeader(ListBase):
    
    def __init__(self, app, worker, parent=None):
        ListBase.__init__(self, app, worker, parent)

        # set up the UI
        self.ui = Ui_Header() 
        self.ui.setupUi(self)

        # initialize line to be plain and the same colour as the text:        
        self.ui.line.setFrameShadow(QtGui.QFrame.Plain)
        clr = QtGui.QApplication.palette().text().color()
        self.ui.line.setStyleSheet("#line{color: rgb(%d,%d,%d);}" % (clr.red(), clr.green(), clr.blue()))

    def set_title(self, title):
        self.ui.label.setText("<big>%s</big>" % title)
        
    def get_title(self):
        return self.ui.label.text()