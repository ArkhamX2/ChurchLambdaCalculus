import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from UI.widget import Widget
from UI.ui_calculus import Ui_MainWindow

sys.setrecursionlimit(10022)
#sys.setrecursionlimit(2147483647)

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = Widget()
window.show()
app.exec()