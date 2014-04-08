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
        try:
            self.c.execute('''CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)''') # Create Table if it not excite
        except:
            pass
if __name__ == '__main__':
    sl = SQL()
    sl.c.close()