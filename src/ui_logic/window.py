#!/usr/bin/env python3
from PySide2.QtWidgets import QMainWindow
from src.ui.window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
