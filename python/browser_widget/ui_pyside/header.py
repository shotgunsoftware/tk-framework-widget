# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'header.ui'
#
# Created: Sun Apr  7 12:08:43 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Header(object):
    def setupUi(self, Header):
        Header.setObjectName("Header")
        Header.resize(389, 37)
        Header.setMinimumSize(QtCore.QSize(0, 0))
        Header.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(Header)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(3, 12, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Header)
        self.label.setStyleSheet("#name_label {\n"
"font-size: 16px\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtGui.QFrame(Header)
        self.line.setStyleSheet("")
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.retranslateUi(Header)
        QtCore.QMetaObject.connectSlotsByName(Header)

    def retranslateUi(self, Header):
        Header.setWindowTitle(QtGui.QApplication.translate("Header", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Header", "<big>Header</big>", None, QtGui.QApplication.UnicodeUTF8))

