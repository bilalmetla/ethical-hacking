#!/usr/bin/python3


import scapy.all as scapy

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
    pass

def process_sniffed_packet(packet):
    print(packet)
    pass

interface = "eth0"
sniff(interface)