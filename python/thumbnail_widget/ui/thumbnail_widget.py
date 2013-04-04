# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thumbnail_widget.ui'
#
# Created: Thu Apr  4 12:31:20 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ThumbnailWidget(object):
    def setupUi(self, ThumbnailWidget):
        ThumbnailWidget.setObjectName("ThumbnailWidget")
        ThumbnailWidget.resize(390, 303)
        self.thumbnail = QtGui.QLabel(ThumbnailWidget)
        self.thumbnail.setGeometry(QtCore.QRect(310, 230, 81, 61))
        self.thumbnail.setMinimumSize(QtCore.QSize(0, 0))
        self.thumbnail.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.thumbnail.setStyleSheet("")
        self.thumbnail.setText("")
        self.thumbnail.setScaledContents(False)
        self.thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.thumbnail.setObjectName("thumbnail")
        self.buttons_frame = QtGui.QFrame(ThumbnailWidget)
        self.buttons_frame.setGeometry(QtCore.QRect(30, 40, 281, 181))
        self.buttons_frame.setStyleSheet("#buttons_frame {\n"
"background-color: rgba(0,0,0, 64)\n"
"}")
        self.buttons_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.buttons_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.buttons_frame.setLineWidth(0)
        self.buttons_frame.setObjectName("buttons_frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.buttons_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtGui.QSpacerItem(20, 52, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.camera_btn = QtGui.QPushButton(self.buttons_frame)
        self.camera_btn.setMinimumSize(QtCore.QSize(64, 64))
        self.camera_btn.setMaximumSize(QtCore.QSize(64, 64))
        self.camera_btn.setCursor(QtCore.Qt.PointingHandCursor)
        self.camera_btn.setStyleSheet("#camera_btn {\n"
"    background-color: rgba( 0, 0, 0, 0 );\n"
"    border-image: url(:/res/camera.png);\n"
"    border: none;\n"
"}\n"
"#camera_btn:hover {\n"
"    background-color: rgba( 0, 0, 0, 0 );\n"
"    border-image: url(:/res/camera_hl.png);\n"
"    border: none;\n"
"}\n"
"#camera_btn:focus:pressed {\n"
"    background-color: rgba( 0, 0, 0, 0 );\n"
"    border-image: url(:/res/camera_hl.png);\n"
"    border: none;\n"
"}\n"
"\n"
"")
        self.camera_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.camera_btn.setIcon(icon)
        self.camera_btn.setIconSize(QtCore.QSize(64, 64))
        self.camera_btn.setFlat(True)
        self.camera_btn.setObjectName("camera_btn")
        self.horizontalLayout_2.addWidget(self.camera_btn)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label = QtGui.QLabel(self.buttons_frame)
        self.label.setStyleSheet("#label {\n"
"color: rgb(225, 225, 225);\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem3 = QtGui.QSpacerItem(20, 51, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)

        self.retranslateUi(ThumbnailWidget)
        QtCore.QMetaObject.connectSlotsByName(ThumbnailWidget)

    def retranslateUi(self, ThumbnailWidget):
        ThumbnailWidget.setWindowTitle(QtGui.QApplication.translate("ThumbnailWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ThumbnailWidget", "Take a Screenshot", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
