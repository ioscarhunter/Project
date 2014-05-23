import sys
import res.resourse
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import G_Custom,G_information,Pizza,G_SizeSide


class Topping(QMainWindow):
    def __init__(self,pizza,user):
        QMainWindow.__init__(self)
        loader = QUiLoader()

        form = loader.load("./res/menu.ui", self)
        self.setCentralWidget(form)
        self.pizza = pizza

        self.setWindowTitle("Topping")
        self.move(100,100)        
                
                                                    
        self.bg1 = form.findChild(QPushButton, "bg1")
        self.bg2 = form.findChild(QPushButton, "bg2")
        self.bg3 = form.findChild(QPushButton, "bg3")
        self.bg4 = form.findChild(QPushButton, "bg4")
        self.bg5 = form.findChild(QPushButton, "bg5")
        self.bg6 = form.findChild(QPushButton, "bg6")
        self.bg7 = form.findChild(QPushButton, "bg7")
        self.bg8 = form.findChild(QPushButton, "bg8")

        b1 = form.findChild(QPushButton, "hawi_1")
        b2 = form.findChild(QPushButton, "sea_2")
        b3 = form.findChild(QPushButton, "tomy_3")
        b4 = form.findChild(QPushButton, "che_4")
        b5 = form.findChild(QPushButton, "sau_5")
        b6 = form.findChild(QPushButton, "pep_6")
        b7 = form.findChild(QPushButton, "spa_7")
        b8 = form.findChild(QPushButton, "cust_8")
        self.lebel = form.findChild(QLabel,"toping")

        self.bn = form.findChild(QPushButton, "Next")
        bb = form.findChild(QPushButton, "Back") 


        b1.clicked.connect(self.one)
        b2.clicked.connect(self.two)
        b3.clicked.connect(self.tree)
        b4.clicked.connect(self.four)
        b5.clicked.connect(self.five)
        b6.clicked.connect(self.six)
        b7.clicked.connect(self.seven)
        b8.clicked.connect(self.eigth)

        self.user = user

        self.bn . clicked.connect(self.next)
        bb . clicked.connect(self.back)

        self.setstartup(self.pizza.order[2]) 

    def one(self):
        self.bg1.setEnabled(False)
        self.setselection(1)
        self.next()

    def two(self):
        self.bg2.setEnabled(False)
        self.setselection(2)
        self.next()

    def tree(self):
        self.bg3.setEnabled(False)
        self.setselection(3)
        self.next()

    def four(self):
        self.bg4.setEnabled(False)
        self.setselection(4)
        self.next()

    def five(self):
        self.bg5.setEnabled(False)
        self.setselection(5)
        self.next()
        
    def six(self):
        self.bg6.setEnabled(False)
        self.setselection(6)
        self.next()

    def seven(self):
        self.bg7.setEnabled(False)
        self.setselection(7)
        self.next()

    def eigth(self):
        self.bg8.setEnabled(False)
        self.setselection(8)
        self.next()

    def next(self):
        if self.pizza.order[2] == 0:
            self.lebel.setText("  Please select the topping")
            self.bn.setText("No topping Select")
            QTimer().singleShot(1000, lambda: self.bn.setText("Next >"))
        else:
            if self.pizza.order[2] == 8:
                self.c =G_Custom.Custom(self.pizza,self.user)                 
                self.c.show()
                c = None
                self.close()
                
            else :
                self.info = G_information.Info(self.pizza,self.user)
                self.info.show()
                self.close()


    def back(self):
        self.G = G_SizeSide.SizeSide(self.pizza,self.user)
        self.G.show()
        self.hide()

    def setselection(self,num):
        self.pizza.order[2] = num
        if(num!=1):
            self.bg1.setEnabled(True)   
        if(num!=2):
            self.bg2.setEnabled(True) 
        if(num!=3):
            self.bg3.setEnabled(True) 
        if(num!=4):
            self.bg4.setEnabled(True) 
        if(num!=5):
            self.bg5.setEnabled(True) 
        if(num!=6):
            self.bg6.setEnabled(True) 
        if(num!=7):
            self.bg7.setEnabled(True) 
        if(num!=8):
            self.bg8.setEnabled(True) 


    def setstartup(self,num):
        if(num==1):
            self.bg1.setEnabled(False)   
        if(num==2):
            self.bg2.setEnabled(False) 
        if(num==3):
            self.bg3.setEnabled(False) 
        if(num==4):
            self.bg4.setEnabled(False) 
        if(num==5):
            self.bg5.setEnabled(False) 
        if(num==6):
            self.bg6.setEnabled(False) 
        if(num==7):
            self.bg7.setEnabled(False) 
        if(num==8):
            self.bg8.setEnabled(False)


                                                                                                                
def main():
    app = QApplication(sys.argv)
    P = Pizza.Pizza()
    mywindow = Topping(P)
    mywindow.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())