import sys

# setting path
sys.path.append('../library/')

from typing import Optional
from PySide6.QtCore import QtMsgType
from PySide6.QtWidgets import QWidget
from library.arithmetic_parser import Parse
from UI.ui_calculus import Ui_MainWindow

class Widget(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Lambda Calculus")
        
        self.Plus.clicked.connect(self.plus)
        self.Minus.clicked.connect(self.minus)
        self.Mult.clicked.connect(self.multiply)
        self.Div.clicked.connect(self.divide)
        self.PlusLog.clicked.connect(self.OR)
        self.MultLog.clicked.connect(self.AND)
        self.NotLog.clicked.connect(self.NOT)
        self.XorLog.clicked.connect(self.XOR)
        self.TrueButton.clicked.connect(self.TRUE)
        self.FalseButton.clicked.connect(self.FALSE)
        self.One.clicked.connect(self.ONE)
        self.Two.clicked.connect(self.TWO)
        self.Three.clicked.connect(self.THREE)
        self.Four.clicked.connect(self.FOUR)
        self.Five.clicked.connect(self.FIVE)
        self.Six.clicked.connect(self.SIX)
        self.Seven.clicked.connect(self.SEVEN)
        self.Eight.clicked.connect(self.EIGHT)
        self.Nine.clicked.connect(self.NINE)
        self.Zer0.clicked.connect(self.ZERO)
        self.ClearButton.clicked.connect(self.CLEARALL)
        self.DeleteButton.clicked.connect(self.DELETELAST)
        self.EqLog.clicked.connect(self.EQUALITY)

    def plus(self):
        self.Input.setText(self.Input.toPlainText() + " +")
    def minus(self):
        self.Input.setText(self.Input.toPlainText() + " -")
    def multiply(self):
        self.Input.setText(self.Input.toPlainText() + " *")
    def divide(self):
        self.Input.setText(self.Input.toPlainText() + " /")
    def OR(self):
        self.Input.setText(self.Input.toPlainText() + " V")
    def AND(self):
        self.Input.setText(self.Input.toPlainText() + " ^")
    def XOR(self):
        self.Input.setText(self.Input.toPlainText() + " XOR")
    def NOT(self):
        self.Input.setText(self.Input.toPlainText() + " !")
    def EQUALITY(self):
        self.Input.setText(self.Input.toPlainText() + " ≡")
    def TRUE(self):
        self.Input.setText(self.Input.toPlainText() + " True")
    def FALSE(self):
        self.Input.setText(self.Input.toPlainText() + " False")
    def ONE(self):
        self.Input.setText(self.Input.toPlainText() + "1")
    def TWO(self):
        self.Input.setText(self.Input.toPlainText() + "2")
    def THREE(self):
        self.Input.setText(self.Input.toPlainText() + "3")
    def FOUR(self):
        self.Input.setText(self.Input.toPlainText() + "4")
    def FIVE(self):
        self.Input.setText(self.Input.toPlainText() + "5")
    def SIX(self):
        self.Input.setText(self.Input.toPlainText() + "6")
    def SEVEN(self):
        self.Input.setText(self.Input.toPlainText() + "7")
    def EIGHT(self):
        self.Input.setText(self.Input.toPlainText() + "8")
    def NINE(self):
        self.Input.setText(self.Input.toPlainText() + "9")
    def ZERO(self):
        self.Input.setText(self.Input.toPlainText() + "0")
    def CLEARALL(self):
        self.Input.setText("")
    def DELETELAST(self):
        self.Input.setText(self.Input.toPlainText()[:len(self.Input.toPlainText())-1])


    def Evaluate(self):
        self.Result.setText(Parse(self.Result.toPlainText()))