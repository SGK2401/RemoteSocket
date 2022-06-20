import socket, time

class client:
    def __init__(self, host, port):
        self.h = host
        self.p = port
        self.con = (host, port)
    
    def recvStr(self, timegap=0):  
        try:
            self.s = socket.socket()
            self.s.connect(self.con)
            self.RECV = self.s.recv(1024)
            self.s.close()
            return self.RECV
        except ConnectionRefusedError:
            print("Connection failed.")
        except not ConnectionRefusedError:
            print("Unexpexted exception!")
            raise
        time.sleep(timegap)
