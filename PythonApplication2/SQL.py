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
        self.date = time.strftime("%d%m%Y")
        self.time = time.strftime("%H%M%S")
        try:
            self.c.execute("CREATE TABLE stocks(ordernum integer, date text,time text,size text,side text,topping text,amount text, prize text)") # Create Table if it not excite
            
        except:
            tmp =[]
            for i in self.c.execute('SELECT max(ordernum) FROM stocks'):
                tmp.extend(i)
            
            if(tmp !=[None]):
                self.ordernum = int(tmp[0])
            #load ordernum
        try:
            self.e.execute("CREATE TABLE extra(ordernum text,SausagePepperonee text,Beef integer,Bacon text,Peperone text,Champignon text,Pork text,Onion text,Octopus text,Shrimp text,Cheese text,Tomato text,Pineapple text)")
        except:
            pass
        try:
            self.inf.execute("CREATE TABLE contrac(ordernum integer,name text,phone text,addr text)")
        except:
            pass
        try:
            self.st.execute("CREATE TABLE status(ordernum integer,sta text)")
        except:
            pass
        print("complete")

    def insert(self, data1,data2,data3,data4):
        print(data1)
        print(data2)
        print(data3)
        print(data4)

        self.c.execute('INSERT INTO stocks VALUES (?,?,?,?,?,?,?,?)', tuple(data1))
        self.e.execute('INSERT INTO extra VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',tuple(data2))
        self.inf.execute('INSERT INTO contrac VALUES (?,?,?,?)',tuple(data3))
        self.st.execute('INSERT INTO status VALUES (?,?)',tuple(data4))

        self.connect.commit()
        self.extra.commit()
        self.info.commit()

    def printrow(self,statement):
        for row in self.c.execute(statement):
            print(row)

    def decode(self,text):
        if(text.startswith("O")):
            print("x")
            tmp = text.split('<>')
            self.date = time.strftime("%d%m%Y")
            self.time = time.strftime("%H%M%S")
            if (len(tmp) == 21):
                stoc = tmp[1:6]
                extra = tmp[6:18]
                addr = tmp[18:]
                self.ordernum+=1
                stoc.insert(0,self.ordernum)
                stoc.insert(1,self.date)
                stoc.insert(2,self.time)
                extra.insert(0,self.ordernum)

                addr.insert(0,self.ordernum)

                status = [self.ordernum,"Cooking"]
                self.insert(stoc,extra,addr,status)
                return str(self.ordernum)
            return 'F'
        elif(text.startswith("C")):
            num = int(text[1:])
            x =[]
            for i in self.s.execute('SELECT status FROM st WHERE ordernum ='+num):
                x.extend(i)

            if len(x)==0 :
                return 0
            return x[0]
        else:
            return str(1234)

            
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
