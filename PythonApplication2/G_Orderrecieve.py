import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import G_Main

from client_Xtion import ChatClient
PORT = 21567

class ShowOrder(QMainWindow):
    def __init__(self,number,user):
        QMainWindow.__init__(self)
        loader = QUiLoader()

        form = loader.load("./res/order1.ui", self)
        self.setCentralWidget(form)

        self.setWindowTitle("Order")
        self.move(100,100) 

        self.numberL = form.findChild(QLabel, "Number")
        self.status = form.findChild(QLabel, "status")

        self.numberL.setText(number)

        self.number = number

        bn = form.findChild(QPushButton, "Next")
        bb = form.findChild(QPushButton, "Back") 

        bn.clicked.connect(self.check)
        bb.clicked.connect(self.Back)
        
        self.check()
        self.user = user


    def Back(self):
        self.mywindow = G_Main.MainWindow(self.user)
        self.mywindow.show()
        self.hide()

    def check(self):
        self.client = ChatClient(PORT)
        self.receive = self.client.send_message('C'+self.number)
        if(self.receive == 'N'):
            self.status.setText("NOT FOUND")
        else :
            self.status.setText(self.receive)
        
         


def main():
    app = QApplication(sys.argv)
    mywindow = ShowOrder(3721)
    mywindow.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())