import sys
import res.resourse
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import Pizza,G_SizeSide

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loader = QUiLoader()

        form = loader.load("./res/Main.ui", self)
        self.setCentralWidget(form)

        self.setWindowTitle("Pizzamai")
        self.move(100,100) 

        order = form.findChild(QPushButton, "Order")
        check = form.findChild(QPushButton, "Status") 
        self.pizza = Pizza.Pizza()

        order.clicked.connect(self.Next)
        check.clicked.connect(self.Back)

       

    def Next(self):
        self.G = G_SizeSide.SizeSide(self.pizza)
        self.G.show()
        self.hide()

    def Back(self):
        pass
        
         


def main():
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())