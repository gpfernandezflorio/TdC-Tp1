import sys
from scapy.all import *
from collections import *
import math

def monitor_callback(pkt):
  print pkt.show()

if __name__ == '__main__':
  if len(sys.argv) > 1:
    to = int(sys.argv[1]);
  else:
    to = 10
  print to
  l = []
  packets = sniff(timeout=to)

  cantPaquetes = 0.0
  for p in packets:
    try:
      current_type = p.type
    except:
      # Asumimos que el type 0 no se usa y lo usamos para los casos que
      # nos vienen sin type, como por ejemplo STP
      current_type = 0x0000
    cantPaquetes = cantPaquetes +1.0
    monitor_callback(p)
    l.append(current_type)

  cantidades = Counter(l)
  print cantidades
  prob = map(lambda x: cantidades[x]/cantPaquetes, cantidades.keys())

  entropia = 0
  for p in prob:
    entropia = entropia - (p * math.log(p,2.0))
  print "entropia: " + str(entropia)
