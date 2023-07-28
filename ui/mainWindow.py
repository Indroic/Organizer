# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,QMetaObject, QRect, QSize)
from PySide6.QtGui import ( QIcon, QPixmap)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
    QListWidget,QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import source.icons_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(450, 700)
        Main.setMinimumSize(QSize(400, 600))
        Main.setMaximumSize(QSize(450, 700))
        Main.setStyleSheet(u"")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(400, 600))
        self.centralwidget.setMaximumSize(QSize(570, 840))
        self.centralwidget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QRect(30, 50, 401, 611))
        self.stackedWidget.setFrameShape(QFrame.VLine)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.body = QWidget(self.home)
        self.body.setObjectName(u"body")
        self.body.setGeometry(QRect(6, 0, 371, 601))
        self.verticalLayout_3 = QVBoxLayout(self.body)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 20, 10, 20)
        self.gear_layout = QHBoxLayout()
        self.gear_layout.setObjectName(u"gear_layout")
        self.gear_btn = QPushButton(self.body)
        self.gear_btn.setObjectName(u"gear_btn")
        self.gear_btn.setStyleSheet(u"background: rgba(0,0,0, 0);")
        icon = QIcon()
        icon.addFile(u":/icons/gear.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.gear_btn.setIcon(icon)
        self.gear_btn.setIconSize(QSize(20, 20))

        self.gear_layout.addWidget(self.gear_btn)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gear_layout.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addLayout(self.gear_layout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.logo = QLabel(self.body)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(90, 90))
        self.logo.setMaximumSize(QSize(90, 90))
        self.logo.setPixmap(QPixmap(u":/logo/logo.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.nombre = QLabel(self.body)
        self.nombre.setObjectName(u"nombre")

        self.horizontalLayout_2.addWidget(self.nombre)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.input_dir_2 = QVBoxLayout()
        self.input_dir_2.setSpacing(0)
        self.input_dir_2.setObjectName(u"input_dir_2")
        self.label_input_dir = QLabel(self.body)
        self.label_input_dir.setObjectName(u"label_input_dir")

        self.input_dir_2.addWidget(self.label_input_dir)

        self.input_button = QHBoxLayout()
        self.input_button.setSpacing(10)
        self.input_button.setObjectName(u"input_button")
        self.input_dir = QLabel(self.body)
        self.input_dir.setObjectName(u"input_dir")
        self.input_dir.setMinimumSize(QSize(200, 0))

        self.input_button.addWidget(self.input_dir)

        self.select_dir = QPushButton(self.body)
        self.select_dir.setObjectName(u"select_dir")
        self.select_dir.setMinimumSize(QSize(40, 20))
        self.select_dir.setMaximumSize(QSize(40, 20))
        self.select_dir.setAutoExclusive(False)

        self.input_button.addWidget(self.select_dir)


        self.input_dir_2.addLayout(self.input_button)


        self.verticalLayout_3.addLayout(self.input_dir_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.label_select_filter = QLabel(self.body)
        self.label_select_filter.setObjectName(u"label_select_filter")
        self.label_select_filter.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_select_filter)

        self.filters_list = QListWidget(self.body)
        self.filters_list.setObjectName(u"filters_list")
        self.filters_list.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout_3.addWidget(self.filters_list)

        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn = QHBoxLayout()
        self.btn.setObjectName(u"btn")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.btn.addItem(self.horizontalSpacer_3)

        self.organize_btn = QPushButton(self.body)
        self.organize_btn.setObjectName(u"organize_btn")
        self.organize_btn.setMinimumSize(QSize(200, 50))

        self.btn.addWidget(self.organize_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.btn.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.btn)

        self.stackedWidget.addWidget(self.home)
        self.config = QWidget()
        self.config.setObjectName(u"config")
        self.stackedWidget.addWidget(self.config)
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
        self.gear_btn.setText("")
        self.logo.setText("")
        self.nombre.setText(QCoreApplication.translate("Main", u"Organizador Personar DL", None))
        self.label_input_dir.setText(QCoreApplication.translate("Main", u"Carpeta:", None))
        self.input_dir.setText(QCoreApplication.translate("Main", u"C:/", None))
        self.select_dir.setText(QCoreApplication.translate("Main", u"...", None))
        self.label_select_filter.setText(QCoreApplication.translate("Main", u"Seleccione Filtro:", None))
        self.organize_btn.setText(QCoreApplication.translate("Main", u"Organizar", None))
    # retranslateUi

