import sqlite3
import time

class SQL:
    def __init__(self):
        self.connect = sqlite3.connect('stocks.db')
        self.extra = sqlite3.connect('extra.db')
        self.info = sqlite3.connect('infor.db')
        self.status = sqlite3.connect('status.db')

        self.e = self.extra.cursor()
        self.c = self.connect.cursor()
        self.inf = self.info.cursor()
        self.st = self.status.cursor()

        self.ordernum = 0
        self.date = time.strftime("%d:%m:%Y")
        self.time = time.strftime("%H:%M:%S")
        try:
            self.c.execute("CREATE TABLE stocks(ordernum integer, date text,time text,size text,side text,topping text,amount integer, prize integer)") # Create Table if it not excite
            self.e.execute("CREATE TABLE extra(ordernum integer,Sausage&Pepperonee integer,Beef integer,Bacon integer,Peperone integer,Champignon integer,Pork integer,Shrimp integer,Onion integer,Octopus integer,Shrimp integer,Cheese integer,Tomato integer,'Pineapple integer")
            self.inf.execute("CREATE TABLE contrac(ordernum integer,name text,phone text,addr text")
            self.st.execute("CREATE TABLE status(ordernum integer,sta text)")
        except:
            self.ordernum = self.c.execute('SELECT max(ordernum) FROM stocks')
            #load ordernum

    def insert(self, data1,data2,data3,data4):
        self.c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?,?,?)', data1)
        self.e.executemany('INSERT INTO extra VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',data2)
        self.inf.executemany('INSERT INTO contrac VALUES (?,?,?,?)',data3)
        self.st.executemany('INSETRT INTO status(?,?)',data4)

        self.connect.commit()
        self.extra.commit()
        self.info.commit()

    def printrow(self,statement):
        for row in self.c.execute(statement):
            print(row)

    def decode(self,text):
        if(text.startswith("O")):
            tmp = text.split('<>')
            self.date = time.strftime("%d:%m:%Y")
            self.time = time.strftime("%H:%M:%S")
            if (len(tmp) == 21):
                stoc = tmp[1:6]
                extra = tmp[6:18]
                addr = tmp[18:]
                self.ordernum+=1
                stoc.insert(0,self.ordernum)
                stoc.insert(1,self.date)
                extra.insert(0,self.ordernum)

                self.insert(stoc,extra)
                return ordernum
            return 'F'
        elif(text.startswitch("C")):
            num = int(text[1:])
            x =[]
            for i in self.s.execute('SELECT status FROM st WHERE ordernum ='+num):
                x.extend(i)

            if len(x)==0 :
                return 0
            return x[0]

            
    def getnumber(self):
        return self.ordernum

    def read(self,date):
        return self.c.execute('select * from stocks where date = '+date)

if __name__ == '__main__':
    sl = SQL()
    purchases = [('20012-03-28', 'BUY', 'Microsoft', 1000, 45.00),
             ('2011-03-05', 'BUY', 'Bata', 1000, 72.00),
             ('2007-04-06', 'SELL', 'fdd', 500, 53.00),]
    #sl.insert(purchases)
    sl.printrow('SELECT * FROM stocks ORDER BY date')
    sl.c.close()