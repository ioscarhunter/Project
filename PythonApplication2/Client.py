import socket
# Simple chat client that allows multiple connections via threads
PORT = 21567 # the port number to run our server on
class ChatClient(object):
 
    def __init__(self, port, host='localhost'):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              
    def check_server(self):
         
        try:
            self.socket.connect((self.host, self.port))
        except ConnectionRefusedError:
           print("error")
           return False
        return True

    def send_message(self, msg):
        if(self.check_server()):
            self.socket.send(msg.encode("utf-8"))
            s = self.socket.recv(1024).decode("utf-8")
            if(s == "complete"):
                print("ohyeah")
            else : print(s)
            self.close_connection()
        else : return False
        

    def close_connection(self):
        self.socket.close()

  
if __name__ == '__main__':
 
    # Send a message to the chat server
 
    client = ChatClient(PORT)
    client.send_message("Hello")
