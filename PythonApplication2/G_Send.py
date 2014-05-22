import sys
import res.resourse
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import Pizza,animate

from client_Xtion import ChatClient
PORT = 21567

class send(QMainWindow):
    def __init__(self):        
        QMainWindow.__init__(self)
        loader = QUiLoader()
        self.setGeometry(100, 100, 391, 400)
        self.setWindowTitle("Sending")
        form = loader.load("./res/sending.ui", self)
        self.setMenuWidget (form)
        player = animate.MoviePlayer()
        self.setCentralWidget(player)

        self.order = form.findChild(QLabel,"Logo")

        client = ChatClient(PORT)

       

def main():
    app = QApplication(sys.argv)
    P = Pizza.Pizza()
    mywindow = send()
    mywindow.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())


