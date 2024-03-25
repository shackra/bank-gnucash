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
        self.bank_name.addItem("")
        self.bank_name.addItem("")
        self.bank_name.addItem("")
        self.bank_name.addItem("")
        self.bank_name.addItem("")
        self.bank_name.addItem("")
        self.bank_name.addItem("")
        self.bank_name.setObjectName(u"bank_name")
        self.bank_name.setEnabled(False)
        self.bank_name.setEditable(False)

        self.information.addWidget(self.bank_name)

        self.currency = QComboBox(Form)
        self.currency.addItem("")
        self.currency.addItem("")
        self.currency.setObjectName(u"currency")
        self.currency.setEnabled(False)

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
        self.date = QVBoxLayout()
        self.date.setObjectName(u"date")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.date.addWidget(self.label)

        self.date_column = QComboBox(Form)
        self.date_column.setObjectName(u"date_column")
        self.date_column.setEnabled(False)

        self.date.addWidget(self.date_column)


        self.horizontalLayout.addLayout(self.date)

        self.reference = QVBoxLayout()
        self.reference.setObjectName(u"reference")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.reference.addWidget(self.label_2)

        self.reference_column = QComboBox(Form)
        self.reference_column.setObjectName(u"reference_column")
        self.reference_column.setEnabled(False)

        self.reference.addWidget(self.reference_column)


        self.horizontalLayout.addLayout(self.reference)

        self.description = QVBoxLayout()
        self.description.setObjectName(u"description")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.description.addWidget(self.label_3)

        self.description_column = QComboBox(Form)
        self.description_column.setObjectName(u"description_column")
        self.description_column.setEnabled(False)

        self.description.addWidget(self.description_column)


        self.horizontalLayout.addLayout(self.description)

        self.debit = QVBoxLayout()
        self.debit.setObjectName(u"debit")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.debit.addWidget(self.label_4)

        self.debit_column = QComboBox(Form)
        self.debit_column.setObjectName(u"debit_column")
        self.debit_column.setEnabled(False)

        self.debit.addWidget(self.debit_column)


        self.horizontalLayout.addLayout(self.debit)

        self.credit = QVBoxLayout()
        self.credit.setObjectName(u"credit")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.credit.addWidget(self.label_5)

        self.credit_column = QComboBox(Form)
        self.credit_column.setObjectName(u"credit_column")
        self.credit_column.setEnabled(False)

        self.credit.addWidget(self.credit_column)


        self.horizontalLayout.addLayout(self.credit)

        self.balance = QVBoxLayout()
        self.balance.setObjectName(u"balance")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.balance.addWidget(self.label_6)

        self.balance_column = QComboBox(Form)
        self.balance_column.setObjectName(u"balance_column")
        self.balance_column.setEnabled(False)

        self.balance.addWidget(self.balance_column)


        self.horizontalLayout.addLayout(self.balance)


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
        self.bank_name.setItemText(0, QCoreApplication.translate("Form", u"BAC San Jos\u00e9", None))
        self.bank_name.setItemText(1, QCoreApplication.translate("Form", u"WINK", None))
        self.bank_name.setItemText(2, QCoreApplication.translate("Form", u"Binance Earn", None))
        self.bank_name.setItemText(3, QCoreApplication.translate("Form", u"THORChain Earn", None))
        self.bank_name.setItemText(4, QCoreApplication.translate("Form", u"Zinli", None))
        self.bank_name.setItemText(5, QCoreApplication.translate("Form", u"Paypal", None))
        self.bank_name.setItemText(6, QCoreApplication.translate("Form", u"Wise", None))

        self.bank_name.setPlaceholderText(QCoreApplication.translate("Form", u"Banco", None))
        self.currency.setItemText(0, QCoreApplication.translate("Form", u"CRC", None))
        self.currency.setItemText(1, QCoreApplication.translate("Form", u"USD", None))

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

