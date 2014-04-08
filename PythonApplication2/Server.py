import socket
import sys
import threading
 

PORT = 21567 # the port number to run our server on
__version__ = "0.0.1"
 
class ChatServer(threading.Thread):
    
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
        s = "defrog"
        while True:
            try:
                data = conn.recv(1024)
                reply = data
                print(reply.decode("utf-8")) # (bytestring.decode("utf-8") = convert byte string to str
                conn.sendall(s.encode("utf-8"))
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
    server = ChatServer(PORT)
    # Run the chat server listening on PORT
    server.run()
 