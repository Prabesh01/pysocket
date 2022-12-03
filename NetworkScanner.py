# pip install scapy 
# install winpcap: https://npcap.com/

from socket import *
from scapy.all import ARP, Ether, srp
import sys
import  ipaddress

def scan():
    global clients
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    print("=========================================")
    print("IP\t\t\tMAC Address\n=========================================")        
    for sent, received in result:
        print(f'{received.psrc}\t\t{received.hwsrc}')
    print("=========================================")
    print(f'Discovered {len(result)} devices on network.')

try:
    hostname = getfqdn()
    mahip=gethostbyname_ex(hostname)[2][1] # import scapy.config scapy.route: scapy.config.conf.route.routes[0][2]
except:
    print('Couldn\'t obtain IP address')
    sys.exit()

target_ip = str(ipaddress.ip_network(mahip+'/255.255.255.0', strict=False)) #192.168.1.1/24

scan()