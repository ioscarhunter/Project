import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import*
from test2 import menu

class mymainwindow(QMainWindow):
    def __init__(self,x):
        QMainWindow.__init__(self)
        loader = QUiLoader()
        x[2] = 9
        form = loader.load("./test.ui", self)
        self.setCentralWidget(form)
        
        self.p1 = form.findChild(QPushButton, "p1")
        p2 = form.findChild(QPushButton, "p2")
        p2.clicked.connect(self.printit)
        self.m = menu(x)
    def printit(self):
        self.m.show()
        self.close()

def main():
    app = QApplication(sys.argv)
    x = [1,2,3]
    mywindow = mymainwindow(x)
    mywindow.show()
    print(x)
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())



    
