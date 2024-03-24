#!/usr/bin/env python3

import sys
from PySide2.QtWidgets import QApplication
from src.ui_logic.window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
