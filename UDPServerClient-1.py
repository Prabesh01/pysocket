import threading
from socket import *

cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
cs.bind(('0.0.0.0', 1234))

def  send():
    print('Ready to send..')
    while True:
        try:
            data=input()
            cs.sendto( str(data).encode('ascii'), ('127.0.0.1', 4321))
        except KeyboardInterrupt:
            break
            
def recv():
    print('Listening..')
    while True:
        try:
            m=cs.recvfrom(4096)
            print(m[1][0]+':'+str(m[1][1])+' -> '+m[0].decode("utf-8") )
        except KeyboardInterrupt:
            break


threading.Thread(target=send).start()
threading.Thread(target=recv).start()