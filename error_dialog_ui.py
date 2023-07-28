# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_self.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import source.icons_rc


class ErrorDialog(QDialog):
    def __init__(self, message):
        super().__init__()
        if not self.objectName():
            self.setObjectName(u"Dialog")
        self.resize(300, 100)
        self.setMinimumSize(QSize(300, 100))
        self.setMaximumSize(QSize(300, 100))
        self.setStyleSheet(open("dialogs_styles.css", "r").read())
        self.horizontalLayout_3 = QHBoxLayout(self)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.body = QWidget(self)
        self.body.setObjectName(u"body")
        self.body.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_2 = QHBoxLayout(self.body)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.icon_success = QLabel(self.body)
        self.icon_success.setObjectName(u"icon_success")
        self.icon_success.setMinimumSize(QSize(30, 40))
        self.icon_success.setMaximumSize(QSize(40, 40))
        self.icon_success.setPixmap(QPixmap(u":/icons/error.svg"))
        self.icon_success.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.icon_success)

        self.label_2 = QLabel(self.body)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100000, 30))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setText(message)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.body)

        self.boton = QWidget(self)
        self.boton.setObjectName(u"boton")
        self.boton.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.boton)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.boton)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(80, 30))
        self.pushButton.setText("Ok")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.boton)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.pushButton.clicked.connect(self.close)


        QMetaObject.connectSlotsByName(self)
    # setupUi

 