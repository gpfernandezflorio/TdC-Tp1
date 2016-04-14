import sys
from scapy.all import *

def monitor_callback(pkt):
	print pkt.show()

if __name__ == '__main__':
	if len(sys.argv) > 1:
		to = int(sys.argv[1]);
	else:
		to = 10
	print to

	sniff(prn=monitor_callback, timeout=to)
