import sys
import res.resourse
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import Pizza

class ShowOrder(QMainWindow):
    def __init__(self,number):
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