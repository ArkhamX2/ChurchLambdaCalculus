# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculus.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(430, 530)
        MainWindow.setMinimumSize(QSize(430, 530))
        MainWindow.setMaximumSize(QSize(430, 530))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Result = QTextEdit(self.centralwidget)
        self.Result.setObjectName(u"Result")
        self.Result.setEnabled(True)
        self.Result.setGeometry(QRect(10, 10, 411, 151))
        self.Result.setAcceptDrops(True)
        self.Result.setInputMethodHints(Qt.ImhNone)
        self.Result.setReadOnly(True)
        self.Button2 = QPushButton(self.centralwidget)
        self.Button2.setObjectName(u"Button2")
        self.Button2.setGeometry(QRect(290, 470, 131, 31))
        self.Evaluate = QPushButton(self.centralwidget)
        self.Evaluate.setObjectName(u"Evaluate")
        self.Evaluate.setGeometry(QRect(10, 470, 131, 31))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 280, 411, 181))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Two = QPushButton(self.gridLayoutWidget)
        self.Two.setObjectName(u"Two")

        self.gridLayout.addWidget(self.Two, 3, 1, 1, 1)

        self.Nine = QPushButton(self.gridLayoutWidget)
        self.Nine.setObjectName(u"Nine")

        self.gridLayout.addWidget(self.Nine, 1, 2, 1, 1)

        self.Zer0 = QPushButton(self.gridLayoutWidget)
        self.Zer0.setObjectName(u"Zer0")

        self.gridLayout.addWidget(self.Zer0, 4, 1, 1, 1)

        self.Four = QPushButton(self.gridLayoutWidget)
        self.Four.setObjectName(u"Four")

        self.gridLayout.addWidget(self.Four, 2, 0, 1, 1)

        self.Mult = QPushButton(self.gridLayoutWidget)
        self.Mult.setObjectName(u"Mult")

        self.gridLayout.addWidget(self.Mult, 1, 3, 1, 1)

        self.Minus = QPushButton(self.gridLayoutWidget)
        self.Minus.setObjectName(u"Minus")

        self.gridLayout.addWidget(self.Minus, 3, 3, 1, 1)

        self.Plus = QPushButton(self.gridLayoutWidget)
        self.Plus.setObjectName(u"Plus")

        self.gridLayout.addWidget(self.Plus, 2, 3, 1, 1)

        self.Eight = QPushButton(self.gridLayoutWidget)
        self.Eight.setObjectName(u"Eight")

        self.gridLayout.addWidget(self.Eight, 1, 1, 1, 1)

        self.Six = QPushButton(self.gridLayoutWidget)
        self.Six.setObjectName(u"Six")

        self.gridLayout.addWidget(self.Six, 2, 2, 1, 1)

        self.Five = QPushButton(self.gridLayoutWidget)
        self.Five.setObjectName(u"Five")

        self.gridLayout.addWidget(self.Five, 2, 1, 1, 1)

        self.One = QPushButton(self.gridLayoutWidget)
        self.One.setObjectName(u"One")

        self.gridLayout.addWidget(self.One, 3, 0, 1, 1)

        self.Three = QPushButton(self.gridLayoutWidget)
        self.Three.setObjectName(u"Three")

        self.gridLayout.addWidget(self.Three, 3, 2, 1, 1)

        self.Equal = QPushButton(self.gridLayoutWidget)
        self.Equal.setObjectName(u"Equal")

        self.gridLayout.addWidget(self.Equal, 4, 3, 1, 1)

        self.Seven = QPushButton(self.gridLayoutWidget)
        self.Seven.setObjectName(u"Seven")

        self.gridLayout.addWidget(self.Seven, 1, 0, 1, 1)

        self.ClearButton = QPushButton(self.gridLayoutWidget)
        self.ClearButton.setObjectName(u"ClearButton")

        self.gridLayout.addWidget(self.ClearButton, 0, 0, 1, 1)

        self.DeleteButton = QPushButton(self.gridLayoutWidget)
        self.DeleteButton.setObjectName(u"DeleteButton")

        self.gridLayout.addWidget(self.DeleteButton, 0, 1, 1, 1)

        self.Powto = QPushButton(self.gridLayoutWidget)
        self.Powto.setObjectName(u"Powto")

        self.gridLayout.addWidget(self.Powto, 0, 2, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 170, 411, 104))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PlusLog = QPushButton(self.gridLayoutWidget_2)
        self.PlusLog.setObjectName(u"PlusLog")

        self.gridLayout_2.addWidget(self.PlusLog, 1, 0, 1, 1)

        self.EqLog = QPushButton(self.gridLayoutWidget_2)
        self.EqLog.setObjectName(u"EqLog")

        self.gridLayout_2.addWidget(self.EqLog, 2, 1, 1, 1)

        self.DivLog = QPushButton(self.gridLayoutWidget_2)
        self.DivLog.setObjectName(u"DivLog")

        self.gridLayout_2.addWidget(self.DivLog, 2, 0, 1, 1)

        self.MinusLog = QPushButton(self.gridLayoutWidget_2)
        self.MinusLog.setObjectName(u"MinusLog")

        self.gridLayout_2.addWidget(self.MinusLog, 1, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_2.addWidget(self.pushButton_11, 2, 2, 1, 1)

        self.MultLog = QPushButton(self.gridLayoutWidget_2)
        self.MultLog.setObjectName(u"MultLog")

        self.gridLayout_2.addWidget(self.MultLog, 1, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setMargin(5)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)

        MainWindow.centralWidget = self.centralwidget
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.statusBar = self.statusbar

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.Button2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043d\u043e\u043f\u043a\u0430 2", None))
        self.Evaluate.setText(QCoreApplication.translate("MainWindow", u"Evaluate", None))
        self.Two.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Nine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Zer0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Four.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Mult.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.Minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Eight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Six.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.Five.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.One.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Three.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.Seven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.ClearButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043f\u043e\u043b\u0435", None))
        self.DeleteButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0438\u043c\u0432\u043e\u043b", None))
        self.Powto.setText(QCoreApplication.translate("MainWindow", u"^x", None))
        self.PlusLog.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.EqLog.setText(QCoreApplication.translate("MainWindow", u"==", None))
        self.DivLog.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.MinusLog.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0430\u0441\u043a\u0430", None))
        self.MultLog.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041bo\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
    # retranslateUi

