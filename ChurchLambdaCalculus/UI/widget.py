from typing import Optional
from PySide6.QtCore import QtMsgType
from PySide6.QtWidgets import QWidget
from library.ArithmeticParser import Parse
from UI.ui_calculus_widget import Ui_MainWindow

class Widget(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Lambda Calculus")
        
        self.Plus.clicked.connect(self.plus)
        self.Minus.clicked.connect(self.minus)
        self.Mult.clicked.connect(self.multiply)
        self.PlusLog.clicked.connect(self.OR)
        self.MultLog.clicked.connect(self.AND)
        self.Equal.clicked.connect(self.EQUALITY)
        
        #TODO: Добавить кнопки для XOR, NOT, TRUE, FALSE
        # self.XORbutton.clicked.connect(self.XOR)
        # self.NOTbutton.clicked.connect(self.NOT)
        # self.TRUEbutton.clicked.connect(self.TRUE)
        # self.FALSEbutton.clicked.connect(self.FALSE)
        
    def plus(self):
        self.Result.setText(self.Result.toPlainText + " +")
    def minus(self):
        self.Result.setText(self.Result.toPlainText + " -")
    def multiply(self):
        self.Result.setText(self.Result.toPlainText + " *")
    def OR(self):
        self.Result.setText(self.Result.toPlainText + " V")
    def AND(self):
        self.Result.setText(self.Result.toPlainText + " ^")
    def XOR(self):
        self.Result.setText(self.Result.toPlainText + " XOR")
    def NOT(self):
        self.Result.setText(self.Result.toPlainText + " !")
    def EQUALITY(self):
        self.Result.setText(self.Result.toPlainText + " ==")
    def TRUE(self):
        self.Result.setText(self.Result.toPlainText + " True")
    def FALSE(self):
        self.Result.setText(self.Result.toPlainText + " False")

    def Evaluate(self):
        self.Result.setText(Parse(self.Result.toPlainText()))