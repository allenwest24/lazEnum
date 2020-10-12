# lazEnum

### Description
lazEnum is a target enumerator for the lazy hacker. When you give lazEnum a target IP or URL, it will do any DNS resolution necessary, check the IP's reachability, do a port
scan to see what ports are open, then go into further enumeration tactics depending on the type of port that is open. This is still a massive work in progress so no judging.

### Logic Map

$ python ./lazEnum.py [ip/url] 

### Issues

This program uses gobuster. On the newest kali release, this tool sometimes doesn't get installed. you can fix thisby entering 'sudo apt-get install gobuster'.
If this returns an error about not being able to find gobuster, visit https://ourcodeworld.com/articles/read/961/how-to-solve-kali-linux-apt-get-install-e-unable-to-locate-package-checkinstall and make those changes. Should fix it!
