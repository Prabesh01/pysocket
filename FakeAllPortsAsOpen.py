#!/usr/bin/env python3
from scapy.all import *
import os
import platform

if platform.system() == 'Windows':
    os.system("netsh advfirewall firewall add rule name='Block RST packets' dir=out protocol=TCP remoteport=1-65535 tcpflags=RST action=block")
else:
    os.system("iptables -A OUTPUT -p tcp -o wlan0 --sport 1:65535 --tcp-flags RST RST -j DROP")

def packet(pkt):
    if pkt[TCP].flags == 2:
        print(f'SYN packet detected port : {str(pkt[TCP].sport)} from IP Src : {pkt[IP].src}')
        send(IP(dst=pkt[IP].src, src=pkt[IP].dst)/TCP(dport=pkt[TCP].sport, sport=pkt[TCP].dport,ack=pkt[TCP].seq + 1, flags='SA'))

while True:
    sniff(iface="wlan0", prn=packet, filter="tcp[0xd]&18=2", count=100)

if platform.system() == 'Windows':
    os.system("netsh advfirewall firewall delete rule name='Block RST packets'")
else:
    os.system("iptables -D OUTPUT -p tcp -o wlan0 --sport 1:65535 --tcp-flags RST RST -j DROP")
