#Version 1 Slides clase
#! /usr/bin/env python
#from scapy.all import *

#def monitor_callback(pkt):
#	print pkt.show()

#if __name__ == '__main__':
#	sniff(prn=monitor_callback, filter="arp", store=0)

#Version 2 template
#from scapy.all import *

#print sniff(filter="arp",count=10).summary()

#Version 3 Editando la version 1
#! /usr/bin/env python
from scapy.all import *
from collections import *
import math
import matplotlib.pyplot as plt
from numpy.random import normal

#def monitor_callback(pkt):
#	print pkt.show()

if __name__ == '__main__':
	l = []
	packets = [{"t":"eth"},{"t":"arp"},{"t":"arp"},{"t":"eth"},{"t":"lan"},{"t":"arp"}]#sniff(prn=monitor_callback, filter="arp", store=0, timeout=10)

	cantPaquetes = 0.0
	for p in packets:
		cantPaquetes = cantPaquetes +1.0
		l.append(p["t"]) #p.type

	cantidades = Counter(l)
	print cantidades
	print cantidades.keys()
	prob = map(lambda x: cantidades[x]/cantPaquetes, cantidades.keys())
	print prob

	entropia = 0
	for p in prob:
		entropia = entropia - (p * math.log(p,2.0))
	print entropia

	#plt.hist(cantidades)
	#plt.hist(l)
	#plt.title("Cantidades")
	#plt.xlabel("Tipo")
	#plt.ylabel("Cantidad")
	#plt.show()
