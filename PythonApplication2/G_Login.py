import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import G_Main,G_Orderrecieve

from client_Xtion import ChatClient
PORT = 21567

class menu(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.loader = QUiLoader()
        self.loadstart()
        

    def loadsignin(self):
        self.form = self.loader.load("./res/Login.ui", self)
        self.setCentralWidget(self.form)
        self.setWindowTitle("Sign in")

        self.next = self.form.findChild(QPushButton,"b1")
        self.back = self.form.findChild(QPushButton,"b2")

        self.next.clicked.connect(self.login)
        self.back.clicked.connect(self.loadstart)

    def loadcreate(self):
        self.form = self.loader.load("./res/Regis.ui", self)
        self.setCentralWidget(self.form)
        self.setWindowTitle("Registor")

        self.next = self.form.findChild(QPushButton,"b1")
        self.back = self.form.findChild(QPushButton,"b2")

        self.usr = self.form.findChild(QLindEdit,"usr")
        self.pwd = self.form.findChild(QLindEdit,"pwd")
        self.pwd2 = self.form.findChild(QLindEdit,"pwd2")

        self.next.clicked.connect(self.registor)
        self.back.clicked.connect(self.loadstart)

    def login(self):
        self.usr.Text(),self.pwd.Text()

    def registor(self):
        pass
    
    def loadstart(self):
        self.form = self.loader.load("./res/Start.ui", self)
        self.setCentralWidget(self.form)
        self.setWindowTitle("Welcome")
        self.move(100,100)
        self.flag = 0

        self.next = self.form.findChild(QPushButton,"b1")
        self.back = self.form.findChild(QPushButton,"b2")

        self.next.clicked.connect(self.loadsignin)
        self.back.clicked.connect(self.loadcreate)

def main():
    app = QApplication(sys.argv)

    mywindow = menu()
    mywindow.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())