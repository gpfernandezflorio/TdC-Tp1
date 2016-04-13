import sys
from scapy.all import *
from collections import *
import math
import matplotlib.pyplot as plt

def imprime_entrada(x, cantidades):
  print (x + ' ' + str(cantidades[x]))

def imprime_salida(counter, file_name_prefix, file_name_suffix):
  f = open('mediciones/' + file_name_prefix + file_name_suffix + '.txt', 'w')
  map(lambda x: imprimir(f,counter,x), counter)

def imprimir(file, counter, key):
  file.write(str(key) + "\t" + str(counter[key]))

if __name__ == '__main__':
  if len(sys.argv) == 3:
    file_name_prefix = sys.argv[1]
    to = int(sys.argv[2])
  elif len(sys.argv) == 2:
    file_name_prefix = sys.argv[1]
    to = 10
  else:
    print 'Se debe pasar como minimo nombre del archivo de salida y opcionalmente el timeout'
    sys.exit()
  protocolos = []
  ips_arp = []
  packets = sniff(timeout=to)

  cantProtocolos = 0.0
  cantIpsArp = 0.0
  for p in packets:
    try:
      current_type = p.type
    except:
      # Asumimos que el type 0 no se usa y lo usamos para los casos que
      # nos vienen sin type, como por ejemplo STP
      current_type = 0x0000
    cantProtocolos = cantProtocolos + 1.0

    protocolos.append(current_type)
    if p.haslayer(ARP):
      ips_arp.append(p[ARP].psrc)
      cantIpsArp += 1.0


  protocolosCounter = Counter(protocolos)
  ipsArpCounter = Counter(ips_arp)
  print ipsArpCounter
  print protocolosCounter

  probProtoclos = map(lambda x: protocolosCounter[x]/cantProtocolos, protocolosCounter.keys())

  entropiaProtocolos = 0
  for p in probProtoclos:
    entropiaProtocolos = entropiaProtocolos - (p * math.log(p,2.0))
  print "entropia de los protocolos: " + str(entropiaProtocolos)

  probIpsArp = map(lambda x: protocolosCounter[x]/cantProtocolos, protocolosCounter.keys())

  entropiaIpsArp = 0
  for p in probIpsArp:
    entropiaIpsArp = entropiaIpsArp - (p * math.log(p,2.0))
  print "entropia de las IPs de ARP: " + str(entropiaIpsArp)

  imprime_salida(protocolosCounter, file_name_prefix, 'Protocolos')
  imprime_salida(ipsArpCounter, file_name_prefix, 'IpsArp')

