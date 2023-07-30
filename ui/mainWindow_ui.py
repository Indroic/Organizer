# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QToolButton, QVBoxLayout, QWidget)
import ui.source.icons_rc

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
        self.stackedWidget.setGeometry(QRect(30, 60, 401, 601))
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
        self.gear_btn.setStyleSheet(u"background: rgba(0,0,0, 0);\n"
"color: #fff;")
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
        self.organize_btn.setMaximumSize(QSize(200, 50))

        self.btn.addWidget(self.organize_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.btn.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.btn)

        self.stackedWidget.addWidget(self.home)
        self.config = QWidget()
        self.config.setObjectName(u"config")
        self.layoutWidget = QWidget(self.config)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 381, 578))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.back_btn = QToolButton(self.layoutWidget)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setStyleSheet(u"background: rgba(0,0,0,0);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.back_btn.setIcon(icon1)
        self.back_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_11.addWidget(self.back_btn)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout_11)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_9.addWidget(self.label)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.filters_created_list = QListWidget(self.layoutWidget)
        self.filters_created_list.setObjectName(u"filters_created_list")
        self.filters_created_list.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_10.addWidget(self.filters_created_list)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.edit_btn = QToolButton(self.layoutWidget)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setMinimumSize(QSize(60, 20))
        self.edit_btn.setMaximumSize(QSize(60, 20))

        self.verticalLayout_8.addWidget(self.edit_btn)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)

        self.delete_btn = QToolButton(self.layoutWidget)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setMinimumSize(QSize(60, 20))
        self.delete_btn.setMaximumSize(QSize(50, 20))

        self.verticalLayout_8.addWidget(self.delete_btn)


        self.horizontalLayout_10.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.verticalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_9)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.text_title = QLabel(self.layoutWidget)
        self.text_title.setObjectName(u"text_title")

        self.horizontalLayout_7.addWidget(self.text_title)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.name_label = QLabel(self.layoutWidget)
        self.name_label.setObjectName(u"name_label")

        self.verticalLayout_4.addWidget(self.name_label)

        self.name_input = QLineEdit(self.layoutWidget)
        self.name_input.setObjectName(u"name_input")

        self.verticalLayout_4.addWidget(self.name_input)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.dir_label = QLabel(self.layoutWidget)
        self.dir_label.setObjectName(u"dir_label")

        self.verticalLayout_5.addWidget(self.dir_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dir_input = QLineEdit(self.layoutWidget)
        self.dir_input.setObjectName(u"dir_input")

        self.horizontalLayout_3.addWidget(self.dir_input)

        self.dir_select_btn = QToolButton(self.layoutWidget)
        self.dir_select_btn.setObjectName(u"dir_select_btn")
        self.dir_select_btn.setMinimumSize(QSize(40, 20))
        self.dir_select_btn.setMaximumSize(QSize(40, 20))

        self.horizontalLayout_3.addWidget(self.dir_select_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_extension_label = QLabel(self.layoutWidget)
        self.add_extension_label.setObjectName(u"add_extension_label")

        self.verticalLayout.addWidget(self.add_extension_label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.add_extension_input = QLineEdit(self.layoutWidget)
        self.add_extension_input.setObjectName(u"add_extension_input")

        self.horizontalLayout_4.addWidget(self.add_extension_input)

        self.add_extension_btn = QToolButton(self.layoutWidget)
        self.add_extension_btn.setObjectName(u"add_extension_btn")
        self.add_extension_btn.setMinimumSize(QSize(40, 20))
        self.add_extension_btn.setMaximumSize(QSize(40, 20))

        self.horizontalLayout_4.addWidget(self.add_extension_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.extensions_list_label = QLabel(self.layoutWidget)
        self.extensions_list_label.setObjectName(u"extensions_list_label")

        self.verticalLayout_6.addWidget(self.extensions_list_label)

        self.extensions_list = QListWidget(self.layoutWidget)
        self.extensions_list.setObjectName(u"extensions_list")
        self.extensions_list.setMaximumSize(QSize(16777215, 100))
        self.extensions_list.setStyleSheet(u"color: white;")

        self.verticalLayout_6.addWidget(self.extensions_list)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.create_filter = QPushButton(self.layoutWidget)
        self.create_filter.setObjectName(u"create_filter")
        self.create_filter.setMinimumSize(QSize(200, 50))
        self.create_filter.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_8.addWidget(self.create_filter)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)


        self.horizontalLayout_11.addLayout(self.verticalLayout_10)

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
        self.back_btn.setText(QCoreApplication.translate("Main", u"...", None))
        self.label.setText(QCoreApplication.translate("Main", u"Filtros:", None))
        self.edit_btn.setText(QCoreApplication.translate("Main", u"Editar", None))
        self.delete_btn.setText(QCoreApplication.translate("Main", u"Eliminar", None))
        self.text_title.setText(QCoreApplication.translate("Main", u"Crear Filtro Nuevo", None))
        self.name_label.setText(QCoreApplication.translate("Main", u"Nombre", None))
        self.dir_label.setText(QCoreApplication.translate("Main", u"Carpeta", None))
        self.dir_select_btn.setText(QCoreApplication.translate("Main", u"...", None))
        self.add_extension_label.setText(QCoreApplication.translate("Main", u"Agregar Extension", None))
        self.add_extension_btn.setText(QCoreApplication.translate("Main", u"+", None))
        self.extensions_list_label.setText(QCoreApplication.translate("Main", u"Extensiones A\u00f1adidas", None))
        self.create_filter.setText(QCoreApplication.translate("Main", u"Crear", None))
    # retranslateUi

