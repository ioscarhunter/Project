import SQL
import server_Xtion
PORT = 21567 # the port number to run our server on
class Server :
    def __init__ (self):
        self.con = server_Xtion.ChatServer(PORT) #connection
        self.con.run()
        
        self.SL = SQL() #SQL


    def refresh(self,date):#dateformate %d%m%Y integer
        self.SL.read('''statement''')
s = Server()