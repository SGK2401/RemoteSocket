import client
from threading import Thread


cm = client.client("localhost", 2401)

print(cm.recvStr())
cm.sendMsg("123")