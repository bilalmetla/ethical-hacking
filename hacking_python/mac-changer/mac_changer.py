#!/usr/bin/python3
# coding: latin-1

import subprocess
import optparse
import re

parser = optparse.OptionParser()

def change_mac(interface, new_mac_address):
    print("[+] changing mac address " + interface + " to " + new_mac_address)
    subprocess.call("ifconfig", shell=True);
    subprocess.call("ifconfig " + interface + " down", shell=True);
    subprocess.call("ifconfig  " + interface + " hw ether " + new_mac_address, shell=True);
    subprocess.call("ifconfig  " + interface + " up", shell=True);
    subprocess.call("ifconfig", shell=True);

def add_options():
    parser.add_option("-i", "--interface", dest="interface", help="Enter the enterface to change mac address")
    parser.add_option("-m", "--mac", dest="new_mac_address", help="Enter a new mac address")

def get_options():
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify interface")
    elif not options.new_mac_address:
        parser.error("[-] please specify new mac")

    return options


def check_mac_changed(interface):
    ifconfig_output = subprocess.check_output(["ifconfig", interface])
    #print(ifconfig_output)
    reg_rule = "\w\w:\w\w:\w\w:\w\w:\w\w:\w\w"
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_output))
    return mac_address_search_result.group(0)
    pass




# interface = options.interface #  input(“enter interface > ”);
# new_mac_address = options.new_mac_address #  input(“enter new mac address > ”);

add_options()
options = get_options()
change_mac(options.interface, options.new_mac_address)
current_mac = check_mac_changed(options.interface)

if current_mac == options.new_mac_address:
    print("[+] succesfully changed mac address to " + current_mac)
else :
    print("[-] could not update mac address")
