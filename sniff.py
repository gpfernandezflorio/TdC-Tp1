#Version 1
#! /usr/bin/env python
from scapy.all import *

def monitor_callback(pkt):
	print pkt.show()

if __name__ == '__main__':
	sniff(prn=monitor_callback, filter="arp", store=0)

#Version 2

#from scapy.all import *

#print sniff(filter="arp",count=10).summary()
