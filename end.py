# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'end.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_End_Form(object):
    def setupUi(self, End_Form):
        if not End_Form.objectName():
            End_Form.setObjectName(u"End_Form")
        End_Form.resize(680, 400)
        End_Form.setMinimumSize(QSize(680, 400))
        End_Form.setMaximumSize(QSize(680, 400))
        self.centralwidget = QWidget(End_Form)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        End_Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(End_Form)

        QMetaObject.connectSlotsByName(End_Form)
    # setupUi

    def retranslateUi(self, End_Form):
        End_Form.setWindowTitle(QCoreApplication.translate("End_Form", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("End_Form", u"MY APP - ADD HERE YOUR WIDGETS", None))
    # retranslateUi

