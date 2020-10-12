# lazEnum

### Description
lazEnum is a target enumerator for the lazy hacker. When you give lazEnum a target IP or URL, it will do any DNS resolution necessary, check the IP's reachability, do a port
scan to see what ports are open, then go into further enumeration tactics depending on the type of port that is open. This is still a massive work in progress so no judging.

### Logic Map

This script is essentially the same first steps for every HackTheBox machine. I can run this script, then go make some food, and when I get back a large portion of my enumeration will be done for me. 

$ python ./lazEnum.py [ip/url] 

- Check if target is reachable
- Run a detailed port scan
- Parse the open ports
- If there is a webserver:
    - Run a directory brute force
    - Analyze results
- If there are other ports open, give specific advice.

More features to follow. 

### Issues

This program uses gobuster for brute forcing subdirectory discovery. On the newest kali release, this tool sometimes doesn't get installed. you can fix this by entering 'sudo apt-get install gobuster'.
If this returns an error about not being able to find gobuster, visit https://ourcodeworld.com/articles/read/961/how-to-solve-kali-linux-apt-get-install-e-unable-to-locate-package-checkinstall and make those changes. Should fix it!
