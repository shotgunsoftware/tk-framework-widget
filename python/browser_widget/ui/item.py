# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'item.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Item(object):
    def setupUi(self, Item):
        Item.setObjectName("Item")
        Item.resize(332, 71)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Item)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.background = QtGui.QFrame(Item)
        self.background.setStyleSheet("#background {\n"
"border-radius: 3px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.background.setFrameShape(QtGui.QFrame.StyledPanel)
        self.background.setFrameShadow(QtGui.QFrame.Raised)
        self.background.setObjectName("background")
        self.horizontalLayout = QtGui.QHBoxLayout(self.background)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.thumbnail = ThumbnailLabel(self.background)
        self.thumbnail.setMinimumSize(QtCore.QSize(80, 55))
        self.thumbnail.setMaximumSize(QtCore.QSize(80, 55))
        self.thumbnail.setStyleSheet("")
        self.thumbnail.setText("")
        self.thumbnail.setPixmap(QtGui.QPixmap(":/res/thumb_empty.png"))
        self.thumbnail.setScaledContents(False)
        self.thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.thumbnail.setObjectName("thumbnail")
        self.horizontalLayout.addWidget(self.thumbnail)
        self.details = QtGui.QLabel(self.background)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.details.sizePolicy().hasHeightForWidth())
        self.details.setSizePolicy(sizePolicy)
        self.details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.details.setWordWrap(True)
        self.details.setObjectName("details")
        self.horizontalLayout.addWidget(self.details)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout_2.addWidget(self.background)

        self.retranslateUi(Item)
        QtCore.QMetaObject.connectSlotsByName(Item)

    def retranslateUi(self, Item):
        Item.setWindowTitle(QtGui.QApplication.translate("Item", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.details.setText(QtGui.QApplication.translate("Item", "content", None, QtGui.QApplication.UnicodeUTF8))

from .thumbnail_label import ThumbnailLabel
from . import resources_rc
