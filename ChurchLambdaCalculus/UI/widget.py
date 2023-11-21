import sys

import PySide6.QtGui

# setting path
sys.path.append('../library/')

from typing import Optional
from PySide6 import QtCore
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QEvent
from library.arithmetic_parser import ArithmeticParse
from library.logical_parser import LogicalParse
from library.arithmetic_evaluator import EvaluateArithmeticEquation
from library.logical_evaluator import EvaluateLogicalEquation
from library.function import *
from UI.ui_calculus import Ui_MainWindow

class Widget(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Lambda Calculus")
        self.InputText=[]
        self.logical=False
        self.UiEnableSwitch()
        self.Plus.clicked.connect(self.plus)
        self.Minus.clicked.connect(self.minus)
        self.Mult.clicked.connect(self.multiply)
        self.Div.clicked.connect(self.divide)
        self.PowTo.clicked.connect(self.POWER)
        self.PlusLog.clicked.connect(self.OR)
        self.MultLog.clicked.connect(self.AND)
        self.NotLog.clicked.connect(self.NOT)
        self.XorLog.clicked.connect(self.XOR)
        self.EqLog.clicked.connect(self.EQUALITY)
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
        self.Evaluate.clicked.connect(self.EVALUATE)
        self.LogcalcButton.clicked.connect(self.LOGCALC)
        self.ParenLeftButton.clicked.connect(self.PARENLEFT)
        self.parenRightButton.clicked.connect(self.PARENRIGHT)

    def UiEnableSwitch(self):
        if self.logical==False:
            self.Plus.setEnabled(True)
            self.Minus.setEnabled(True)
            self.Mult.setEnabled(True)
            self.Div.setEnabled(True)
            self.PowTo.setEnabled(True)
            self.One.setEnabled(True)
            self.Two.setEnabled(True)
            self.Three.setEnabled(True)
            self.Four.setEnabled(True)
            self.Five.setEnabled(True)
            self.Six.setEnabled(True)
            self.Seven.setEnabled(True)
            self.Eight.setEnabled(True)
            self.Nine.setEnabled(True)
            self.Zer0.setEnabled(True)

            self.PlusLog.setEnabled(False)
            self.MultLog.setEnabled(False)
            self.NotLog.setEnabled(False)
            self.XorLog.setEnabled(False)
            self.EqLog.setEnabled(False)
            self.TrueButton.setEnabled(False)
            self.FalseButton.setEnabled(False)
        else:
            self.Plus.setEnabled(False)
            self.Minus.setEnabled(False)
            self.Mult.setEnabled(False)
            self.Div.setEnabled(False)
            self.PowTo.setEnabled(False)
            self.One.setEnabled(False)
            self.Two.setEnabled(False)
            self.Three.setEnabled(False)
            self.Four.setEnabled(False)
            self.Five.setEnabled(False)
            self.Six.setEnabled(False)
            self.Seven.setEnabled(False)
            self.Eight.setEnabled(False)
            self.Nine.setEnabled(False)
            self.Zer0.setEnabled(False)

            self.PlusLog.setEnabled(True)
            self.MultLog.setEnabled(True)
            self.NotLog.setEnabled(True)
            self.XorLog.setEnabled(True)
            self.EqLog.setEnabled(True)
            self.TrueButton.setEnabled(True)
            self.FalseButton.setEnabled(True)

    def LOGCALC(self):
        if self.logical==True:
            self.logical=False
            self.CLEARALL()
            self.Result.setText("")
            self.UiEnableSwitch()            
        else:
            self.logical=True
            self.CLEARALL()
            self.Result.setText("")
            self.UiEnableSwitch()            

    def IsNumber(self, item):
        numbers="0123456789"
        return numbers.find(item)!=-1

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
            if self.IsNumber(self.InputText[len(self.InputText)-1])==False:
                if self.InputText[len(self.InputText)-1]=="(" or self.InputText[len(self.InputText)-1]==")":
                    pass
                else:
                    self.DELETELAST()
            self.InputText.append("+")
            self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
                
    def minus(self):
        if len(self.InputText)==0:
            self.InputText.append("0")
            self.InputText.append("-")
            self.Input.setText(self.Input.toPlainText() + "0" + self.InputText[len(self.InputText)-1])
        else:
            if self.IsNumber(self.InputText[len(self.InputText)-1])==False and (self.InputText[len(self.InputText)-1]!="(" or self.InputText[len(self.InputText)-1]!=")"):
                if self.InputText[len(self.InputText)-1]=="(" or self.InputText[len(self.InputText)-1]==")":
                    pass
                else:
                    self.DELETELAST()
            self.InputText.append("-")
            self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def multiply(self):
        if len(self.InputText)==0:
            self.InputText.append("0")
            self.InputText.append("*")
            self.Input.setText(self.Input.toPlainText() + "0" + self.InputText[len(self.InputText)-1])
        else:
            if self.IsNumber(self.InputText[len(self.InputText)-1])==False and (self.InputText[len(self.InputText)-1]!="(" or self.InputText[len(self.InputText)-1]!=")"):
                if self.InputText[len(self.InputText)-1]=="(" or self.InputText[len(self.InputText)-1]==")":
                    pass
                else:
                    self.DELETELAST()
            self.InputText.append("*")
            self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def divide(self):
        if len(self.InputText)==0:
            self.InputText.append("0")
            self.InputText.append("/")
            self.Input.setText(self.Input.toPlainText() + "0" + self.InputText[len(self.InputText)-1])
        else:
            if self.IsNumber(self.InputText[len(self.InputText)-1])==False and (self.InputText[len(self.InputText)-2]!="(" or self.InputText[len(self.InputText)-2]!=")"):
                if self.InputText[len(self.InputText)-1]=="(" or self.InputText[len(self.InputText)-1]==")":
                    pass
                else:
                    self.DELETELAST()
            self.InputText.append("/")
            self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def POWER(self):
        if len(self.InputText)==0:
            self.InputText.append("0")
            self.InputText.append("^")
            self.Input.setText(self.Input.toPlainText() + "0" + self.InputText[len(self.InputText)-1])
        else:
            if self.IsNumber(self.InputText[len(self.InputText)-1])==False and (self.InputText[len(self.InputText)-2]!="(" or self.InputText[len(self.InputText)-2]!=")"):
                if self.InputText[len(self.InputText)-1]=="(" or self.InputText[len(self.InputText)-1]==")":
                    pass
                else:
                    self.DELETELAST()
            self.InputText.append("^")
            self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def OR(self):
        self.InputText.append("V")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def AND(self):
        self.InputText.append("^")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def XOR(self):
        self.InputText.append("⊕")
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
    def PARENLEFT(self):
        self.InputText.append("(")
        self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
    def PARENRIGHT(self):
        try:
            if self.InputText[len(self.InputText)-1]=="(":
                if self.logical == False:
                    self.InputText.append("0")
                    self.InputText.append(")")
                    self.Input.setText(self.Input.toPlainText() +"0"+ self.InputText[len(self.InputText)-1])
                else:
                    self.InputText.append("False")
                    self.InputText.append(")")
                    self.Input.setText(self.Input.toPlainText() +"False"+ self.InputText[len(self.InputText)-1])
            else:
                self.InputText.append(")")
                self.Input.setText(self.Input.toPlainText() + self.InputText[len(self.InputText)-1])
        except:
            if self.logical == False:
                self.InputText.append("(")
                self.InputText.append("0")
                self.InputText.append(")")
                self.Input.setText(self.Input.toPlainText() +"("+"0"+ self.InputText[len(self.InputText)-1])
            else:
                self.InputText.append("(")
                self.InputText.append("False")
                self.InputText.append(")")
                self.Input.setText(self.Input.toPlainText() +"("+"False"+ self.InputText[len(self.InputText)-1])
    def CLEARALL(self):
        self.InputText.clear()
        self.Input.setText("")
    def DELETELAST(self):
        try:        
            self.Input.setText(self.Input.toPlainText()[:len(self.Input.toPlainText())-len(self.InputText.pop())])
        except:
            pass

    def NegativeNumbers(self):
        try:
            for i in range (len(self.InputText)-1):
                if self.InputText[i]=="-":
                    if self.InputText[i-1] == "(" and self.InputText[i+2] == ")":
                       self.InputText[i]=self.InputText[i]+self.InputText[i+1]
                       self.InputText.pop(i+1)
        except:
            pass

    def CheckLastNotOperation(self, input):
        if self.logical == False:
            arithmeticoperators="/*+-^"
            if (arithmeticoperators.find(self.InputText[len(self.InputText)-1])==-1):
                return input
            else:
                self.Result.setText("Не закрытая операция")
                return None
        else:
            logicaloperators="!^V⊕≡"
            if (logicaloperators.find(self.InputText[len(self.InputText)-1])==-1):
                return input
            else:
                self.Result.setText("Не закрытая операция")
                return None

    def CheckOpenParen(self, input):
        tmp=input
        parenleft="("
        parenleftcount=0
        parenright=")"
        parenrightcount=0
        while tmp.find(parenleft) != -1:
            parenleftcount+=1
            tmp=tmp.replace(parenleft, "", 1)            
        while tmp.find(parenright) != -1:
            parenrightcount+=1
            tmp=tmp.replace(parenright, "", 1)
        if parenleftcount!=parenrightcount:
            self.Result.setText("Скобки не закрыты")
            return None
        else:
            for i in range(len(self.InputText)):
                if self.InputText[i]=="(":
                    try:
                        if self.InputText[i+1] != None:
                            pass
                    except:
                        self.Result.setText("Скобки не закрыты")
                        return None                    
            return input

    def CheckDivideZero(self, input):
        tmp=input
        id=0
        div="/"
        end=0
        c=1
        while tmp.find(div) != -1:
            id=(tmp.find(div))
            try:            
                if input[id+3]=="(":
                    depth=0
                    for i in range(id+3,len(input)):
                        if input[i]=="(":
                            depth+=1
                        if input[i]==")":
                            depth-=1
                            if depth==0:
                                end=i
                                break
                    substring=input[id+2:end+1]
                    substring_eval=str(eval(EvaluateArithmeticEquation(ArithmeticParse(substring))))
                    if substring_eval == "0":
                        self.Result.setText("Деление на 0")
                        return None
                    else:
                        input = input[:id+2] + substring_eval + input[end+1:]
                        tmp=input
                        tmp=tmp.replace(div, " ", c)                
                else:
                    if input[id+2]=="0":
                        self.Result.setText("Деление на 0")
                        return None
                    else:
                        tmp=tmp.replace(div, " ", c)
            except:
                if input[id+2]=="0":
                    self.Result.setText("Деление на 0")
                    return None
                else:
                    tmp=tmp.replace(div, " ", c)
            c+=1
        return input

    def EVALUATE(self):
        if len(self.InputText)==0:
            self.Result.setText("")
        else:
            if self.logical==False:
                self.NegativeNumbers()
                input=self.CheckLastNotOperation(self.MakeString())
                if input!= None:
                    input=self.CheckOpenParen(input)
                    if input != None:
                        input=self.CheckDivideZero(input)
                        if input != None:
                            self.Result.setText(str(eval(EvaluateArithmeticEquation(ArithmeticParse(input)))))
                pass
            else:
                pass
                input=self.CheckLastNotOperation(self.MakeString())
                if input!= None:
                    input=self.CheckOpenParen(input)
                    if input != None:
                        self.Result.setText(str(eval(EvaluateLogicalEquation(LogicalParse(input)))))

    def keyPressEvent(self, event):
        if (event.type() == QtCore.QEvent.KeyPress):
                if self.logical==False:
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
                        case QtCore.Qt.Key_AsciiCircum:
                            self.POWER()
                else:
                    match event.key():
                        case QtCore.Qt.Key_0:
                            self.FALSE()
                        case QtCore.Qt.Key_1:
                            self.TRUE()
                        case QtCore.Qt.Key_Plus:
                            self.OR()
                        case QtCore.Qt.Key_Minus:
                            self.NOT()
                        case QtCore.Qt.Key_Asterisk:
                            self.AND()
                match event.key():
                    case QtCore.Qt.Key_M:
                        self.LogcalcButton.click()
                    case QtCore.Qt.Key_ParenLeft:
                        self.PARENLEFT()
                    case QtCore.Qt.Key_ParenRight:
                        self.PARENRIGHT()
                    case QtCore.Qt.Key_Backspace:
                        self.DELETELAST()
                    case QtCore.Qt.Key_Delete:
                        self.CLEARALL()
                    case QtCore.Qt.Key_Enter:
                        self.EVALUATE()
                    case QtCore.Qt.Key_Return:
                        self.EVALUATE()