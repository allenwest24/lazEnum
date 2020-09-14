import os
import sys

def parseArgs():
    if len(sys.argv) != 2:
        print('Aight, what\'re you doin? Directions were very simple. Let\'s break it down Barney-style I guess..\n    Usage: python ./lazEnum [ip/url]')
        exit()
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print('So, there isn\'t really a help menu for this program because it\'s really not that complicated..\n    Usage: python ./lazEnum [ip/url]')
        exit()

def checkReachability():
    print('\nWelcome to lazEnum! Let\'s start with a ping check to see if this shit is even reachable first yeh?\n')
    cmd = 'ping -w 3 ' + sys.argv[1]
    x = os.system(cmd)
    if x == 512:
        print('Exiting because that IP is wack yo.')
        exit()
    elif x == 256:
        print('Is your refridgerator running? Because that IP is not. Server down!')
        exit()
    else:
        print('\nSick! The server at that IP is up and running. Let\'s do a port scan. This part may take ages. Trust the system..\n')

def scanForOpenPorts():
    cmd = 'nmap -sV -sC -Pn -A ' + sys.argv[1]
    x = os.system(cmd)

def main():
    parseArgs()
    checkReachability()
    scanForOpenPorts()


if __name__ == "__main__":
    main()

