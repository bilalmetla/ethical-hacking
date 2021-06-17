import socket
from colorama import Fore

#color as a global variable
GREE = Fore.GREEN
GRAY = Fore.LIGHTBLACK_EX
RESET = Fore.RESET

# define port scanner
def portScanner(host, port):
    sock = socket.socket()
    try:
        sock.connect({host, port})
        sock.settimeout(0.2)
    except:
        return False
    else:
        return True

def runner():
    try:
        print("starting runner ....")
        host = input("please enter the host to scan:")
        for port in range(1,1000):
            if(portScanner(host, port)):
                #print("{GREEN}{+}The port {port} was open on {host}! {RESET}")
                print("port is open: %s" % port)
            #else:
                #print("{GRAY}{-}Port is closed!{RESET}", end="\r")
               # print("port is closed %s" % port)
    except:
        print("exception happened")


#if __name__ == "__man__":
runner()
    

