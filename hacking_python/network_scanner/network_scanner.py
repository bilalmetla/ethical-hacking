#!/usr/bin/python3


import scapy.all as scapy
#import optparse
import argparse

#parser = optparse.OptionParser()
parser = argparse.ArgumentParser()


def scan_basic (ip):
    #scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    #scapy.ls(arp_request)
    #arp_request.pdst = ip
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(broadcast)
    arp_request_broadcast = broadcast / arp_request
    print(arp_request.summary())
    print(broadcast.summary())
    print(arp_request_broadcast.summary())
    #show each packet details
    arp_request.show()
    broadcast.show()
    arp_request_broadcast.show()
    
    pass

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    #(answered, unanswered) = scapy.srp(arp_request_broadcast, timeout=1) # srp allow to send custom ether part
    (answered, unanswered) = scapy.srp(arp_request_broadcast, timeout=1, verbose=False) # srp allow to send custom ether part
    #print(answered.summary())    

   
    clients_lists = []
    for element in answered:
        # print(element[0].show())
        # print(element[1].show())
        #print(element[1].psrc + "\t\t" + element[1].hwdst)
        clients_lists.append({
            "ip": element[1].psrc,
            "mac": element[1].hwdst
        })
    return clients_lists


def print_scan(result):
    print('--------------------------------------------')
    print("IP\t\t\tMac Address")
    print('--------------------------------------------')
    for element in result:
        print(element['ip'] + "\t\t" + element["mac"])
    pass


def add_input_options():
   parser.add_argument("-t", "--target", dest="target", help="enter ip or ip range")
   pass

def get_input_options():
    #(options, arguments) = parser.parse_args()
    options = parser.parse_args()
    return options

#main program
add_input_options()
input_options = get_input_options()
if not input_options.target:
    print("[-] IP or IP range is required")
else:
    scan_result = scan(input_options.target)
    print_scan(scan_result)