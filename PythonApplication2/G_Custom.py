import sys
import res.resourse
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class Custom(QMainWindow):
    def __init__(self,x):
        QMainWindow.__init__(self)
        loader = QUiLoader()

        form = loader.load("./res/Extra.ui", self)
        self.setCentralWidget(form)
        self.selected = 0  
        
        self.temp = [0,0,0,0,0,0,0,0,0,0,0,0]
                                                     
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

    def one(self):
        if(self.bg1.isEnabled()):
            self.bg1.setEnabled(False)
            self.temp[0] = 1
        else:
            self.bg1.setEnabled(True)
            self.temp[0] = 0


    def two(self):
        if(self.bg2.isEnabled()):
            self.bg2.setEnabled(False)
            self.temp[1] = 1
        else:
            self.bg2.setEnabled(True)
            self.temp[1] = 0

    def tree(self):
        if(self.bg3.isEnabled()):
            self.bg3.setEnabled(False)
            self.temp[2] = 1
        else:
            self.bg3.setEnabled(True)
            self.temp[2] = 0

    def four(self):
        if(self.bg4.isEnabled()):
            self.bg4.setEnabled(False)
            self.temp[3] = 1
        else:
            self.bg4.setEnabled(True)
            self.temp[3] = 0

    def five(self):
        if(self.bg5.isEnabled()):
            self.bg5.setEnabled(False)
            self.temp[4] = 1
        else:
            self.bg5.setEnabled(True)
            self.temp[4] = 0
        
    def six(self):
        if(self.bg6.isEnabled()):
            self.bg6.setEnabled(False)
            self.temp[5] = 1
        else:
            self.bg6.setEnabled(True)
            self.temp[5] = 0

    def seven(self):
        if(self.bg7.isEnabled()):
            self.bg7.setEnabled(False)
            self.temp[6] = 1
        else:
            self.bg7.setEnabled(True)
            self.temp[6] = 0

    def eigth(self):
        if(self.bg8.isEnabled()):
            self.bg8.setEnabled(False)
            self.temp[7] = 1
        else:
            self.bg8.setEnabled(True)
            self.temp[7] = 0

    def nine(self):
        if(self.bg9.isEnabled()):
            self.bg9.setEnabled(False)
            self.temp[8] = 1
        else:
            self.bg9.setEnabled(True)
            self.temp[8] = 0

    def ten(self):
        if(self.bg10.isEnabled()):
            self.bg10.setEnabled(False)
            self.temp[9] = 1
        else:
            self.bg10.setEnabled(True)
            self.temp[9] = 0

    def elev(self):
        if(self.bg11.isEnabled()):
            self.bg11.setEnabled(False)
            self.temp[10] = 1
        else:
            self.bg11.setEnabled(True)
            self.temp[10] = 0

    def twen(self):
        if(self.bg12.isEnabled()):
            self.bg12.setEnabled(False)
            self.temp[11] = 1
        else:
            self.bg12.setEnabled(True)
            self.temp[11] = 0

    def next(self):
        pass


    def back(self):
        pass

   
                                                                                                                
def main():
    app = QApplication(sys.argv)
    x = [1,2,3]
    mywindow = Custom(x)
    mywindow.show()
    print(x)
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())