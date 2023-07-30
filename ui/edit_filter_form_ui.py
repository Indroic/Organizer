# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_filter_form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
    QMetaObject,
    QSize)
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import ( QDialog, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QFileDialog)

from handlers.file_handler import Filter

class Ui_EditFilter(QDialog):
    def __init__(self, filter: Filter):
        super().__init__()
        if not self.objectName():
            self.setObjectName(u"Dialog")
        self.resize(339, 387)
        self.horizontalLayout = QHBoxLayout(self)
        self.setWindowTitle(u"Edit Filter")
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.setStyleSheet(open("ui/source/styles/dialogs_styles.css", "r").read())
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.text_title_2 = QLabel(self)
        self.text_title_2.setObjectName(u"text_title_2")
        self.setWindowIcon(QPixmap("ui/source/logo.png"))
        self.setMaximumSize(QSize(340, 433))
        self.setMinimumSize(QSize(340, 433))

        self.horizontalLayout_11.addWidget(self.text_title_2)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.dir_label_2 = QLabel(self)
        self.dir_label_2.setObjectName(u"dir_label_2")

        self.verticalLayout_13.addWidget(self.dir_label_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.dir_input_2 = QLineEdit(self)
        self.dir_input_2.setObjectName(u"dir_input_2")

        self.horizontalLayout_13.addWidget(self.dir_input_2)

        self.dir_select_btn_2 = QToolButton(self)
        self.dir_select_btn_2.setObjectName(u"dir_select_btn_2")
        self.dir_select_btn_2.setMinimumSize(QSize(40, 20))

        self.horizontalLayout_13.addWidget(self.dir_select_btn_2)


        self.verticalLayout_13.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_12.addLayout(self.verticalLayout_13)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.add_extension_label_2 = QLabel(self)
        self.add_extension_label_2.setObjectName(u"add_extension_label_2")

        self.verticalLayout_2.addWidget(self.add_extension_label_2)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.add_extension_input_2 = QLineEdit(self)
        self.add_extension_input_2.setObjectName(u"add_extension_input_2")

        self.horizontalLayout_15.addWidget(self.add_extension_input_2)

        self.add_extension_btn_2 = QToolButton(self)
        self.add_extension_btn_2.setObjectName(u"add_extension_btn_2")
        self.add_extension_btn_2.setMinimumSize(QSize(40, 20))

        self.horizontalLayout_15.addWidget(self.add_extension_btn_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_14.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_14)


        self.verticalLayout_11.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_12)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.extensions_list_label_2 = QLabel(self)
        self.extensions_list_label_2.setObjectName(u"extensions_list_label_2")

        self.verticalLayout_14.addWidget(self.extensions_list_label_2)

        self.extensions_list_2 = QListWidget(self)
        self.extensions_list_2.setObjectName(u"extensions_list_2")
        self.extensions_list_2.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_14.addWidget(self.extensions_list_2)


        self.verticalLayout_11.addLayout(self.verticalLayout_14)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_13)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_15)

        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(200, 30))

        self.horizontalLayout_16.addWidget(self.pushButton_2)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_16)


        self.verticalLayout_11.addLayout(self.horizontalLayout_16)


        self.horizontalLayout.addLayout(self.verticalLayout_11)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
        self.dir_output_dialog = QFileDialog(self)

        self.dir_output_dialog.setFileMode(QFileDialog.Directory)

        self.dir_output_dialog.setWindowTitle("Seleccionar Carpeta")
     
        self.dir_input_2.setText(filter.dir_output)
        self.extensions_list_2.addItems(filter.extensions)
        
        self.filter = filter
    # setupUi
    
        self.dir_select_btn_2.clicked.connect(self.select_dir_output)
        self.pushButton_2.clicked.connect(self.save)
        self.add_extension_btn_2.clicked.connect(self.add_extension_list)
    def add_extension_list(self):
        lista = [self.extensions_list_2.item(row).text() for row in range(self.extensions_list_2.count())]
        if not self.add_extension_input_2.text():
            return
        
        if self.add_extension_input_2.text() in lista:
            self.add_extension_input_2.clear()
            return
        
        lista.append(self.add_extension_input_2.text())
        self.add_extension_input_2.clear()
        self.extensions_list_2.clear()
        self.extensions_list_2.addItems(lista)
    def save(self):
        edited_filter = Filter(
            name=self.filter.name,
            extensions=self.filter.extensions,
            dir_output=self.dir_input_2.text()
        )
        
        edited_filter.save()
        
        
        self.close()
        
    def select_dir_output(self):
        self.dir_output_dialog.exec()
        self.dir_input_2.setText(self.dir_output_dialog.selectedFiles()[0])

    def retranslateUi(self):
        self.text_title_2.setText(QCoreApplication.translate("Dialog", u"Editar Filtro", None))
        self.dir_label_2.setText(QCoreApplication.translate("Dialog", u"Carpeta", None))
        self.dir_select_btn_2.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.add_extension_label_2.setText(QCoreApplication.translate("Dialog", u"Agregar Extension", None))
        self.add_extension_btn_2.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.extensions_list_label_2.setText(QCoreApplication.translate("Dialog", u"Extensiones A\u00f1adidas", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
    # retranslateUi

