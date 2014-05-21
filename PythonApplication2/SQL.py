import sqlite3
import time
#conn = sqlite3.connect('example.db')
#c = conn.cursor()

##http://www.tutorialspoint.com/sqlite/sqlite_python.htm

#'''
## Larger example that inserts many records at a time
#purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#            ]
#c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
#conn.commit() #to save chance in the database
#'''
#for row in c.execute('SELECT * FROM stocks ORDER BY price'):
#        print(row[0])

#c.close()
class SQL:
    def __init__(self):
        self.connect = sqlite3.connect('stocks.db')
        self.extra = sqlite3.connect('extra.db')
        self.info = sqlite.connect('infor.db')
        self.e = self.extra.cursor()
        self.c = self.connect.cursor()
        self.inf = self.info.cursor()

        self.ordernum = 0
        self.date = time.strftime("%d:%m:%Y")
        self.time = time.strftime("%H:%M:%S")
        try:
            self.c.execute("CREATE TABLE stocks(ordernum integer, date text,time text,size text,side text,topping text,amount integer, prize integer)") # Create Table if it not excite
            self.e.execute("CREATE TABLE extra(ordernum integer,Sausage&Pepperonee integer,Beef integer,Bacon integer,Peperone integer,Champignon integer,Pork integer,Shrimp integer,Onion integer,Octopus integer,Shrimp integer,Cheese integer,Tomato integer,'Pineapple integer")
            self.inf.execute("CREATE TABLE contrac(ordernum integer,name text,phone text,addr text")
        except:
            self.ordernum = self.c.execute('SELECT max(ordernum) FROM stocks')
            #load ordernum

    def insert(self, data1,data2,data3):
        self.c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?,?,?)', data1)
        self.e.executemany('INSERT INTO extra VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',data2)
        self.inf.executemany('INSERT INTO contrac VALUES (?,?,?,?)',data3)

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
                return true
            return false
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