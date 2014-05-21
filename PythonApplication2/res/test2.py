import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class menu(QMainWindow):
    def __init__(self,x):
        QMainWindow.__init__(self)
        loader = QUiLoader()
        form = loader.load("./test.ui", self)
        self.setCentralWidget(form)
        self.p1 = form.findChild(QPushButton, "p1")
        p2 = form.findChild(QPushButton, "p2")
        p2.clicked.connect(self.printit)
        self.x = x
    def printit(self):
        
        print(self.x)
