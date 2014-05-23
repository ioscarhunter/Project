import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import G_Main,G_Orderrecieve,User

class ShowOrder(QMainWindow):
    def __init__(self,number,user):
        QMainWindow.__init__(self)
        loader = QUiLoader()

        form = loader.load("./res/complete.ui", self)
        self.setCentralWidget(form)
        self.number = number
        self.user = user
        self.setWindowTitle("Order")
        self.move(100,100) 

        self.numberL =  self.bg1 = form.findChild(QLabel, "Number")
        self.numberL.setText(self.number)

        bn = form.findChild(QPushButton, "Next")
        bb = form.findChild(QPushButton, "Back") 

        bn.clicked.connect(self.Next)
        bb.clicked.connect(self.Back)

    def Next(self):
        self.ord = G_Orderrecieve.ShowOrder(self.number,self.user)
        self.ord.show()
        self.hide()

    def Back(self):
        self.mywindow = G_Main.MainWindow(self.user)
        self.mywindow.show()
        self.hide()
        
         


def main():
    app = QApplication(sys.argv)
    mywindow = ShowOrder(3721)
    mywindow.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())