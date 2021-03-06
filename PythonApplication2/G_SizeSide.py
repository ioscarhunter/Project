import sys
import res.resourse
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import G_Topping,G_Main,Pizza,User

class SizeSide(QMainWindow):
    def __init__(self,pizza,user):
        QMainWindow.__init__(self)
        loader = QUiLoader()

        form = loader.load("./res/Size.ui", self)
        self.setCentralWidget(form)
        self.pizza = pizza

        self.setWindowTitle("Size and Side")
        self.move(100,100) 
        self.flag = 0

        self.user = user

        self.bg1 = form.findChild(QPushButton, "bg1")
        self.bg2 = form.findChild(QPushButton, "bg2")
        self.bg3 = form.findChild(QPushButton, "bg3")
        self.bg4 = form.findChild(QPushButton, "bg4")
        self.bg5 = form.findChild(QPushButton, "bg5")

        S = form.findChild(QPushButton, "S")
        M = form.findChild(QPushButton, "M")
        L = form.findChild(QPushButton, "L")
        T1 = form.findChild(QPushButton, "Thin")
        T2 = form.findChild(QPushButton, "Thick")

        self.next = form.findChild(QPushButton, "Next")
        self.back = form.findChild(QPushButton, "Back")

        S.clicked.connect(self.Small)
        M.clicked.connect(self.Medium)
        L.clicked.connect(self.Large)

        T1.clicked.connect(self.Thin)
        T2.clicked.connect(self.Thick)

        self.next.clicked.connect(self.Next)
        self.back.clicked.connect(self.Back)

        self.setstart()

    def Small(self):
        self.bg1.setEnabled(False)
        self.bg2.setEnabled(True)
        self.bg3.setEnabled(True)
        self.pizza.order[0] = 1

    def Medium(self):
        self.bg1.setEnabled(True)
        self.bg2.setEnabled(False)
        self.bg3.setEnabled(True)
        self.pizza.order[0] = 2

    def Large(self):
        self.bg1.setEnabled(True)
        self.bg2.setEnabled(True)
        self.bg3.setEnabled(False)
        self.pizza.order[0] = 3
    
    def Thin(self):
        self.bg4.setEnabled(False)
        self.bg5.setEnabled(True)
        self.pizza.order[1] = 1

    def Thick(self):
        self.bg4.setEnabled(True)
        self.bg5.setEnabled(False)
        self.pizza.order[1] = 2

    def Next(self):
        print(self.flag)
        if (self.flag == 0):
            if(self.pizza.order[0]!=0 and self.pizza.order[1]!=0):
                self.top = G_Topping.Topping(self.pizza,self.user)
                self.top.show()
                self.hide()
        else:
            self.flag = 0
            self.next.setText("Next>")
            self.back.setText("Back")
    def Back(self):
        if(self.flag == 0):
            self.back.setText("Discard")
            self.next.setText("Continue")
            self.flag = 1
        else:
            self.mywindow = G_Main.MainWindow(self.user)
            self.mywindow.show()
            self.hide()

    def setstart(self):
        if(self.pizza.order[0] == 1):
            self.Small()
        elif(self.pizza.order[0] == 2):
            self.Medium()
        elif(self.pizza.order[0] == 3):
            self.Large()
        if(self.pizza.order[1] == 1):
            self.Thin()
        elif(self.pizza.order[1] == 2):
            self.Thick()

