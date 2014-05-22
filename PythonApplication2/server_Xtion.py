import socket
import sys
import threading
 
import SQL

PORT = 21567 # the port number to run our server on
__version__ = "0.0.1"
 
class Server_connection():
    
    def __init__(self, port, host='localhost'):
        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.users = {} # current connections
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

        
        
        try:
            self.server.bind((self.host, self.port))
        except socket.error:
            print('Bind failed %s' % (socket.error))
            sys.exit()
 
        self.server.listen(10)
        
    # Not currently used.  Ensure sockets are closed on disconnect
    def exit(self):
        self.server.close()
 
    def run_thread(self, conn, addr):
        print('Client connected with ' + addr[0] + ':' + str(addr[1]))
        while True:
            try:
                self.SL = SQL.SQL() #SQL
                data = (conn.recv(1024)).decode("utf-8")
                
                conn.sendall((self.SL.decode(data)).encode("utf-8")) # send order number back to custommer
                #conn.sendall('1234'.encode("utf-8")) # send order number back to custommer

            except (ConnectionError):
                print('Connection Error/Close')
                break
        conn.close() # Close
 
    def run(self):
        print('Waiting for connections on port %s' % (self.port))
        # We need to run a loop and create a new thread for each connection
        while True:
            conn, addr = self.server.accept()
            threading.Thread(target=self.run_thread, args=(conn, addr)).start()
 
  
if __name__ == '__main__':
    
    server = Server_connection(PORT)
    server.run()
 
