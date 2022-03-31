# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tela.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 251)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 341, 51))
        font = QFont()
        font.setFamily(u"MV Boli")
        font.setPointSize(14)
        self.label.setFont(font)
        self.pushButtonCalcular = QPushButton(Form)
        self.pushButtonCalcular.setObjectName(u"pushButtonCalcular")
        self.pushButtonCalcular.setGeometry(QRect(30, 190, 91, 41))
        font1 = QFont()
        font1.setFamily(u"MV Boli")
        font1.setPointSize(16)
        self.pushButtonCalcular.setFont(font1)
        self.pushButtonCalcular.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(209,209,209);\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(9,125,235);\n"
"	color: #fff;\n"
"}")
        self.pushButtonLimpar = QPushButton(Form)
        self.pushButtonLimpar.setObjectName(u"pushButtonLimpar")
        self.pushButtonLimpar.setGeometry(QRect(280, 190, 91, 41))
        self.pushButtonLimpar.setFont(font1)
        self.pushButtonLimpar.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(209,209,209);\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(9,125,235);\n"
"	color: #fff;\n"
"}")
        self.pushButtonSair = QPushButton(Form)
        self.pushButtonSair.setObjectName(u"pushButtonSair")
        self.pushButtonSair.setGeometry(QRect(150, 190, 101, 41))
        self.pushButtonSair.setFont(font1)
        self.pushButtonSair.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(209,209,209);\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(9,125,235);\n"
"	color: #fff;\n"
"}")
        self.lineEditPosto1 = QLineEdit(Form)
        self.lineEditPosto1.setObjectName(u"lineEditPosto1")
        self.lineEditPosto1.setGeometry(QRect(10, 80, 171, 31))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 171, 21))
        font2 = QFont()
        font2.setFamily(u"Myanmar Text")
        font2.setPointSize(8)
        self.label_2.setFont(font2)
        self.lineEditPosto2 = QLineEdit(Form)
        self.lineEditPosto2.setObjectName(u"lineEditPosto2")
        self.lineEditPosto2.setGeometry(QRect(220, 80, 171, 31))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 60, 161, 21))
        self.label_3.setFont(font2)
        self.lineEditTanque = QLineEdit(Form)
        self.lineEditTanque.setObjectName(u"lineEditTanque")
        self.lineEditTanque.setGeometry(QRect(120, 140, 171, 31))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 120, 171, 21))
        self.label_4.setFont(font2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Calculadora de calculo de combustivel", None))
        self.pushButtonCalcular.setText(QCoreApplication.translate("Form", u"Calcular", None))
        self.pushButtonLimpar.setText(QCoreApplication.translate("Form", u"Limpar", None))
        self.pushButtonSair.setText(QCoreApplication.translate("Form", u"Sair", None))
        self.lineEditPosto1.setPlaceholderText(QCoreApplication.translate("Form", u"Ex: 6.999", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Insira o valor do primeiro posto", None))
        self.lineEditPosto2.setPlaceholderText(QCoreApplication.translate("Form", u"Ex: 6.999", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Insira o valor do outro posto", None))
        self.lineEditTanque.setPlaceholderText(QCoreApplication.translate("Form", u"Total em litros Ex: 54", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Capacidade total do tanque", None))
    # retranslateUi

