import socket
import sys

try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print('Failed to create socket')
    print("Reason: "+str(err))
    sys.exit()
print('socket created')

target_host='python.org'
target_port='80'

try:
    sock.connect((target_host,int(target_port)))
    print(f"connectted to {target_host}:{target_port}")
    sock.shutdown(2)
except socket.error as err:
    print('failed to connect to %s on port %s'%(target_host,target_port))
    print("Reason: "+str(err))
    sys.exit()
