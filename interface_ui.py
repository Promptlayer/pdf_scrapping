# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)


class Ui_LLMandSCRAP(object):
    def setupUi(self, LLMandSCRAP):
        if not LLMandSCRAP.objectName():
            LLMandSCRAP.setObjectName(u"LLMandSCRAP")
        LLMandSCRAP.resize(1277, 679)
        LLMandSCRAP.setStyleSheet(u"QStackedWidget{\n"
"background-color: white;\n"
"}")
        self.centralwidget = QWidget(LLMandSCRAP)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self._header_frame = QFrame(self.centralwidget)
        self._header_frame.setObjectName(u"_header_frame")
        self._header_frame.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._header_frame.sizePolicy().hasHeightForWidth())
        self._header_frame.setSizePolicy(sizePolicy)
        self._header_frame.setMinimumSize(QSize(0, 0))
        self._header_frame.setMaximumSize(QSize(16777215, 65))
        self._header_frame.setStyleSheet(u"QFrame#_header_frame\n"
"{\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 0px;\n"
"	background-color: qlineargradient(spread:repeat, cx1:1, cy1:1, x2:1, y2:1, stop:0 #9BA6AF,stop:1 #697782);\n"
"\n"
"/*\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                 stop:0 white, stop: 0.4 gray, stop:1 green)\n"
"\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                 stop:0 white, stop: 0.4 rgba(10, 20, 30, 40),\n"
"                 stop:1 rgb(0, 200, 230, 200))\n"
"\n"
"     background: qconicalgradient(cx:0.5, cy:0.5, angle:30,\n"
"                 stop:0 white, stop:1 #00FF00)\n"
"\n"
"     background: qradialgradient(cx:0, cy:0, radius: 1,\n"
"                 fx:0.5, fy:0.5, stop:0 white, stop:1 green)\n"
"}")
        self._header_frame.setFrameShape(QFrame.StyledPanel)
        self._header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self._header_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 5)
        self.header_left_layout = QVBoxLayout()
        self.header_left_layout.setSpacing(0)
        self.header_left_layout.setObjectName(u"header_left_layout")
        self.header_left_layout.setContentsMargins(-1, 10, -1, -1)
        self._subtitle_label = QLabel(self._header_frame)
        self._subtitle_label.setObjectName(u"_subtitle_label")
        self._subtitle_label.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Segoe Print"])
        font.setBold(True)
        self._subtitle_label.setFont(font)
        self._subtitle_label.setStyleSheet(u"")
        self._subtitle_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self._subtitle_label.setMargin(0)

        self.header_left_layout.addWidget(self._subtitle_label)


        self.horizontalLayout_3.addLayout(self.header_left_layout)

        self.header_right_layout = QVBoxLayout()
        self.header_right_layout.setObjectName(u"header_right_layout")
        self.navigationheader_frame = QFrame(self._header_frame)
        self.navigationheader_frame.setObjectName(u"navigationheader_frame")
        self.navigationheader_frame.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1: 0, y1: 0, x2: 1, y2: 1, stop:0 #f7f7f7, stop:1 #f6f6f6);\n"
