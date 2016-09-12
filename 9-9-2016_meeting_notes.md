# September 9th, 2016 - CDC@UI


# Leadership for the 2016-17 term is finalized!
* President: Christopher Goes
* Vice President: Hannah Pearson
* Secretary: Animesh Pattanayak
* Treasurer: Antonius Stalick
* Sidekick: Joey Chereck


# Club Websites
* [OrgSync](https://orgsync.com/138225/chapter)
* [GitHub](https://github.com/CDC-UI)
* Facebook/Twitter TBD


# Meeting Notes
This week we went over general security concepts and terminology. 

## Terms and concepts
* CIA: Confidentiality, integrity and availability
* What are "Hackers": White, Black, Grey hats
## The Threats
* Internet Background Radiation: Automated attacks
* The real threat: financial crime (Identity theft, Ransomware)
* Malware: Worms, Viruses, Adware, Spyware, Rootkits (and mobile variants, like Angry Birds 2 fiasco)
    * (C2 server: command and control)
Attacks: Drive-by, Denial of Service (DOS), Man-in-the-middle, Brute Force, Exploits
* Exploits and Vulnerabilities 
    * SQL Injection exploit
        ```
        SELECT user FROM users WHERE '$name' == user;
        Enter Username: [' OR '1'=='1';-- ]
        SELECT user FROM users WHERE '' OR 1==1;
        ```
    * SQL Injection Mitigations: 
        * Prepared Statements
        * String escaping
        * Stored Procedures
* OWASP Top 10: 10 most common vulnerabilities in websites globally.

## Networking basics
* Hardware -> Local Link -> "TCP/IP" -> Application
* TCP/IP: IP addresses , subnets and masks, routers and gateways, "ports"
* MAC addresses, switches,
* Local Area Network (LAN) vs Wide Area Network (WAN)

## Local
* Anti-malware
    * Traditional: Hash-based checking (virustotal.com)
    * Modern: Heuristics
    * Good choices:  Avast, MalwareBytes
    * For a quick check: ProcessExplorer (Enable VirusTotal and Signature checking in settings)
* Firewalls (IP layer)
	
* Useful reference sheets for everything networking (and therefore hacking)
    * [PacketLife cheet sheets](http://packetlife.net/library/cheat-sheets/)

* Further reading
    * [CIA reading](http://whatis.techtarget.com/definition/Confidentiality-integrity-and-availability-CIA)
    * [Awesome FBI reading](https://www.fbi.gov/news/speeches/the-fbis-approach-to-the-cyber-threat)


# Future Meetings

## Next time - 9/13/2016 (I will send a reminder Monday):
Bring a laptop if you have one. If disk space is limited, bring an external HDD or a flash drive.
What we're going to do is have some fun cracking!
	Break Brett's used-in-production web app (recon + exploit)
	Password cracking 
	Possibly some network exploitation and/or recon

## The week after - 9/20/2016
Hardware! If there is something you want to do, email me or mention it at the meeting.
	Arduinos
	Old HDDs/ODDs (and possibly an SSD!)
	Anything you want to bring and pry open!
	
## Two weeks after - 9/27/2016 (Tentative)
Picklocking (Please email if you have locks)
Reverse Engineering
