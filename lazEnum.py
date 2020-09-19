import os
import sys

buff = ''

def parseArgs(target):
    if len(sys.argv) != 2:
        print('Aight, what\'re you doin? Directions were very simple. Let\'s break it down Barney-style I guess..\n    Usage: python ./lazEnum [ip/url]')
        exit()
    elif target == "-h" or target == "--help":
        print('So, there isn\'t really a help menu for this program because it\'s really not that complicated..\n    Usage: python ./lazEnum [ip/url]')
        exit()
    elif not target.isdigit():
        if target[0:5] == 'http:':
            cmd = 'nslookup ' + target[7:]
            os.system(cmd)
            return target[7:]
        elif target[0:6] == 'https:':
            cmd = 'nslookup ' + target[8:]
            os.system(cmd)
            return target[8:]
        else:
            cmd = 'nslookup ' + target
            os.system(cmd)
            return target
    else:
        return target

def checkReachability(target):
    buff += 'Starting a test for ' + target + '\n'
    print('\nWelcome to lazEnum! Let\'s start with a ping check to see if this shit is even reachable first yeh?\n')
    cmd = 'ping -w 3 ' + target
    x = os.system(cmd)
    if x == 512:
        print('Exiting because that IP is wack yo.')
        buff += 'Target unreachable\n'
        exit()
    elif x == 256:
        print('Is your refridgerator running? Because that IP is not. Server down!')
        buff += 'Target unreachable\n'
        exit()
    else:
        print('\nSick! The server at that IP is up and running. Let\'s do a port scan. This part may take ages. Trust the system..\n')
        buff += 'Target reachable'

def scanForOpenPorts(target):
    cmd1 = 'nmap -sV -sC -Pn -A ' + target + ' > lazEnumResultsForIP' + target + '.txt'
    x = os.system(cmd1)
    cmd2 = 'cat lazEnumResultsForIP' + target + '.txt'
    y = os.system(cmd2)

def dynamicallyEnumPorts(portsFound, target):
    if 80 in portsFound:
        print('\nSince port 80 is open, lets do a dictionary attack to see if any subdirectories are accessible!')
        cmd = 'gobuster -u http://' + target + ' -w ./resources/directory-list-2.3-medium.txt -x php -t 20 -o output.txt'
        os.system(cmd)
    if 22 in portsFound:
        print('\nSSH is open on port 22 so be looking for usernames and passwords.')

def addListToBuff(listOfItems):
    buff += 'Found the following ports open:\n'
    tempBuff = ''
    for item in listOfItems:
        tempBuff += ' ' + str(item) + ','
    buf += tempBuff[0:(len(tempBuff) - 1)]

def assessPortScan(target):
    portsFound = []
    fn = 'lazEnumResultsForIP' + target + '.txt'
    f = open(fn, "r")
    for line in f:
        if line[0].isdigit():
            tmp = ""
            curr = 0
            while line[curr].isdigit():
                tmp += line[curr]
                curr += 1
            portsFound.append(int(tmp))
    addListToBuff(portsFound)
    dynamicallyEnumPorts(portsFound, target)

def showResults():
    print(buff)

def main():
    target = parseArgs(sys.argv[1])
    checkReachability(target)
    scanForOpenPorts(target)
    assessPortScan(target)
    showResults()

if __name__ == "__main__":
    main()
