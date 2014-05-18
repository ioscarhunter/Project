
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class mymainwindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loader = QUiLoader()

        form = loader.load("./test.ui", self)
        self.setCentralWidget(form)
        
        self.p1 = form.findChild(QPushButton, "p1")
        p2 = form.findChild(QPushButton, "p2")
        p2.clicked.connect(self.printit)
    def printit(self):
        if(self.p1.isEnabled()):
            self.p1.setEnabled(False)
        else:
            self.p1.setEnabled(True)
        print("d")

def main():
    app = QApplication(sys.argv)

    mywindow = mymainwindow()
    mywindow.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())



    
