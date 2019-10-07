# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Browser(object):
    def setupUi(self, Browser):
        Browser.setObjectName("Browser")
        Browser.resize(591, 565)
        self.verticalLayout = QtGui.QVBoxLayout(Browser)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.browser_header = QtGui.QFrame(Browser)
        self.browser_header.setMinimumSize(QtCore.QSize(0, 44))
        self.browser_header.setMaximumSize(QtCore.QSize(16777215, 44))
        self.browser_header.setStyleSheet("")
        self.browser_header.setFrameShape(QtGui.QFrame.StyledPanel)
        self.browser_header.setFrameShadow(QtGui.QFrame.Raised)
        self.browser_header.setObjectName("browser_header")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.browser_header)
        self.horizontalLayout_4.setContentsMargins(12, 3, 12, 3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtGui.QLabel(self.browser_header)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.search = QtGui.QLineEdit(self.browser_header)
        self.search.setMinimumSize(QtCore.QSize(150, 0))
        self.search.setMaximumSize(QtCore.QSize(150, 16777215))
        self.search.setStyleSheet("border-width: 1px; \n"
"background-image: url(:/res/search.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center left;\n"
"border-style: inset; \n"
"border-color: #535353; \n"
"border-radius: 9px; \n"
"padding-left: 15px")
        self.search.setObjectName("search")
        self.horizontalLayout_4.addWidget(self.search)
        self.verticalLayout.addWidget(self.browser_header)
        self.main_pages = QtGui.QStackedWidget(Browser)
        self.main_pages.setObjectName("main_pages")
        self.items_page = QtGui.QWidget()
        self.items_page.setObjectName("items_page")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.items_page)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scroll_area = QtGui.QScrollArea(self.items_page)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 589, 519))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.load_all_top = QtGui.QToolButton(self.scrollAreaWidgetContents)
        self.load_all_top.setObjectName("load_all_top")
        self.horizontalLayout_7.addWidget(self.load_all_top)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.scroll_area_layout = QtGui.QVBoxLayout()
        self.scroll_area_layout.setSpacing(0)
        self.scroll_area_layout.setObjectName("scroll_area_layout")
        self.verticalLayout_4.addLayout(self.scroll_area_layout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.load_all_bottom = QtGui.QToolButton(self.scrollAreaWidgetContents)
        self.load_all_bottom.setObjectName("load_all_bottom")
        self.horizontalLayout_8.addWidget(self.load_all_bottom)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scroll_area)
        self.main_pages.addWidget(self.items_page)
        self.loading_page = QtGui.QWidget()
        self.loading_page.setStyleSheet("")
        self.loading_page.setObjectName("loading_page")
        self.horizontalLayout = QtGui.QHBoxLayout(self.loading_page)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progress_bar = QtGui.QLabel(self.loading_page)
        self.progress_bar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progress_bar.setStyleSheet("#progress_bar {\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.progress_bar.setText("")
        self.progress_bar.setPixmap(QtGui.QPixmap(":/res/progress_bar_1.png"))
        self.progress_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_bar.setObjectName("progress_bar")
        self.horizontalLayout.addWidget(self.progress_bar)
        self.main_pages.addWidget(self.loading_page)
        self.status_page = QtGui.QWidget()
        self.status_page.setObjectName("status_page")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.status_page)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.status_message = QtGui.QLabel(self.status_page)
        self.status_message.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status_message.setStyleSheet("#status_message {\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.status_message.setAlignment(QtCore.Qt.AlignCenter)
        self.status_message.setWordWrap(True)
        self.status_message.setObjectName("status_message")
        self.horizontalLayout_2.addWidget(self.status_message)
        self.main_pages.addWidget(self.status_page)
        self.verticalLayout.addWidget(self.main_pages)

        self.retranslateUi(Browser)
        self.main_pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Browser)

    def retranslateUi(self, Browser):
        Browser.setWindowTitle(QtGui.QApplication.translate("Browser", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Browser", "<big>Browser Title</big>", None, QtGui.QApplication.UnicodeUTF8))
        self.load_all_top.setText(QtGui.QApplication.translate("Browser", "Showing 50 out of 250 matches. Click to load all...", None, QtGui.QApplication.UnicodeUTF8))
        self.load_all_bottom.setText(QtGui.QApplication.translate("Browser", "Showing 50 out of 250 matches. Click to load all...", None, QtGui.QApplication.UnicodeUTF8))
        self.status_message.setText(QtGui.QApplication.translate("Browser", "Sorry, no items found!", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
from . import resources_rc
