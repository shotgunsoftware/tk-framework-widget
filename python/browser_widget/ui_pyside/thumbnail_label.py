"""
Copyright (c) 2012 Shotgun Software, Inc
----------------------------------------------------
"""
import os
import sys

from tank.platform.qt import QtCore, QtGui 

class ThumbnailLabel(QtGui.QLabel):

    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)

    def setPixmap(self, pixmap):
        
        # scale the pixmap down to fit
        if pixmap.height() > 80 or pixmap.width() > 120:
            # scale it down to 120x80
            pixmap = pixmap.scaled( QtCore.QSize(120,80), 
                                    QtCore.Qt.KeepAspectRatio, 
                                    QtCore.Qt.SmoothTransformation)

        
        
        
        QtGui.QLabel.setPixmap(self, pixmap)

