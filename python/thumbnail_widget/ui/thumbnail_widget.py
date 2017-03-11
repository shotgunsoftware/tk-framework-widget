# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thumbnail_widget.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_ThumbnailWidget(object):
    def setupUi(self, ThumbnailWidget):
        ThumbnailWidget.setObjectName("ThumbnailWidget")
        ThumbnailWidget.resize(347, 266)
        ThumbnailWidget.setStyleSheet("")
        self.thumbnail = QtGui.QLabel(ThumbnailWidget)
        self.thumbnail.setGeometry(QtCore.QRect(210, 190, 81, 61))
        self.thumbnail.setMinimumSize(QtCore.QSize(0, 0))
        self.thumbnail.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.thumbnail.setStyleSheet("")
        self.thumbnail.setText("")
        self.thumbnail.setScaledContents(False)
        self.thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.thumbnail.setObjectName("thumbnail")
        self.buttons_frame = QtGui.QFrame(ThumbnailWidget)
        self.buttons_frame.setGeometry(QtCore.QRect(40, 30, 211, 191))
        self.buttons_frame.setStyleSheet("#buttons_frame {\n"
"border-radius: 2px;\n"
"background-color: rgba(0,0,0, 64);\n"
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
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_btn.sizePolicy().hasHeightForWidth())
        self.camera_btn.setSizePolicy(sizePolicy)
        self.camera_btn.setMinimumSize(QtCore.QSize(64, 64))
        self.camera_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.camera_btn.setCursor(QtCore.Qt.PointingHandCursor)
        self.camera_btn.setStyleSheet("#camera_btn {\n"
"    background-color: rgba( 0, 0, 0, 0 );\n"
"    image: url(:/res/camera.png);\n"
"    margin: 5px;\n"
"    border: none;\n"
"}\n"
"#camera_btn:hover {\n"
"    image: url(:/res/camera_hl.png);\n"
"}\n"
"#camera_btn:focus:pressed {\n"
"    image: url(:/res/camera_hl.png);\n"
"}\n"
"\n"
"")
        self.camera_btn.setText("")
        self.camera_btn.setIconSize(QtCore.QSize(64, 64))
        self.camera_btn.setFlat(True)
        self.camera_btn.setObjectName("camera_btn")
        self.horizontalLayout_2.addWidget(self.camera_btn)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 51, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)

        self.retranslateUi(ThumbnailWidget)
        QtCore.QMetaObject.connectSlotsByName(ThumbnailWidget)

    def retranslateUi(self, ThumbnailWidget):
        ThumbnailWidget.setWindowTitle(QtGui.QApplication.translate("ThumbnailWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
