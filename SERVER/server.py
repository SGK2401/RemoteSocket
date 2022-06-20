import socket


class server:
    def __init__(self, host, port):
        self.h = host
        self.p = port
        self.con = (host, port)

        self.s = socket.socket()
        self.s.bind(self.con)
        self.s.listen(5)
    
    def sndStr(self, msg):
        clientSocket, address = self.s.accept()
        clientSocket.send(msg.encode("utf-8"))
#        s.shutdown()


