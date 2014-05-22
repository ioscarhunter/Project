import sys
import res.resourse
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import Pizza,animate

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

        self.client = ChatClient(PORT)

        self.order = form.findChild(QLabel,"Logo")
        self.button = form.findChild(QPushButton,"Try")
        self.recieve = "Fail"
        self.send()
        
        

    def send(self):
        self.recieve = self.client.send_message(self.detail)
        if(self.recieve == "Fail"):
            self.order.setText("ERROR\nTRY AGAIN")
            self.button.setEnabled(True)
       

def main():
    app = QApplication(sys.argv)
    mywindow = send()
    mywindow.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())


