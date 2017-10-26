# Black Nurse DOS

### Vulnerable systems

 - Cisco ASA 5505, 5506, 5515, 5525 , 5540 (default settings)
 - Cisco 6500 routers with SUP2T and Netflow v9 on the inbound interface - 100% CPU load
 - Cisco ASA 5550 (Legacy) and 5515-X (latest generation)
 - SonicWall - Misconfiguration can be changed and mitigated (Enable Anti-DDOS)
 - Palo Alto 5050 Firewalls with firmware 7.1.4-h2 
 - Zyxel NWA3560-N (Wireless attack from LAN Side)
 - Zyxel Zywall USG50

### Tested not vulnerable

 * Iptables (Netfilter even with 480 Mbit/sec)
 * mikrotik CCR1036-12G-4S firmware: 3.27 (250 Mbit/sec) and no problem && RouterOS 5.4 on Mikrotik RB750
 * OpenBSD 6.0 and current
 * Windows Firewalls
 * pfSense
 * GigaVUE HC-Serie (Gigamon)
 * AVM Fritz!Box 7360 (common ADSl router in Germany)
 * Ubiquiti Networks - EdgeRouter Lite CPU 60-70% load but still going

## Mitigation

### Cisco ASA 5550 (Legacy) and 5515-X (latest generation) 

To mitigate this attack on Cisco routers the following commands can help

    icmp deny any unreachable outside
    icmp deny any time outside

## C compilation

    gcc exploit.c -o exploit
    ./blacknurse <target ip>

## Python Dependencies

 * Python 2.6 or 2.7
 * Scapy
 * argparse (included with Python >= 2.7 and >= 3.2)

### Scapy installation with pip

    pip install scapy

