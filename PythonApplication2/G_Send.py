import sys
import res.resourse
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import Pizza,animate,time,G_Orderrecieve

import threading 
import time

from client_Xtion import ChatClient
PORT = 21567

class send(QMainWindow):
    def __init__(self,orderdetail):        
        QMainWindow.__init__(self)
        loader = QUiLoader()
        self.setGeometry(100, 100, 391, 400)
        self.setWindowTitle("Sending")
        form = loader.load("./res/sending.ui", self)
        self.setMenuWidget (form)
        self.player = animate.MoviePlayer()
        self.setCentralWidget(self.player)
        self.detail = orderdetail
        print(self.detail)
        self.client = ChatClient(PORT)

        self.order = form.findChild(QLabel,"Logo")
        self.button = form.findChild(QPushButton,"Try")
        self.recieve = "Fail"
        self.timerScreen = QTimer()
        self.timerScreen.singleShot(1000, lambda: self.send())

        self.button.clicked.connect(self.Try)
        
        

    def send(self):
        self.recieve = self.client.send_message(self.detail)
        if(self.recieve == "Fail"):
            self.order.setText("ERROR\nTRY AGAIN")
            self.button.setEnabled(True)
            self.setWindowTitle("Fail")
            
        else:
            self.orc = G_Orderrecieve.ShowOrder(self.recieve)
            self.orc.show()
            self.hide()

    def Try(self):
        self.button.setEnabled(False)
        self.order.setText("SENDING\nORDER")
        self.setWindowTitle("Sending")
        self.timerScreen.singleShot(1000, lambda: self.send())
       




def main():
    app = QApplication(sys.argv)
    mywindow = send("fff")
    mywindow.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())


