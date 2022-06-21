import socket, time, json, os

class client:
    def __init__(self, host="localhost", port=24010):
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
    
    def jsonFile(self, file):
        try:
            return json.load(open(file, mode="r", encoding="utf-8"))
        except FileNotFoundError:
            print("File not found!")
    
    def keyMatch(self, key, dict):
        if key in dict:
            return dict[key]
        else:
            print("No matching key")
    
    def execute(self, target):
            os.startfile(target)
    
    def sendMsg(self, msg):
        try:
            self.m = socket.socket()
            self.m.connect(self.con)
            self.m.send(msg.encode("utf=8"))
        except ConnectionRefusedError:
            print("Connection failed.")
        except not ConnectionRefusedError:
            print("Unexpected exception!")
            raise