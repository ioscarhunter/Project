import sys
import res.resourse
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import G_Topping,G_Custom,Pizza,G_Send,Calculate


class Info(QMainWindow):
    def __init__(self,pizza,user):
        QMainWindow.__init__(self)
        loader = QUiLoader()

        form = loader.load("./res/askdetail.ui", self)
        self.setCentralWidget(form)
        self.pizza = pizza
        self.setWindowTitle("Information")
        self.move(100,100)
        
        self.cal = Calculate.My_calcu(self.pizza)
        self.prize = self.cal.getPrize()

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
        self.amount.setValue(self.pizza.order[3])
        self.setDetail()

        self.next.clicked.connect(self.confirm)
        self.back.clicked.connect(self.goback)

        self.prizeL.setText(str(self.amount.value()*self.prize))
        self.user = user
        

    def goback(self):
        if(self.pizza.order[2]!=8):
            self.mywindow = G_Topping.Topping(self.pizza,self.user)
            self.mywindow.show()
        else:
            self.c = G_Custom.Custom(self.pizza,self.user)                 
            self.c.show()
        self.close()


    def changeAmount(self):

        self.prizeL.setText(str(self.amount.value()*self.prize))
        self.pizza.order[3] = self.amount.value()

    def setDetail(self):
        size=['','Small','Medium','Large']
        side = ['','Thin','Thick']

        topping = ['','Hawaiian','Seafood','Tom Yum Kung','Cheese','Sausage & Ham','Peperonee','Spacial']
        extra = ['Sausage','Beef','Bacon','Peper','Champig','Pork','Shrimp','Onion','Octopus','Cheese','Tomato','Pineapple']

        strtmp = "Size: "
        strtmp+=size[self.pizza.order[0]]+"\n"
        strtmp+= "Side: "
        strtmp+=side[self.pizza.order[1]]+"\n"
        j=0
        strtmp += "Topping : "
        if (self.pizza.order[2] == 8):
            for i in range(0,12):
                if(self.pizza.extra[i] == 1):
                    if(j%4==0 and j!=0):
                        strtmp+=extra[i]+"\n"
                    else:
                        strtmp+=extra[i]+", "
                    
                    j+=1                             
            if(j==0):
                strtmp+= "Plan"
        else:
            strtmp+=topping[self.pizza.order[2]]
        self.detail.setText(strtmp)


    def confirm(self):
        if (self.name.text()!='' and self.phone.text()!='' and self.adress.toPlainText()!=''):
            self.user.info = [self.name.text(),self.phone.text(),self.adress.toPlainText()]            
            self.s = G_Send.send(self.pizza.export(self.prize)+self.mouseReleaseEvent.export(),self.user)
            self.s.show()
            self.hide()
        else:
            self.next.setText("Invalid Information")
            QTimer().singleShot(1000, lambda: self.next.setText("CONFIRM!"))
            
        
                    
def main():
    app = QApplication(sys.argv)

    P = Pizza.Pizza()
    mywindow = Info(P)
    mywindow.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())