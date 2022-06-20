import client
from threading import Thread


cm = client.client("cn-sx-bgp-2.natfrp.cloud", 24010)

while True:
    print(cm.recvStr(3))