from typing import Optional
from PySide6 import QtCore, QtWidgets
import PySide6.QtCore
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("calculus.ui",None)
        self.ui.setWindowTitle("Lambda Calculus")
        self.ui.Button1.clicked.connect(self.do_something)
    def show(self):
        self.ui.show()
    def do_something(self):
        print(self.ui.Result.toPlainText(), " is a")
