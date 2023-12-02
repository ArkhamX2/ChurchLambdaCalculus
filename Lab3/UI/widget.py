import sys
from typing import Optional
import PySide6.QtCore
sys.path.append('../library/')

from PySide6.QtWidgets import QWidget,QMessageBox,QTableWidgetItem
from library.calc import *
from UI.inputHandler import *
from UI.outputHandler import *
from UI.ui_function_calc import Ui_MainWindow

class Widget(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Function calculus")

        self.Calculate.clicked.connect(self.calculate)
    
    def calculate(self):
        parameters = [self.SpinBoxA.value(),
                      self.SpinBoxB.value(),
                      self.SpinBoxH.value(),
                      self.SpinBoxK.value(),
                      self.SpinBoxM.value(),]
        check = CheckParameters(parameters)
        if check == "":
            self.HandleOutputWidget(parameters,LinearList(parameters))
        else:
            self.msgbox = QMessageBox(self)
            self.msgbox.setWindowTitle("Error")
            self.msgbox.setText(check)
            self.msgbox.show()
    
        
    def HandleOutputWidget(self,inputParameters:list[float],functionResult:list[float]):

        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderItem(0,QTableWidgetItem("N"))
        self.tableWidget.setHorizontalHeaderItem(1,QTableWidgetItem("X"))
        self.tableWidget.setHorizontalHeaderItem(2,QTableWidgetItem("f(x)"))

        leftBorder = inputParameters[0]
        rightBorder = inputParameters[1]
        step = inputParameters[2]
        counter = 1
        for i in np.arange(leftBorder,rightBorder+step,step):
            self.add_row(counter,i,functionResult[counter-1])
            counter += 1
            
    
    def add_row(self,counter,xValue,functionResult):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)      
        self.tableWidget.setRowCount(rowPosition+1)          
        self.tableWidget.setItem(rowPosition,0,QTableWidgetItem(str(counter)))
        self.tableWidget.setItem(rowPosition,1,QTableWidgetItem(str(xValue)))
        self.tableWidget.setItem(rowPosition,2,QTableWidgetItem(str(functionResult)))