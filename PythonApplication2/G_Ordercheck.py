import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import G_Main,G_Orderrecieve,User
from client_Xtion import ChatClient
PORT = 21567

class ShowOrder(QMainWindow):
    def __init__(self,user):
        QMainWindow.__init__(self)
        loader = QUiLoader()

        form = loader.load("./res/checkorder.ui", self)
        self.setCentralWidget(form)

        self.setWindowTitle("Order")
        self.move(100,100) 

        self.user = user

        self.numberL = form.findChild(QLineEdit, "Number")
        self.status1 = form.findChild(QLabel,"status")
        self.status2 = form.findChild(QLabel,"status2")
        self.Refresh = form.findChild(QPushButton,"ref")

        self.bn = form.findChild(QPushButton, "Next")
        bb = form.findChild(QPushButton, "Back") 

        self.bn.clicked.connect(self.Next)
        bb.clicked.connect(self.Back)
        self.Refresh.clicked.connect(self.startcheck)

        self.startcheck()

    def checkint(self,input):
        try:
            int(input)
        except(ValueError):
            return False
        return True

    def Next(self):
        if(self.checkint(self.numberL.text())):
            self.ord = G_Orderrecieve.ShowOrder(self.numberL.text(),self.user)
            self.bn.setText("CHECKING")
            QTimer().singleShot(500, lambda: self.ord.show())
            QTimer().singleShot(500, lambda: self.hide())
        else:
            self.bn.setText("NUMBER ERROR")
            QTimer().singleShot(1000, lambda: self.bn.setText("CHECK"))

    def Back(self):
        self.mywindow = G_Main.MainWindow(self.user)
        self.mywindow.show()
        self.hide()

    def startcheck(self):
        self.client = ChatClient(PORT)
        self.receive = self.client.send_message('M'+self.user.username)
        tmp = self.receive.split("?")
        num = ""
        sta = ""
        print(tmp)
        if(tmp!="n"):
            for i in range (len(tmp)):
                if(i%2 == 0):
                    num+=tmp[i]
                    if(i<(len(tmp)-3)):
                        num+="\n"
                else:
                    sta+=tmp[i]     
                    if(i!=(len(tmp)-2)):
                        sta+="\n"    
            self.status1.setText(num)                              
            self.status2.setText(sta)
