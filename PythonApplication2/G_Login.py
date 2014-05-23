import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import G_Main,User

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
        self.status= self.form.findChild(QLabel,"sta")
        
        self.usr = self.form.findChild(QLineEdit,"usr")
        self.pwd = self.form.findChild(QLineEdit,"pwd")

        self.next.clicked.connect(self.login)
        self.back.clicked.connect(self.loadstart)

    def loadcreate(self):
        self.form = self.loader.load("./res/Regis.ui", self)
        self.setCentralWidget(self.form)
        self.setWindowTitle("Registor")

        self.next = self.form.findChild(QPushButton,"b1")
        self.back = self.form.findChild(QPushButton,"b2")

        self.usr = self.form.findChild(QLineEdit,"usr")
        self.pwd = self.form.findChild(QLineEdit,"pwd")
        self.pwd2 = self.form.findChild(QLineEdit,"pwd_2")

        self.status= self.form.findChild(QLabel,"sta")

        self.next.clicked.connect(self.registor)
        self.back.clicked.connect(self.loadstart)

    def login(self):
        if(self.usr.text() == ""):
            self.status.setText("Please Enter Username")
        elif(self.pwd.text() == ""):
            self.status.setText("Please Enter Password")
        else:
            self.status.setText("Signing in")
            detail = "L?"+self.usr.text()+'?'+self.pwd.text()
        
            self.client = ChatClient(PORT)
            self.recieve = self.client.send_message(detail)
            if(self.recieve == "Fail"):
                self.status.setText("Connection Error")
            elif(self.recieve == "F"):
                self.status.setText("Username or Password Incorrect")
            else :
                data = self.recieve
                self.user = User.account(self.usr.text())
                self.user.info = data.split("<>")[:-1]
                mywindow = G_Main.MainWindow(self.user)
                mywindow.show()


            
    def registor(self):
        if(self.usr.text() == ""):
            self.status.setText("Please Enter Username")
        elif(self.pwd.text() == ""):
            self.status.setText("Please Enter Password")
        elif(self.pwd2.text() == ""):
            self.status.setText("Please Enter Password Again")
        elif(self.pwd.text() != self.pwd2.text()):
                self.status.setText("Password Not Match")
        else: 
            self.status.setText("Registering")
            detail = "R?"+self.usr.text()+'?'+self.pwd.text()
        
            self.client = ChatClient(PORT)
            self.recieve = self.client.send_message(detail)
            print(self.recieve)
            if(self.recieve == "Fail"):
                self.status.setText("Connection Error")
            elif(self.recieve == "T"):
                self.status.setText("Registerd")
                self.next.setEnabled(False)
                self.use.setEnabled(False)
                self.pwd.setEnabled(False)
                self.pwd2.setEnabled(False)
            else :
                self.status.setText("Username Ready Exit")
    
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