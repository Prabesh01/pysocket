import socket
from _thread import *

ThreadCount=0

server_socket=socket.socket()
try:
    server_socket.bind(('127.0.0.1',65535))
except socket.error as e:
    print(str(e))

print('Server waiting for connection')

server_socket.listen(5)

def client_thread(connection):
    global ThreadCount
    connection.send(str.encode('welcome'))
    while True:
        try:
            data=connection.recv(1024)
            if not data or data.decode('utf-8')=='END':
                break
        except socket.error as e:
            print(str(e))
            ThreadCount-=1
            break
        print('Receinved from client: %s'%data.decode('utf-8'))
        try:
            connection.sendall(str.encode('welcome'))
        except:
            print("Exited by the user")
            ThreadCount-=1
            break
    connection.close()
        
    
while True:
    client_socket,addr=server_socket.accept()
    print("client connected from ", addr)
    start_new_thread(client_thread,(client_socket,))
    ThreadCount+=1
    print('ThreadCount: '+str(ThreadCount))

server_socket.close()