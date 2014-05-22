import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import G_Main

class ShowOrder(QMainWindow):
    def __init__(self,number):
        QMainWindow.__init__(self)
        loader = QUiLoader()

        form = loader.load("./res/complete.ui", self)
        self.setCentralWidget(form)

        self.setWindowTitle("Order")
        self.move(100,100) 

        self.numberL =  self.bg1 = form.findChild(QLabel, "Number")
        self.numberL.setText(str(number))

        bn = form.findChild(QPushButton, "Next")
        bb = form.findChild(QPushButton, "Back") 

        bn.clicked.connect(self.Next)
        bb.clicked.connect(self.Back)

    def Next(self):
        pass

    def Back(self):
        pass
        
         


def main():
    app = QApplication(sys.argv)
    mywindow = ShowOrder(3721)
    mywindow.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())