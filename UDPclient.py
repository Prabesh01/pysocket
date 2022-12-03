import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg='oa'

while True:
    sock.sendto(msg.encode('utf-8'),('127.0.0.1',53556))
    data,addr=sock.recvfrom(4096)
    print(str(data))
    msg=input()
    if msg.lower()=='n':
        break

sock.close()