import sys
import res.resourse
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import Pizza,G_SizeSide,G_Ordercheck,User,G_Login

class MainWindow(QMainWindow):
    def __init__(self,user):
        QMainWindow.__init__(self)
        loader = QUiLoader()

        form = loader.load("./res/Main.ui", self)
        self.setCentralWidget(form)

        self.setWindowTitle("Pizzamai")
        self.move(100,100) 

        order = form.findChild(QPushButton, "Order")
        check = form.findChild(QPushButton, "Status") 
        out = form.findChild(QPushButton, "logout")
        self.pizza = Pizza.Pizza()

        self.user = user

        order.clicked.connect(self.Next)
        check.clicked.connect(self.Back)
        out.clicked.connect(self.logout)

       
    def logout(self):
        self.windows = G_Login.Login()
        self.hide()
        self.windows.show()

    def Next(self):
        self.G = G_SizeSide.SizeSide(self.pizza,self.user)
        self.G.show()
        self.hide()

    def Back(self):
        self.G = G_Ordercheck.ShowOrder(self.user)
        self.G.show()
        self.hide()
