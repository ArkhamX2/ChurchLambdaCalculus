import sys

import PySide6.QtGui

# setting path
sys.path.append('../library/')

from typing import Optional
from PySide6 import QtCore
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QEvent
from library.arithmetic_parser import Parse
from library.arithmetic_evaluator import EvaluateEquation
from library.function import *
from UI.ui_calculus import Ui_MainWindow

class Widget(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Lambda Calculus")
        self.InputText=[]
        
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
        self.Evaluate.clicked.connect(self.EVALUATE)

    def IsNumber(self, item):
        match item:
            case "0":
                return True
            case "1":
                return True
            case "2":
                return True
            case "3":
                return True
            case "4":
                return True
            case "5":
                return True
            case "6":
                return True
            case "7":
                return True
            case "8":
                return True
            case "9":
                return True
            case _:
                return False

    def MakeString(self):
        answ=""
        for item in self.InputText:
            if self.IsNumber(item)==True:
                answ+=item
            else:
                answ+=" "
                answ+=item
                answ+=" "
        return answ

    def plus(self):
        if len(self.InputText)==0:
            self.InputText.append("0")
            self.InputText.append("+")
            self.Input.setText(self.Input.toPlainText() + "0" + self.InputText[len(self.InputText)-1])
        else:
            self.InputText.append("+")
            self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def minus(self):
        if len(self.InputText)==0:
            self.InputText.append("0")
            self.InputText.append("-")
            self.Input.setText(self.Input.toPlainText() + "0" + self.InputText[len(self.InputText)-1])
        else:
            self.InputText.append("-")
            self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def multiply(self):
        if len(self.InputText)==0:
            self.InputText.append("0")
            self.InputText.append("*")
            self.Input.setText(self.Input.toPlainText() + "0" + self.InputText[len(self.InputText)-1])
        else:
            self.InputText.append("*")
            self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def divide(self):
        if len(self.InputText)==0:
            self.InputText.append("0")
            self.InputText.append("/")
            self.Input.setText(self.Input.toPlainText() + "0" + self.InputText[len(self.InputText)-1])
        else:
            self.InputText.append("/")
            self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def OR(self):
        self.InputText.append("V")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def AND(self):
        self.InputText.append("^")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def XOR(self):
        self.InputText.append("XOR")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def NOT(self):
        self.InputText.append("!")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def EQUALITY(self):
        self.InputText.append("≡")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def TRUE(self):
        self.InputText.append("True")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def FALSE(self):
        self.InputText.append("False")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def ONE(self):
        self.InputText.append("1")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def TWO(self):
        self.InputText.append("2")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def THREE(self):
        self.InputText.append("3")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def FOUR(self):
        self.InputText.append("4")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def FIVE(self):
        self.InputText.append("5")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def SIX(self):
        self.InputText.append("6")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def SEVEN(self):
        self.InputText.append("7")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def EIGHT(self):
        self.InputText.append("8")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def NINE(self):
        self.InputText.append("9")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def ZERO(self):
        self.InputText.append("0")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def CLEARALL(self):
        self.InputText.clear()
        self.Input.setText("")
    def DELETELAST(self):
        try:        
            self.Input.setText(self.Input.toPlainText()[:len(self.Input.toPlainText())-len(self.InputText.pop())])
        except:
            pass

    def EVALUATE(self):
        if len(self.InputText)==0:
            self.Result.setText("")
        else:
            self.Result.setText(str(eval(EvaluateEquation(Parse(self.MakeString())))))

    def keyPressEvent(self, event):
        if (event.type() == QtCore.QEvent.KeyPress):
                match event.key():
                    case QtCore.Qt.Key_0:
                        self.ZERO()
                    case QtCore.Qt.Key_1:
                        self.ONE()
                    case QtCore.Qt.Key_2:
                        self.TWO()
                    case QtCore.Qt.Key_3:
                        self.THREE()
                    case QtCore.Qt.Key_4:
                        self.FOUR()
                    case QtCore.Qt.Key_5:
                        self.FIVE()
                    case QtCore.Qt.Key_6:
                        self.SIX()
                    case QtCore.Qt.Key_7:
                        self.SEVEN()
                    case QtCore.Qt.Key_8:
                        self.EIGHT()
                    case QtCore.Qt.Key_9:
                        self.NINE()
                    case QtCore.Qt.Key_Plus:
                        self.plus()
                    case QtCore.Qt.Key_Minus:
                        self.minus()
                    case QtCore.Qt.Key_Asterisk:
                        self.multiply()
                    case QtCore.Qt.Key_Slash:
                        self.divide()
                    case QtCore.Qt.Key_Backspace:
                        self.DELETELAST()
                    case QtCore.Qt.Key_Delete:
                        self.CLEARALL()
                    case QtCore.Qt.Key_Enter:
                        self.EVALUATE()
                    case QtCore.Qt.Key_Return:
                        self.EVALUATE()