"	font-size: 16px;\n"
"	color: #646363;\n"
"	text-transform: uppercase;\n"
"	font-weight: bold;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: qlineargradient(spread:pad, x1: 0, y1: 0, x2: 0, y2: 1, stop:0 #ebebeb, stop:1 #e5e5e5);\n"
"	border-color: #ecf3f7;\n"
"}\n"
"\n"
"QPushButton::selected {\n"
"	background-color: #2b6c7e;\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"	background-color: #BDBDBD;\n"
"	color: #757575;\n"
"	border-color: #9E9E9E;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background-color: qlineargradient(spread:pad, x1: 0, y1: 0, x2: 1, y2: 1, stop:0 #2b9c8b, stop:1 #3ad3bc);\n"
"}")
        self.navigationheader_frame.setFrameShape(QFrame.NoFrame)
        self.navigationheader_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.navigationheader_frame)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.nav_button_1 = QPushButton(self.navigationheader_frame)
        self.nav_button_1.setObjectName(u"nav_button_1")
        self.nav_button_1.setEnabled(True)
        sizePolicy.setHeightForWidth(self.nav_button_1.sizePolicy().hasHeightForWidth())
        self.nav_button_1.setSizePolicy(sizePolicy)
        self.nav_button_1.setMinimumSize(QSize(0, 0))
        self.nav_button_1.setMaximumSize(QSize(16777215, 44))
        self.nav_button_1.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.nav_button_1)

        self.nav_button_2 = QPushButton(self.navigationheader_frame)
        self.nav_button_2.setObjectName(u"nav_button_2")
        self.nav_button_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.nav_button_2.sizePolicy().hasHeightForWidth())
        self.nav_button_2.setSizePolicy(sizePolicy)
        self.nav_button_2.setMinimumSize(QSize(0, 0))
        self.nav_button_2.setMaximumSize(QSize(16777215, 44))
        self.nav_button_2.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.nav_button_2)

        self.nav_button_3 = QPushButton(self.navigationheader_frame)
        self.nav_button_3.setObjectName(u"nav_button_3")
        self.nav_button_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.nav_button_3.sizePolicy().hasHeightForWidth())
        self.nav_button_3.setSizePolicy(sizePolicy)
        self.nav_button_3.setMinimumSize(QSize(0, 0))
        self.nav_button_3.setMaximumSize(QSize(16777215, 44))
        self.nav_button_3.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.nav_button_3)


        self.header_right_layout.addWidget(self.navigationheader_frame)


        self.horizontalLayout_3.addLayout(self.header_right_layout)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout.addWidget(self._header_frame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.horizontalLayout = QHBoxLayout(self.page_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.entry_widget = QWidget(self.page_1)
        self.entry_widget.setObjectName(u"entry_widget")
        self.entry_widget.setStyleSheet(u"#entry_widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(46, 46, 46, 55), stop:0.55 rgba(71, 98, 126, 35), stop:0.9375 rgba(85, 102, 113, 38), stop:1 rgba(0, 0, 0, 0));\n"
"}")
        self.gridLayout = QGridLayout(self.entry_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.entry_widget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidget_1 = QTableWidget(self.widget)
        if (self.tableWidget_1.columnCount() < 2):
            self.tableWidget_1.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_1.setObjectName(u"tableWidget_1")
        sizePolicy.setHeightForWidth(self.tableWidget_1.sizePolicy().hasHeightForWidth())
        self.tableWidget_1.setSizePolicy(sizePolicy)
        self.tableWidget_1.setAlternatingRowColors(True)
        self.tableWidget_1.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.horizontalLayout_2.addWidget(self.tableWidget_1)

        self.tableWidget_2 = QTableWidget(self.widget)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.horizontalLayout_2.addWidget(self.tableWidget_2)

        self.tableWidget_3 = QTableWidget(self.widget)
        if (self.tableWidget_3.columnCount() < 2):
            self.tableWidget_3.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        sizePolicy.setHeightForWidth(self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy)
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.horizontalLayout_2.addWidget(self.tableWidget_3)


        self.gridLayout.addWidget(self.widget, 12, 0, 1, 8)

        self.combo_3 = QComboBox(self.entry_widget)
        self.combo_3.addItem("")
        self.combo_3.addItem("")
        self.combo_3.setObjectName(u"combo_3")
        sizePolicy.setHeightForWidth(self.combo_3.sizePolicy().hasHeightForWidth())
        self.combo_3.setSizePolicy(sizePolicy)
        self.combo_3.setMinimumSize(QSize(0, 25))
        self.combo_3.setMaximumSize(QSize(16777215, 25))
        self.combo_3.setStyleSheet(u"/* QComboBox Styles */\n"
"QComboBox {\n"
"color: #2b2d42;\n"
"background-color: qlineargradient(\n"
"spread: pad,\n"
"x1: 1,\n"
"y1: 0,\n"
"x2: 1,\n"
"y2: 1,\n"
"stop: 0 #d9deee,\n"
"stop: 1 #c2c7d5\n"
");\n"
"  border: 1px solid #6272a4;\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"width: 20px;\n"
"border-left-width: 1px;\n"
"border-left-color: #191919;\n"
"border-left-style: solid;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"background-color: #6272a4;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"image: url(://arrow-down.png);\n"
"}\n"
"\n"
"QComboBox,\n"
"QAbstractItemView {\n"
"background-color: qlineargradient(\n"
"spread: pad,\n"
"x1: 1,\n"
"y1: 0,\n"
"x2: 1,\n"
"y2: 1,\n"
"stop: 0 #d9deee,\n"
"stop: 1 #c2c7d5\n"
");\n"
"color: #2b2d42;\n"
"selection-background-color: #6272a4;\n"
"selection-color: #f8f8f2;\n"
"  border: 1px solid #6272a4;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.combo_3, 2, 4, 1, 1)

        self.combo_2 = QComboBox(self.entry_widget)
        self.combo_2.setObjectName(u"combo_2")
        sizePolicy.setHeightForWidth(self.combo_2.sizePolicy().hasHeightForWidth())
        self.combo_2.setSizePolicy(sizePolicy)
        self.combo_2.setMinimumSize(QSize(0, 25))
        self.combo_2.setMaximumSize(QSize(16777215, 25))
        self.combo_2.setStyleSheet(u"/* QComboBox Styles */\n"
"QComboBox {\n"
"color: #2b2d42;\n"
"background-color: qlineargradient(\n"
"spread: pad,\n"
"x1: 1,\n"
"y1: 0,\n"
"x2: 1,\n"
"y2: 1,\n"
"stop: 0 #d9deee,\n"
"stop: 1 #c2c7d5\n"
");\n"
"  border: 1px solid #6272a4;\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"width: 20px;\n"
"border-left-width: 1px;\n"
"border-left-color: #191919;\n"
"border-left-style: solid;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"background-color: #6272a4;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"image: url(://arrow-down.png);\n"
"}\n"
"\n"
"QComboBox,\n"
"QAbstractItemView {\n"
"background-color: qlineargradient(\n"
"spread: pad,\n"
"x1: 1,\n"
"y1: 0,\n"
"x2: 1,\n"
"y2: 1,\n"
"stop: 0 #d9deee,\n"
"stop: 1 #c2c7d5\n"
");\n"
"color: #2b2d42;\n"
"selection-background-color: #6272a4;\n"
"selection-color: #f8f8f2;\n"
"  border: 1px solid #6272a4;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.combo_2, 6, 4, 1, 1)

        self.edit_label_3 = QLabel(self.entry_widget)
        self.edit_label_3.setObjectName(u"edit_label_3")
        self.edit_label_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.edit_label_3.sizePolicy().hasHeightForWidth())
        self.edit_label_3.setSizePolicy(sizePolicy)
        self.edit_label_3.setMinimumSize(QSize(0, 32))
        self.edit_label_3.setMaximumSize(QSize(16777215, 32))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.edit_label_3.setFont(font1)
        self.edit_label_3.setStyleSheet(u"color: #ffffff;")

        self.gridLayout.addWidget(self.edit_label_3, 5, 3, 1, 1)

        self.edit_label_1 = QLabel(self.entry_widget)
        self.edit_label_1.setObjectName(u"edit_label_1")
        self.edit_label_1.setEnabled(True)
        sizePolicy.setHeightForWidth(self.edit_label_1.sizePolicy().hasHeightForWidth())
        self.edit_label_1.setSizePolicy(sizePolicy)
        self.edit_label_1.setMinimumSize(QSize(0, 25))
        self.edit_label_1.setMaximumSize(QSize(16777215, 25))
        self.edit_label_1.setFont(font1)
        self.edit_label_1.setStyleSheet(u"color: #ffffff;")

        self.gridLayout.addWidget(self.edit_label_1, 2, 0, 1, 1)

        self.data_selected = QLabel(self.entry_widget)
        self.data_selected.setObjectName(u"data_selected")
        self.data_selected.setEnabled(True)
        sizePolicy.setHeightForWidth(self.data_selected.sizePolicy().hasHeightForWidth())
        self.data_selected.setSizePolicy(sizePolicy)
        self.data_selected.setMinimumSize(QSize(150, 32))
        self.data_selected.setMaximumSize(QSize(150, 32))
        self.data_selected.setFont(font1)
        self.data_selected.setStyleSheet(u"color: #000000;\n"
"background-color: #d9deee;\n"
"\n"
"font-weight: bold;\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"\n"
"")

        self.gridLayout.addWidget(self.data_selected, 18, 0, 1, 1)

        self.edit_label_6 = QLabel(self.entry_widget)
        self.edit_label_6.setObjectName(u"edit_label_6")
        self.edit_label_6.setEnabled(True)
        sizePolicy.setHeightForWidth(self.edit_label_6.sizePolicy().hasHeightForWidth())
        self.edit_label_6.setSizePolicy(sizePolicy)
        self.edit_label_6.setMinimumSize(QSize(0, 32))
        self.edit_label_6.setMaximumSize(QSize(16777215, 32))
        self.edit_label_6.setFont(font1)
        self.edit_label_6.setStyleSheet(u"color: #ffffff;")

        self.gridLayout.addWidget(self.edit_label_6, 6, 3, 1, 1)

        self.edit_label_2 = QLabel(self.entry_widget)
        self.edit_label_2.setObjectName(u"edit_label_2")
        self.edit_label_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.edit_label_2.sizePolicy().hasHeightForWidth())
        self.edit_label_2.setSizePolicy(sizePolicy)
        self.edit_label_2.setMinimumSize(QSize(0, 32))
        self.edit_label_2.setMaximumSize(QSize(16777215, 32))
        self.edit_label_2.setFont(font1)
        self.edit_label_2.setStyleSheet(u"color: #ffffff;")

        self.gridLayout.addWidget(self.edit_label_2, 2, 3, 1, 1)

        self.edit_2 = QLineEdit(self.entry_widget)
        self.edit_2.setObjectName(u"edit_2")
        self.edit_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.edit_2.sizePolicy().hasHeightForWidth())
        self.edit_2.setSizePolicy(sizePolicy)
        self.edit_2.setMinimumSize(QSize(0, 25))
        self.edit_2.setMaximumSize(QSize(16777215, 25))
        self.edit_2.setStyleSheet(u"/* QLineEdit Styles */\n"
"QLineEdit {\n"
"font-weight: bold;\n"
"color: #2b2d42;\n"
"background-color: qlineargradient(\n"
"spread: pad,\n"
"x1: 1,\n"
"y1: 0,\n"
"x2: 1,\n"
"y2: 1,\n"
"stop: 0 #d9deee,\n"
"stop: 1 #c2c7d5\n"
");\n"
"border: 1px solid #6272a4;\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"important!\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 1px solid #81a1c1;\n"
"background-color: qlineargradient(\n"
"spread: pad,\n"
"x1: 1,\n"
"y1: 0,\n"
"x2: 1,\n"
"y2: 1,\n"
"stop: 0 #d9deee,\n"
"stop: 1 #c2c7d5\n"
");\n"
"}")
        self.edit_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.edit_2, 6, 1, 1, 1)

        self.edit_3 = QLineEdit(self.entry_widget)
        self.edit_3.setObjectName(u"edit_3")
        self.edit_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.edit_3.sizePolicy().hasHeightForWidth())
        self.edit_3.setSizePolicy(sizePolicy)
        self.edit_3.setMinimumSize(QSize(0, 25))
        self.edit_3.setMaximumSize(QSize(16777215, 25))
        self.edit_3.setStyleSheet(u"/* QLineEdit Styles */\n"
"QLineEdit {\n"
"font-weight: bold;\n"
"color: #2b2d42;\n"
"background-color: qlineargradient(\n"
"spread: pad,\n"
"x1: 1,\n"
"y1: 0,\n"
"x2: 1,\n"
"y2: 1,\n"
"stop: 0 #d9deee,\n"
"stop: 1 #c2c7d5\n"
");\n"
"border: 1px solid #6272a4;\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"important!\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 1px solid #81a1c1;\n"
"background-color: qlineargradient(\n"
"spread: pad,\n"
"x1: 1,\n"
"y1: 0,\n"
"x2: 1,\n"
"y2: 1,\n"
"stop: 0 #d9deee,\n"
"stop: 1 #c2c7d5\n"
");\n"
"}")
        self.edit_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.edit_3, 5, 4, 1, 1)

        self.casual_button_1 = QPushButton(self.entry_widget)
        self.casual_button_1.setObjectName(u"casual_button_1")
        sizePolicy.setHeightForWidth(self.casual_button_1.sizePolicy().hasHeightForWidth())
        self.casual_button_1.setSizePolicy(sizePolicy)
        self.casual_button_1.setMinimumSize(QSize(40, 30))
        self.casual_button_1.setMaximumSize(QSize(100, 30))
        self.casual_button_1.setStyleSheet(u"\n"
"QPushButton{\n"
" border-radius: 10px;\n"
" background-color: #FFFFFF;\n"
" border: 3px;\n"
" border-style: outset;\n"
" border-color: #b5c3d0;\n"
"margin: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #d8d8d8;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e6e6e6;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover:pressed {\n"
"    background-color: #d8d8d8;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.casual_button_1.setIconSize(QSize(28, 28))

        self.gridLayout.addWidget(self.casual_button_1, 5, 2, 1, 1)

        self.widget_2 = QWidget(self.entry_widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 30))
        self.widget_2.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setMaximumSize(QSize(16777215, 25))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 25))
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 25))
        self.label_3.setMaximumSize(QSize(16777215, 25))
        self.label_3.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.gridLayout.addWidget(self.widget_2, 11, 0, 1, 8)

        self.list_created = QLabel(self.entry_widget)
        self.list_created.setObjectName(u"list_created")
        self.list_created.setEnabled(True)
        sizePolicy.setHeightForWidth(self.list_created.sizePolicy().hasHeightForWidth())
        self.list_created.setSizePolicy(sizePolicy)
        self.list_created.setMinimumSize(QSize(150, 32))
        self.list_created.setMaximumSize(QSize(150, 32))
        self.list_created.setFont(font1)
        self.list_created.setStyleSheet(u"color: #000000;\n"
"background-color: #d9deee;\n"
"\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"font-weight: bold;")

        self.gridLayout.addWidget(self.list_created, 18, 7, 1, 1)

        self.progress_bar = QProgressBar(self.entry_widget)
        self.progress_bar.setObjectName(u"progress_bar")
        sizePolicy.setHeightForWidth(self.progress_bar.sizePolicy().hasHeightForWidth())
        self.progress_bar.setSizePolicy(sizePolicy)
        self.progress_bar.setStyleSheet(u"QProgressBar {\n"
"    background-color: #e1e1e1;\n"
"    border: none;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #C5E6AC;\n"
"    border-radius: 5px;\n"
"}")
        self.progress_bar.setValue(0)

        self.gridLayout.addWidget(self.progress_bar, 18, 1, 1, 6)

        self.combo_1 = QComboBox(self.entry_widget)
        self.combo_1.setObjectName(u"combo_1")
        sizePolicy.setHeightForWidth(self.combo_1.sizePolicy().hasHeightForWidth())
        self.combo_1.setSizePolicy(sizePolicy)
        self.combo_1.setMinimumSize(QSize(0, 25))
        self.combo_1.setMaximumSize(QSize(16777215, 25))
        self.combo_1.setStyleSheet(u"/* QComboBox Styles */\n"
"QComboBox {\n"
"color: #2b2d42;\n"
"background-color: qlineargradient(\n"
"spread: pad,\n"
"x1: 1,\n"
"y1: 0,\n"
"x2: 1,\n"
"y2: 1,\n"
"stop: 0 #d9deee,\n"
"stop: 1 #c2c7d5\n"
");\n"
"  border: 1px solid #6272a4;\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"width: 20px;\n"
"border-left-width: 1px;\n"
"border-left-color: #191919;\n"
"border-left-style: solid;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"background-color: #6272a4;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"image: url(://arrow-down.png);\n"
"}\n"
"\n"
"QComboBox,\n"
"QAbstractItemView {\n"
"background-color: qlineargradient(\n"
"spread: pad,\n"
"x1: 1,\n"
"y1: 0,\n"
"x2: 1,\n"
"y2: 1,\n"
"stop: 0 #d9deee,\n"
"stop: 1 #c2c7d5\n"
");\n"
"color: #2b2d42;\n"
"selection-background-color: #6272a4;\n"
"selection-color: #f8f8f2;\n"
"  border: 1px solid #6272a4;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.combo_1, 2, 1, 1, 1)

        self.edit_label_4 = QLabel(self.entry_widget)
        self.edit_label_4.setObjectName(u"edit_label_4")
        self.edit_label_4.setEnabled(True)
        sizePolicy.setHeightForWidth(self.edit_label_4.sizePolicy().hasHeightForWidth())
        self.edit_label_4.setSizePolicy(sizePolicy)
        self.edit_label_4.setMinimumSize(QSize(0, 25))
        self.edit_label_4.setMaximumSize(QSize(16777215, 25))
        self.edit_label_4.setFont(font1)
        self.edit_label_4.setStyleSheet(u"color: #ffffff;")

        self.gridLayout.addWidget(self.edit_label_4, 5, 0, 1, 1)

        self.edit_1 = QLineEdit(self.entry_widget)
        self.edit_1.setObjectName(u"edit_1")
        self.edit_1.setEnabled(True)
        sizePolicy.setHeightForWidth(self.edit_1.sizePolicy().hasHeightForWidth())
        self.edit_1.setSizePolicy(sizePolicy)
        self.edit_1.setMinimumSize(QSize(0, 25))
        self.edit_1.setMaximumSize(QSize(16777215, 25))
        self.edit_1.setStyleSheet(u"/* QLineEdit Styles */\n"
"QLineEdit {\n"
"font-weight: bold;\n"
"color: #2b2d42;\n"
"background-color: qlineargradient(\n"
"spread: pad,\n"
"x1: 1,\n"
"y1: 0,\n"
"x2: 1,\n"
"y2: 1,\n"
"stop: 0 #d9deee,\n"
"stop: 1 #c2c7d5\n"
");\n"
"border: 1px solid #6272a4;\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"important!\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 1px solid #81a1c1;\n"
"background-color: qlineargradient(\n"
"spread: pad,\n"
"x1: 1,\n"
"y1: 0,\n"
"x2: 1,\n"
"y2: 1,\n"
"stop: 0 #d9deee,\n"
"stop: 1 #c2c7d5\n"
");\n"
"}")
        self.edit_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.edit_1, 5, 1, 1, 1)

        self.edit_label_5 = QLabel(self.entry_widget)
        self.edit_label_5.setObjectName(u"edit_label_5")
        self.edit_label_5.setEnabled(True)
        sizePolicy.setHeightForWidth(self.edit_label_5.sizePolicy().hasHeightForWidth())
        self.edit_label_5.setSizePolicy(sizePolicy)
        self.edit_label_5.setMinimumSize(QSize(0, 25))
        self.edit_label_5.setMaximumSize(QSize(16777215, 25))
        self.edit_label_5.setFont(font1)
        self.edit_label_5.setStyleSheet(u"color: #ffffff;")

        self.gridLayout.addWidget(self.edit_label_5, 6, 0, 1, 1)

        self.casual_button_2 = QPushButton(self.entry_widget)
        self.casual_button_2.setObjectName(u"casual_button_2")
        sizePolicy.setHeightForWidth(self.casual_button_2.sizePolicy().hasHeightForWidth())
        self.casual_button_2.setSizePolicy(sizePolicy)
        self.casual_button_2.setMinimumSize(QSize(40, 40))
        self.casual_button_2.setMaximumSize(QSize(100, 40))
        self.casual_button_2.setStyleSheet(u"\n"
"QPushButton{\n"
" border-radius: 10px;\n"
" background-color: #FFFFFF;\n"
" border: 3px;\n"
" border-style: outset;\n"
" border-color: #b5c3d0;\n"
"margin: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #d8d8d8;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e6e6e6;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover:pressed {\n"
"    background-color: #d8d8d8;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.casual_button_2.setIconSize(QSize(28, 28))

        self.gridLayout.addWidget(self.casual_button_2, 6, 7, 1, 1)

        self.green_button = QPushButton(self.entry_widget)
        self.green_button.setObjectName(u"green_button")
        self.green_button.setEnabled(True)
        sizePolicy.setHeightForWidth(self.green_button.sizePolicy().hasHeightForWidth())
        self.green_button.setSizePolicy(sizePolicy)
        self.green_button.setMinimumSize(QSize(32, 32))
        self.green_button.setMaximumSize(QSize(100, 32))
        self.green_button.setSizeIncrement(QSize(0, 0))
        self.green_button.setBaseSize(QSize(0, 0))
        self.green_button.setMouseTracking(True)
        self.green_button.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #50d236, stop: 1 #6ab718);\n"
"color: white;\n"
"border: 3px solid #50d236;\n"
"padding: 5px 15px;\n"
"font: bold 14px;\n"
"transition: all 0.2s;\n"
"text-transform: uppercase;\n"
"letter-spacing: 1px;\n"
"border-radius: 5px;\n"
"box-shadow: 0px 5px 0px #B71C1C;\n"
" border-radius: 10px;\n"
"\n"
" border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #adee82, stop: 1 #50d236);\n"
"box-shadow: 0px 2px 0px #50d236;\n"
"transform: translateY(-2px);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #50d236;\n"
"box-shadow: none;\n"
"transform: translateY(0px);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: #BDBDBD;\n"
"color: #757575;\n"
"border-color: #9E9E9E;\n"
"box-shadow: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/edit/ico/bleistift_1.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.green_button.setIcon(icon)
        self.green_button.setIconSize(QSize(28, 28))

        self.gridLayout.addWidget(self.green_button, 6, 5, 1, 1)

        self.casual_button_3 = QPushButton(self.entry_widget)
        self.casual_button_3.setObjectName(u"casual_button_3")
        sizePolicy.setHeightForWidth(self.casual_button_3.sizePolicy().hasHeightForWidth())
        self.casual_button_3.setSizePolicy(sizePolicy)
        self.casual_button_3.setMinimumSize(QSize(40, 40))
        self.casual_button_3.setMaximumSize(QSize(100, 40))
        self.casual_button_3.setStyleSheet(u"\n"
"QPushButton{\n"
" border-radius: 10px;\n"
" background-color: #FFFFFF;\n"
" border: 3px;\n"
" border-style: outset;\n"
" border-color: #b5c3d0;\n"
"margin: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #d8d8d8;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e6e6e6;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover:pressed {\n"
"    background-color: #d8d8d8;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.casual_button_3.setIconSize(QSize(28, 28))

        self.gridLayout.addWidget(self.casual_button_3, 6, 6, 1, 1)

        self.red_button = QPushButton(self.entry_widget)
        self.red_button.setObjectName(u"red_button")
        self.red_button.setEnabled(True)
        sizePolicy.setHeightForWidth(self.red_button.sizePolicy().hasHeightForWidth())
        self.red_button.setSizePolicy(sizePolicy)
        self.red_button.setMinimumSize(QSize(32, 32))
        self.red_button.setMaximumSize(QSize(100, 32))
        self.red_button.setSizeIncrement(QSize(0, 0))
        self.red_button.setBaseSize(QSize(0, 0))
        self.red_button.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #F44336, stop: 1 #B71C1C);\n"
"color: white;\n"
"border: 3px solid #B71C1C;\n"
"padding: 5px 15px;\n"
"font: bold 14px;\n"
"transition: all 0.2s;\n"
"text-transform: uppercase;\n"
"letter-spacing: 1px;\n"
"border-radius: 5px;\n"
"box-shadow: 0px 5px 0px #B71C1C;\n"
" border-radius: 10px;\n"
"\n"
" border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 rgb(255, 131, 131), stop: 1 #ce2020);\n"
"box-shadow: 0px 2px 0px #B71C1C;\n"
"transform: translateY(-2px);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #B71C1C;\n"
"box-shadow: none;\n"
"transform: translateY(0px);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: #BDBDBD;\n"
"color: #757575;\n"
"border-color: #9E9E9E;\n"
"box-shadow: none;\n"
"}")

        self.gridLayout.addWidget(self.red_button, 2, 5, 1, 1)


        self.horizontalLayout.addWidget(self.entry_widget)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        LLMandSCRAP.setCentralWidget(self.centralwidget)

        self.retranslateUi(LLMandSCRAP)

        QMetaObject.connectSlotsByName(LLMandSCRAP)
    # setupUi

    def retranslateUi(self, LLMandSCRAP):
        LLMandSCRAP.setWindowTitle(QCoreApplication.translate("LLMandSCRAP", u"MainWindow", None))
        self._subtitle_label.setText(QCoreApplication.translate("LLMandSCRAP", u"<html><head/><body><p><span style=\" font-size:22pt;\">Textscrapping and LLM</span></p></body></html>", None))
        self.nav_button_1.setText(QCoreApplication.translate("LLMandSCRAP", u"nav_button_1", None))
        self.nav_button_2.setText(QCoreApplication.translate("LLMandSCRAP", u"nav_button_2", None))
        self.nav_button_3.setText(QCoreApplication.translate("LLMandSCRAP", u"nav_button_3", None))
        ___qtablewidgetitem = self.tableWidget_1.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LLMandSCRAP", u"Formel", None));
        ___qtablewidgetitem1 = self.tableWidget_1.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LLMandSCRAP", u"Beschreibung", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("LLMandSCRAP", u"Formel", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("LLMandSCRAP", u"Beschreibung", None));
        ___qtablewidgetitem4 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("LLMandSCRAP", u"Formel", None));
        ___qtablewidgetitem5 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("LLMandSCRAP", u"Beschreibung", None));
        self.combo_3.setItemText(0, QCoreApplication.translate("LLMandSCRAP", u"1", None))
        self.combo_3.setItemText(1, QCoreApplication.translate("LLMandSCRAP", u"2", None))

        self.edit_label_3.setText(QCoreApplication.translate("LLMandSCRAP", u"....", None))
        self.edit_label_1.setText(QCoreApplication.translate("LLMandSCRAP", u"DATA SCRAP !!", None))
        self.data_selected.setText(QCoreApplication.translate("LLMandSCRAP", u"REAAADDYYY!!!", None))
        self.edit_label_6.setText(QCoreApplication.translate("LLMandSCRAP", u"....", None))
        self.edit_label_2.setText(QCoreApplication.translate("LLMandSCRAP", u"Tabelle", None))
        self.edit_2.setInputMask("")
        self.edit_2.setPlaceholderText("")
        self.edit_3.setInputMask("")
        self.edit_3.setPlaceholderText("")
        self.casual_button_1.setText(QCoreApplication.translate("LLMandSCRAP", u"Datei \u00f6ffnen", None))
        self.label.setText(QCoreApplication.translate("LLMandSCRAP", u"Tabelle 1", None))
        self.label_2.setText(QCoreApplication.translate("LLMandSCRAP", u"Tabelle 2", None))
        self.label_3.setText(QCoreApplication.translate("LLMandSCRAP", u"Tabelle 3", None))
        self.list_created.setText(QCoreApplication.translate("LLMandSCRAP", u"DOOONEEEE!!!", None))
        self.progress_bar.setFormat("")
        self.edit_label_4.setText(QCoreApplication.translate("LLMandSCRAP", u"TEXT FILE:", None))
        self.edit_1.setInputMask("")
        self.edit_1.setPlaceholderText("")
        self.edit_label_5.setText(QCoreApplication.translate("LLMandSCRAP", u"WEBSITE:", None))
        self.casual_button_2.setText(QCoreApplication.translate("LLMandSCRAP", u"Speichern", None))
        self.green_button.setText(QCoreApplication.translate("LLMandSCRAP", u"START", None))
        self.casual_button_3.setText(QCoreApplication.translate("LLMandSCRAP", u"Vergleichen", None))
        self.red_button.setText("")
    # retranslateUi

