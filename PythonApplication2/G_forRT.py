
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

        #self.form.setMinimumSize(885,547)
        #self.setMaximumSize(885,547)
        self.setFixedSize(985,547)

        m = ["21/05/14","13:51","0001",1,1,2,[0,0,0,0,0,0,0,0,0,0,0,0],"Dan","098-9228292","18/3 djdj road",1,450,"-Process-"]
        self.Bsave = self.form.findChild(QPushButton, "Bedit")
        self.Brefesh = self.form.findChild(QPushButton,"Bref")
        self.StatusTB = self.form.findChild(QTableWidget,"StatusTB")
        self.Status = self.form.findChild(QComboBox,"comboBox")
        self.Ordernum = self.form.findChild(QLineEdit,"lineEdit")
        self.Date = self.form.findChild(QDateEdit,"dateEdit")
        
        self.server = server_Xtion.Server_connection(PORT)
        threading.Thread(target=self.server.run).start()
        self.SL = SQL.SQL()

        self.StatusTB.insertRow(1)
        a = ["2","22/05/14","14:57","0","0","6","1","199","-","Jane","0899999999","23/4 jane road","Processing"]
        for i in range(self.StatusTB.columnCount()):
            self.StatusTB.setItem(1,i,QTableWidgetItem(a[i]))
        

        #self.StatusTB.removeRow(0)
        print(self.StatusTB.rowCount())
        #print(self.Date.date().toString("dd:MM:yy"))
        
        
        self.Date.dateChanged.connect(self.Update)
        self.Bsave.clicked.connect(self.set_Status)
        self.Brefesh.clicked.connect(self.Update)
        self.Date.setDate(QDate.currentDate())


    def Update(self):
        datenow = self.Date.date().toString("ddMMyyyy")
        print(datenow)
        for i in reversed(range(self.StatusTB.rowCount())):
            self.StatusTB.removeRow(i)

        self.insert_many(self.SL.getrow(datenow))
            
        #if clear already find the datenow from sql and insert from the first row

    def insert_many(self,data):

        for i in range (len(data)):
            ex = data[i][8:20]
            tmp = data[i][:8]
            tmp.extend(data[i][20:])
            tmp.insert(8,ex)
            self.StatusTB.insertRow(i)
            for j in range (len(tmp)):
                self.StatusTB.setItem(i,j,QTableWidgetItem(str(tmp[j])))
        
    def set_Status(self):
        s = self.Ordernum.text()
        status = str(self.Status.currentText())
        self.SL.setStatus(s,status)
        self.Update()
        


def main():
    app = QApplication(sys.argv)

    w = My_forRT()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

