#!/usr/bin/env python3
from os.path import expanduser
from typing import Callable, List
import decimal

from PySide2.QtCore import QObject
from PySide2.QtWidgets import QFileDialog, QWidget, QTableWidgetItem
from src.ui.tab_content import Ui_Form
from src import rsv
import re


class TabContent(QWidget):
    data: List[List[str | None]]
    clean_description_data: List[str | None]
    calculated_balance_data: List[str | None]
    index_columns: List[str]

    def __init__(self, index: int, tabRenameFunc: Callable[[int, str], None]):
        super(TabContent, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.index = index
        self.change_tab_name = tabRenameFunc

        self.clean_description_data = []
        self.calculated_balance_data = []

        self._wd_columns = [
            self.ui.balance_column,
            self.ui.credit_column,
            self.ui.debit_column,
            self.ui.description_column,
            self.ui.date_column,
            self.ui.reference_column,
            self.ui.bank_name,
            self.ui.currency,
        ]
        self._statement_columns = [
            self.ui.balance_column,
            self.ui.credit_column,
            self.ui.debit_column,
            self.ui.description_column,
            self.ui.date_column,
            self.ui.reference_column,
        ]

        self.ui.bank_name.currentIndexChanged.connect(self.rename_tab)
        self.ui.currency.currentIndexChanged.connect(self.rename_tab)

        self.ui.load_rsv.clicked.connect(self.read_rsv)

        self.ui.description_column.currentIndexChanged.connect(
            self.clean_description_data_on_index_changed
        )
        self.ui.balance_column.currentIndexChanged.connect(
            self.balance_on_index_changed
        )
        self.ui.initial_balance.valueChanged.connect(self.balance_calculate_each_field)

    def get_new_name(self):
        current_currency = self.ui.currency.currentText()
        # cambia el prefijo para initial_balance
        self.ui.initial_balance.setPrefix(current_currency+" ")
        return "%s %s" % (
            self.ui.bank_name.currentText(),
            current_currency,
        )

    def rename_tab(self):
        self.change_tab_name(self.index, self.get_new_name())

    def tr(self, text):
        return QObject.tr(self, text)

    def clean_description_data_on_index_changed(self, index):
        if index == 0:
            return

        index = index - 1  # tomamos en cuenta la etiqueta vacia
        self.clean_description_data.clear()

        # restauramos los datos en la tabla
        self.add_data_to_table(self.data, True)

        for row in range(0, len(self.data)):
            description = re.sub(r"\s+", " ", self.data[row][index].strip())
            self.clean_description_data.append(description)

            self.ui.statements.setItem(row, index, QTableWidgetItem(description))

    def add_data_to_table(self, data: List[List[str | None]], restore: bool = False):
        for row in range(0, len(self.data)):
            if not restore:
                self.ui.statements.insertRow(row)
            for column in range(0, len(data[row])):
                self.ui.statements.setItem(
                    row, column, QTableWidgetItem(data[row][column])
                )

    def read_rsv(self):
        path_to_file, _ = QFileDialog.getOpenFileName(
            self,
            self.tr("Load data"),
            self.tr(expanduser("~")),
            self.tr("Stenway's Rows of String Values (*.rsv)"),
        )
        self.data = rsv.load_rsv(path_to_file)

        if len(self.data) == 0:
            return

        self.rename_tab()

        # limpia la tabla
        self.ui.statements.setRowCount(0)

        self.add_data_to_table(self.data, False)

        # habilita todas las cajas de selección
        self.toggle_comboboxes(True)

        self.index_columns = [""]
        for column in range(0, 6):
            data = self.tr("%d: ?" % column)

            if column <= len(self.data[0]):
                data = self.tr("%d: %s" % (column + 1, self.data[0][column]))

            self.index_columns.append(data)

        for column in self._statement_columns:
            column.clear()
            column.addItems(self.index_columns)

    def toggle_comboboxes(self, state: bool):
        for column in self._wd_columns:
            column.setEnabled(state)

    def balance_calculate_each_field(self, initial: float):
        index = self.ui.balance_column.currentIndex() - 1
        credit_index = self.ui.credit_column.currentIndex() - 1
        debit_index = self.ui.debit_column.currentIndex() - 1

        if index < 0 or credit_index < 0 or debit_index < 0:
            return

        self.calculated_balance_data.clear()
        balance = decimal.Decimal(initial)
        for row in range(len(self.data)):
            credit = decimal.Decimal(self.data[row][credit_index])
            debit = decimal.Decimal(self.data[row][debit_index])

            balance = balance + credit - debit
            amount = f"{balance:.2f}"

            self.calculated_balance_data.append(amount)

            self.ui.statements.setItem(row, index, QTableWidgetItem(self.tr(amount)))

    def balance_on_index_changed(self, index):
        # necesitamos debit y credit establecidos
        if len(self.data) == 0:
            return

        index = index - 1 # index de Balance

        credit_index = self.ui.credit_column.currentIndex() - 1
        debit_index = self.ui.debit_column.currentIndex() - 1

        if index < 0 or credit_index < 0 or debit_index < 0:
            return

        if self.data[0][index] is None or self.data[0][index] == 0:
            self.enable_initial_balance(False)
            self.balance_calculate_each_field(self.ui.initial_balance.value())
            return

        credit = decimal.Decimal(self.data[0][credit_index])
        debit = decimal.Decimal(self.data[0][debit_index])
        balance = decimal.Decimal(self.data[0][index])

        prev_balance = balance - credit + debit

        # establece el balance anterior
        self.enable_initial_balance()
        self.ui.initial_balance.setValue(float(prev_balance))

    def enable_initial_balance(self, readOnly=True):
        self.ui.initial_balance.setEnabled(True)
        self.ui.initial_balance.setReadOnly(readOnly)
