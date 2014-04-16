import sqlite3
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
    def __init__ (self):
        self.connect = sqlite3.connect('example.db')
        self.c = self.connect.cursor()
        self.ordernum=0
        self.time = int(time.strftime("%d%m%Y"))
        try:
            self.c.execute("CREATE TABLE stocks(date integer, ordernum integer, size text)") # Create Table if it not excite
        except:
            pass
            #load ordernum

    def insert(self, data):
        self.c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', data)
        self.connect.commit()

    def printrow(self,statement):
        for row in self.c.execute(statement):
            print(row)

    def decode(self,text):
        pass
        insert()

    def getnumber(self):
        self.ordernum+=1
        return self.ordernum

if __name__ == '__main__':
    sl = SQL()
    purchases = [('20012-03-28', 'BUY', 'Microsoft', 1000, 45.00),
             ('2011-03-05', 'BUY', 'Bata', 1000, 72.00),
             ('2007-04-06', 'SELL', 'fdd', 500, 53.00),
            ]
    #sl.insert(purchases)
    sl.printrow('SELECT * FROM stocks ORDER BY date')
    sl.c.close()