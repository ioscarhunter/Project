
import threading
import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from PySide.QtCore import QDate

import SQL,server_Xtion
PORT = 21567
class My_forRT(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        loader = QUiLoader()
        self.form = loader.load("./res/ForRT.ui", self)
        self.setCentralWidget(self.form)


       
        self.Bsave = self.form.findChild(QPushButton, "Bedit")
        self.Brefesh = self.form.findChild(QPushButton,"Bref")
        self.StatusTB = self.form.findChild(QTableWidget,"StatusTB")
        self.Status = self.form.findChild(QComboBox,"comboBox")
        self.Ordernum = self.form.findChild(QLineEdit,"lineEdit")
        self.Date = self.form.findChild(QDateEdit,"dateEdit")
        
        self.server = server_Xtion.Server_connection(PORT)
        threading.Thread(target=self.server.run).start()
        self.SL = SQL.SQL()

        self.Date.dateChanged.connect(self.Update)
        self.Bsave.clicked.connect(self.set_Status)
        self.Brefesh.clicked.connect(self.Update)
        self.Date.setDate(QDate.currentDate())


    def Update(self):
        datenow = self.Date.date().toString("ddMMyyyy")
        print(datenow)
        for i in reversed(range(self.StatusTB.rowCount())):
            self.StatusTB.removeRow(i)

        data = self.SL.getrow(datenow)

        self.insert_many(data)
        self.StatusTB.resizeColumnsToContents()
            
        #if clear already find the datenow from sql and insert from the first row

    def insert_many(self,data):

        for i in range (len(data)):
            ex = data[i][8:20]
            tmp = data[i][:8]
            tmp.extend(data[i][20:])
            tmp.insert(8,ex)
            self.formatdata(tmp)        

            self.StatusTB.insertRow(i)
            for j in range (len(tmp)):
                self.StatusTB.setItem(i,j,QTableWidgetItem(str(tmp[j])))
        
    def set_Status(self):
        s = self.Ordernum.text()
        status = str(self.Status.currentText())
        self.SL.setStatus(s,status)
        self.Update()
        
    def formatdata(self,data):

        size=['','Small','Medium','Large']
        side = ['','Thin','Thick']

        topping = ['','Hawaiian','Seafood','Tom Yum Kung','Cheese','Sausage & Ham','Peperonee','Spacial','Custom']
        extra = ['Sausage','Beef','Bacon','Peper','Champig','Pork','Shrimp','Onion','Octopus','Cheese','Tomato','Pineapple']

        data[1] = data[1][:2]+"/"+data[1][3:5]+"/"+data[1][4:]
        data[2] = data[2][:2]+":"+data[2][2:4]+":"+data[2][4:]
        data[3] = size[int(data[3])]
        data[4] = side[int(data[4])]
        data[5] = topping[int(data[5])]
        if(data[5]!='Custom'):
            data[8] = '-'
        else:
            tmp = ""
            for i in range (len(data[8])):
                if (data[8][i] == '1'):
                    tmp+=extra[i]
                    tmp+=","
            data[8] = tmp


def main():
    app = QApplication(sys.argv)

    w = My_forRT()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
