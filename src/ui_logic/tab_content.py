#!/usr/bin/env python3
from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import QObject
from src.ui.tab_content import Ui_Form
from typing import Callable
from os.path import expanduser


class TabContent(QWidget):
    def __init__(self, index: int, tabRenameFunc: Callable[[int, str], None]):
        super(TabContent, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.index = index
        self.change_tab_name = tabRenameFunc

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

        self.ui.bank_name.currentIndexChanged.connect(self.rename_tab)
        self.ui.currency.currentIndexChanged.connect(self.rename_tab)

        self.ui.load_rsv.clicked.connect(self.read_rsv)

    def get_new_name(self):
        return "%s %s" % (
            self.ui.bank_name.currentText(),
            self.ui.currency.currentText(),
        )

    def rename_tab(self):
        self.change_tab_name(self.index, self.get_new_name())

    def tr(self, text):
        return QObject.tr(self, text)

    def read_rsv(self):
        path_to_file, _ = QFileDialog.getOpenFileName(
            self,
            self.tr("Load data"),
            self.tr(expanduser("~")),
            self.tr("Stenway Rows of String Values (*.rsv)"),
        )
        print(path_to_file)
