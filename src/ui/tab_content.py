# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_content.ui'
##
## Created by: Qt User Interface Compiler version 5.15.12
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(660, 525)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.information = QHBoxLayout()
        self.information.setObjectName(u"information")
        self.load_rsv = QPushButton(Form)
        self.load_rsv.setObjectName(u"load_rsv")

        self.information.addWidget(self.load_rsv)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.information.addWidget(self.line)

        self.bank_name = QComboBox(Form)
        self.bank_name.setObjectName(u"bank_name")

        self.information.addWidget(self.bank_name)

        self.currency = QComboBox(Form)
        self.currency.setObjectName(u"currency")

        self.information.addWidget(self.currency)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.information.addItem(self.horizontalSpacer)

        self.initial_balance = QDoubleSpinBox(Form)
        self.initial_balance.setObjectName(u"initial_balance")
        self.initial_balance.setDecimals(3)

        self.information.addWidget(self.initial_balance)


        self.verticalLayout.addLayout(self.information)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_3.addWidget(self.comboBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_4.addWidget(self.comboBox_3)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.comboBox_4 = QComboBox(Form)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_5.addWidget(self.comboBox_4)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.comboBox_5 = QComboBox(Form)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.verticalLayout_6.addWidget(self.comboBox_5)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.comboBox_6 = QComboBox(Form)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.verticalLayout_7.addWidget(self.comboBox_6)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.save_statements = QPushButton(Form)
        self.save_statements.setObjectName(u"save_statements")

        self.verticalLayout.addWidget(self.save_statements)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.load_rsv.setText(QCoreApplication.translate("Form", u"Cargar RSV...", None))
        self.bank_name.setPlaceholderText(QCoreApplication.translate("Form", u"Banco", None))
        self.currency.setCurrentText("")
        self.currency.setPlaceholderText(QCoreApplication.translate("Form", u"Moneda", None))
        self.label.setText(QCoreApplication.translate("Form", u"Fecha", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"N\u00ba Referencia", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Descripci\u00f3n", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"D\u00e9bitos", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Cr\u00e9ditos", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Balance", None))
        self.save_statements.setText(QCoreApplication.translate("Form", u"Salvar", None))
    # retranslateUi

