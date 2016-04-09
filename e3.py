from scapy.all import *
from collections import *
import math

def monitor_callback(pkt):
	print pkt.show()

if __name__ == '__main__':
	l = []
	packets = sniff(filter = "arp", timeout=2)

	cantPaquetes = 0.0
	for p in packets:
		cantPaquetes = cantPaquetes +1.0
		monitor_callback(p)
		l.append(p.hwsrc)

	cantidades = Counter(l)
	print cantidades
	prob = map(lambda x: cantidades[x]/cantPaquetes, cantidades.keys())

	entropia = 0
	for p in prob:
		entropia = entropia - (p * math.log(p,2.0))
	print "entropia: " + str(entropia)
