import sqlite3
import time

class SQL:
    def __init__(self):
        self.connect = sqlite3.connect('stocks.db')
        self.c = self.connect.cursor()
        
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
            self.c.execute("CREATE TABLE extra(ordernum integer,SausagePepperonee text,Beef text,Bacon text,Peperone text,Champignon text,Pork text,Onion text,Octopus text,Shrimp text,Cheese text,Tomato text,Pineapple text)")
        except:
            pass
        try:
            self.c.execute("CREATE TABLE contrac(ordernum integer,name text,phone text,addr text)")
        except:
            pass
        try:
            self.c.execute("CREATE TABLE status(ordernum integer,sta text,username text)")
        except:
            pass
        try:
            self.c.execute("CREATE TABLE account(username text,password text)")
        except:
           pass
        try:
            self.c.execute("CREATE TABLE adress(username text,name text,phone text,addr text)")
        except:
            pass

    def userexit(self,user):
        tmp = []
        for i in self.c.execute("SELECT username FROM account WHERE username = '"+user+"'"):
            tmp.extend(i)
        return len(tmp)!=0

    def registor(self,user,passw):
        if not(self.userexit(user)):
            self.c.execute('INSERT INTO account VALUES(?,?)',(user,passw))
            self.c.execute('INSERT INTO adress VALUES(?,?,?,?)',(user,"","",""))
            self.connect.commit()
            return 'T'
        return 'F'

    def login(self,user,passw):
        tmp = []
        for i in self.c.execute("SELECT username, password FROM account WHERE username = '"+user+"'"):
            tmp.extend(i)

        if(len(tmp)!=0):
            if(user == tmp[0] and passw == tmp[1]):
                exp = []
                for i in self.c.execute("SELECT name ,phone, addr FROM adress WHERE username = '"+user+"'"):
                    exp.extend(i)
                exp2 = ""
                for i in exp:
                    exp2+=str(i)
                    exp2+="<>"
                return exp2
        return 'F'

    def getmanyinfo(self, user):
        tmp = ""
        for i in self.c.execute("SELECT ordernum,sta FROM status WHERE username ='"+user+"'ORDER BY ordernum DESC LIMIT 3"):
            for j in i:
                tmp+=str(j)
                tmp+="?"
        return tmp
        


    def insert(self, data1,data2,data3,data4):
        print(data1)
        print(data2)
        print(data3)
        print(data4)

        self.c.execute('INSERT INTO stocks VALUES (?,?,?,?,?,?,?,?)', tuple(data1))
        self.c.execute('INSERT INTO extra VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',tuple(data2))
        self.c.execute('INSERT INTO contrac VALUES (?,?,?,?)',tuple(data3))
        self.c.execute('INSERT INTO status VALUES (?,?,?)',tuple(data4))
        self.c.execute("UPDATE adress SET name = '"+data3[1]+"' , phone = '"+data3[2]+"' ,addr = '"+data3[3]+"' WHERE username = '"+data4[2]+"'")

        self.connect.commit()

    def getrow(self,date):
        statement = 'SELECT * FROM stocks,extra,contrac,status WHERE stocks.ordernum = extra.ordernum AND stocks.ordernum = contrac.ordernum AND stocks.ordernum = status.ordernum AND stocks.date ='+date
        tmp =[]
        for row in self.c.execute(statement):
            tmp2 = []
            for i in row:
                tmp2.append(i)
            tmp2.pop()
            tmp2.pop(25)
            tmp2.pop(21)
            tmp2.pop(8)
            tmp.append(tmp2)
        return tmp

    def setStatus(self, ordernum, status):
        statement = "UPDATE status SET sta = '"+status+"' WHERE ordernum = "+ordernum 
        self.c.execute(statement)
        self.connect.commit()

    def decode(self,text):
        if(text.startswith("O")):
            tmp = text.split('<>')
            self.date = time.strftime("%d%m%Y")
            self.time = time.strftime("%H%M%S")
            print(len(tmp),tmp)
            if (len(tmp) == 22):
                stoc = tmp[1:6]
                extra = tmp[6:18]
                addr = tmp[18:-1]
                self.ordernum+=1
                stoc.insert(0,self.ordernum)
                stoc.insert(1,self.date)
                stoc.insert(2,self.time)
                extra.insert(0,self.ordernum)

                addr.insert(0,self.ordernum)

                status = [self.ordernum,"Cooking",tmp[-1]]
                self.insert(stoc,extra,addr,status)
                return str(self.ordernum)
            return 'F'
        elif(text.startswith("C")):
            num = int(text[1:])
            x =[]
            for i in self.c.execute('SELECT sta FROM status WHERE ordernum ='+str(num)):
                x.extend(i)

            if len(x)==0 :
                return 'N'
            return x[0]
        elif(text.startswith("L")):
            tmp = text.split('?')
            print(tmp)
            return self.login(tmp[1],tmp[2])

        elif(text.startswith("R")):
            tmp = text.split('?')
            return self.registor(tmp[1],tmp[2])
        elif(text.startswith("M")):
            return self.getmanyinfo( text[1:])
        else:
            return str(1234)

            
    def getnumber(self):
        return self.ordernum

    def read(self,date):
        return self.c.execute('select * from stocks where date = '+date)

if __name__ == '__main__':
    sl = SQL()
    print (sl.getrow('24052014'))
    print(sl.registor("x","y"))
    
    
