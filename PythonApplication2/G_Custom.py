import sys
import res.resourse
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import G_Topping,G_information,Pizza,User

class Custom(QMainWindow):
    def __init__(self,pizza,user):
        QMainWindow.__init__(self)
        loader = QUiLoader()

        form = loader.load("./res/Extra.ui", self)
        self.setCentralWidget(form)
        self.selected = 0  

        self.setWindowTitle("Custom Topping")
        self.move(100,100)
        
        self.pizza = pizza
                                                     
        self.bg1 = form.findChild(QPushButton, "bg1")
        self.bg2 = form.findChild(QPushButton, "bg2")
        self.bg3 = form.findChild(QPushButton, "bg3")
        self.bg4 = form.findChild(QPushButton, "bg4")
        self.bg5 = form.findChild(QPushButton, "bg5")
        self.bg6 = form.findChild(QPushButton, "bg6")
        self.bg7 = form.findChild(QPushButton, "bg7")
        self.bg8 = form.findChild(QPushButton, "bg8")
        self.bg9 = form.findChild(QPushButton, "bg9")
        self.bg10 = form.findChild(QPushButton, "bg10")
        self.bg11 = form.findChild(QPushButton, "bg11")
        self.bg12 = form.findChild(QPushButton, "bg12")


        b1 = form.findChild(QPushButton, "Saug_1")
        b2 = form.findChild(QPushButton, "Beef_2")
        b3 = form.findChild(QPushButton, "Baco_3")
        b4 = form.findChild(QPushButton, "Pepe_4")
        b5 = form.findChild(QPushButton, "Cham_5")
        b6 = form.findChild(QPushButton, "Pork_6")
        b7 = form.findChild(QPushButton, "Shri_7")
        b8 = form.findChild(QPushButton, "Onio_8")
        b9 = form.findChild(QPushButton, "Octo_9")
        b10 = form.findChild(QPushButton, "Ches_10")
        b11 = form.findChild(QPushButton, "Toma_11")
        b12 = form.findChild(QPushButton, "Pine_12")

        bn = form.findChild(QPushButton, "Next")
        bb = form.findChild(QPushButton, "Back") 

        self.user = user

        b1.clicked.connect(self.one)
        b2.clicked.connect(self.two)
        b3.clicked.connect(self.tree)
        b4.clicked.connect(self.four)
        b5.clicked.connect(self.five)
        b6.clicked.connect(self.six)
        b7.clicked.connect(self.seven)
        b8.clicked.connect(self.eigth)
        b9.clicked.connect(self.nine)
        b10.clicked.connect(self.ten)
        b11.clicked.connect(self.elev)
        b12.clicked.connect(self.twen)

        bn . clicked.connect(self.next)
        bb . clicked.connect(self.back)
        self.setstart()

    def one(self):
        if(self.bg1.isEnabled()):
            self.bg1.setEnabled(False)
            self.pizza.extra[0] = 1
        else:
            self.bg1.setEnabled(True)
            self.pizza.extra[0] = 0


    def two(self):
        if(self.bg2.isEnabled()):
            self.bg2.setEnabled(False)
            self.pizza.extra[1] = 1
        else:
            self.bg2.setEnabled(True)
            self.pizza.extra[1] = 0

    def tree(self):
        if(self.bg3.isEnabled()):
            self.bg3.setEnabled(False)
            self.pizza.extra[2] = 1
        else:
            self.bg3.setEnabled(True)
            self.pizza.extra[2] = 0

    def four(self):
        if(self.bg4.isEnabled()):
            self.bg4.setEnabled(False)
            self.pizza.extra[3] = 1
        else:
            self.bg4.setEnabled(True)
            self.pizza.extra[3] = 0

    def five(self):
        if(self.bg5.isEnabled()):
            self.bg5.setEnabled(False)
            self.pizza.extra[4] = 1
        else:
            self.bg5.setEnabled(True)
            self.pizza.extra[4] = 0
        
    def six(self):
        if(self.bg6.isEnabled()):
            self.bg6.setEnabled(False)
            self.pizza.extra[5] = 1
        else:
            self.bg6.setEnabled(True)
            self.pizza.extra[5] = 0

    def seven(self):
        if(self.bg7.isEnabled()):
            self.bg7.setEnabled(False)
            self.pizza.extra[6] = 1
        else:
            self.bg7.setEnabled(True)
            self.pizza.extra[6] = 0

    def eigth(self):
        if(self.bg8.isEnabled()):
            self.bg8.setEnabled(False)
            self.pizza.extra[7] = 1
        else:
            self.bg8.setEnabled(True)
            self.pizza.extra[7] = 0

    def nine(self):
        if(self.bg9.isEnabled()):
            self.bg9.setEnabled(False)
            self.pizza.extra[8] = 1
        else:
            self.bg9.setEnabled(True)
            self.pizza.extra[8] = 0

    def ten(self):
        if(self.bg10.isEnabled()):
            self.bg10.setEnabled(False)
            self.pizza.extra[9] = 1
        else:
            self.bg10.setEnabled(True)
            self.pizza.extra[9] = 0

    def elev(self):
        if(self.bg11.isEnabled()):
            self.bg11.setEnabled(False)
            self.pizza.extra[10] = 1
        else:
            self.bg11.setEnabled(True)
            self.pizza.extra[10] = 0

    def twen(self):
        if(self.bg12.isEnabled()):
            self.bg12.setEnabled(False)
            self.pizza.extra[11] = 1
        else:
            self.bg12.setEnabled(True)
            self.pizza.extra[11] = 0

    def next(self):
        self.info = G_information.Info(self.pizza,self.user)
        self.info.show()
        self.close()


    def back(self):
        self.mywindow = G_Topping.Topping(self.pizza,self.user)
        self.mywindow.show()
        self.close()

    def setstart(self):
        if(self.pizza.extra[0] == 1):
            self.bg1.setEnabled(False)
        if(self.pizza.extra[1] == 1):
            self.bg2.setEnabled(False)
        if(self.pizza.extra[2] == 1):
            self.bg3.setEnabled(False)
        if(self.pizza.extra[3] == 1):
            self.bg4.setEnabled(False)
        if(self.pizza.extra[4] == 1):
            self.bg5.setEnabled(False)
        if(self.pizza.extra[5] == 1):
            self.bg6.setEnabled(False)
        if(self.pizza.extra[6] == 1):
            self.bg7.setEnabled(False)
        if(self.pizza.extra[7] == 1):
            self.bg8.setEnabled(False)
        if(self.pizza.extra[8] == 1):
            self.bg9.setEnabled(False)
        if(self.pizza.extra[9] == 1):
            self.bg10.setEnabled(False)
        if(self.pizza.extra[10] == 1):
            self.bg11.setEnabled(False)
        if(self.pizza.extra[11] == 1):
            self.bg12.setEnabled(False)
                                                                                          