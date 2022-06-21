import server

sm = server.server("localhost", 2401)


#sm.sndStr(input("Message: \n"))


while True:
    print(sm.recvMsg())