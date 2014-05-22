import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import G_Main,G_Orderrecieve

class ShowOrder(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loader = QUiLoader()

        form = loader.load("./res/checkorder.ui", self)
        self.setCentralWidget(form)

        self.setWindowTitle("Order")
        self.move(100,100) 

        self.numberL =  self.bg1 = form.findChild(QLineEdit, "Number")

        self.bn = form.findChild(QPushButton, "Next")
        bb = form.findChild(QPushButton, "Back") 

        self.bn.clicked.connect(self.Next)
        bb.clicked.connect(self.Back)

    def checkint(self,input):
        try:
            int(input)
        except(ValueError):
            return False
        return True

    def Next(self):
        if(self.checkint(self.numberL.text())):
            self.ord = G_Orderrecieve.ShowOrder(self.numberL.text())
            self.ord.show()
            self.hide()
        else:
            self.bn.setText("NUMBER ERROR")
            QTimer().singleShot(1000, lambda: self.bn.setText("CHECK"))

    def Back(self):
        self.mywindow = G_Main.MainWindow()
        self.mywindow.show()
        self.hide()
        
         


def main():
    app = QApplication(sys.argv)
    mywindow = ShowOrder()
    mywindow.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())