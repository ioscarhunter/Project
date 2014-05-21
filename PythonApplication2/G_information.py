import sys
import res.resourse
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import G_Topping,G_Custom

from client_Xtion import ChatClient

class Info(QMainWindow):
    def __init__(self,x,y):
        QMainWindow.__init__(self)
        loader = QUiLoader()

        form = loader.load("./res/askdetail.ui", self)
        self.setCentralWidget(form)
        self.x = x
        self.y = y
        self.setWindowTitle("Information")
        self.move(100,100)
        self.prize = 1
        self.ordernum = 0        
        self.name = form.findChild(QLineEdit,"lEname")
        self.phone = form.findChild(QLineEdit,"lEphone")
        self.adress = form.findChild(QTextEdit,"Addr")

        self.detail = form.findChild(QLabel,"Detail")
        self.amount = form.findChild(QSpinBox,"spinBox")
        self.prizeL = form.findChild(QLabel,"Prize")

        self.back = form.findChild(QPushButton,"Back")
        self.next = form.findChild(QPushButton,"Confirm")

        self.amount.valueChanged.connect(self.changeAmount)
        self.amount.setValue(self.x[3])
        self.setDetail()

        self.next.clicked.connect(self.confirm)


    def changeAmount(self):
        self.prizeL.setText(str(self.amount.value()*self.prize))

    def setDetail(self):
        size=['','Small','Medium','Large']
        side = ['','Thin','Thick']

        topping = ['','Hawaiian','Seafood','Tom Yum Kung','Cheese','Sausage & Ham','Peperonee','Spacial']
        extra = ['','Sausage&Pepperonee','Beef','Bacon','Peperone','Champignon','Pork','Shrimp','Onion','Octopus','Shrimp','Cheese','Tomato','Pineapple']

        strtmp = "Size: "
        strtmp+=size[self.x[0]]+"\n"
        strtmp+= "Side: "
        strtmp+=side[self.x[1]]+"\n"
        j=0
        strtmp += "Topping : "
        if (self.x[2] == 8):
            for i in range(0,12):
                if(self.y[i] == 1):
                    if(j%4==0 and j!=0):
                        strtmp+=extra[i]+"\n"
                    elif(j%4!=0 and j!=0):
                        strtmp+=extra[i]+", "
                    j+=1                             
            if(j==0):
                strtmp+= "Plan"
        else:
            strtmp+=topping[self.x[2]]
        self.detail.setText(strtmp)


    def confirm(self):
        if (self.name.text()!='' and self.phone.text()!='' and self.adress.toPlainText()!=''):
            self.export()
            

    def export(self):
        tmp = []
        tmp.extend(self.x)
        tmp.append(self.prize)
        tmp.extend(self.y)
        tmp.append(self.name.text())
        tmp.append(self.phone.text())
        tmp.append(self.adress.toPlainText())
        stri = "O"
        for i in tmp:
            stri+="<>"+str(i).rstrip()
        print (stri)
            
                    
def main():
    app = QApplication(sys.argv)
    x = [1,2,8,4]
    y = [0,0,1,0,1,0,0,0,0,0,1,1]
    mywindow = Info(x,y)
    mywindow.show()
    print(x)
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())