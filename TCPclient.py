import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',65535))

msg='Oi'

try:
    while True:
        client_socket.send(msg.encode('utf-8'))
        data=client_socket.recv(1024)
        print(str(data.decode('utf-8')))
        msg=input()
        if msg.lower()=='n':
            break
except:
    print('Exited by the user')
client_socket.close()