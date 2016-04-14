import sys
from scapy.all import *
from collections import *
import math
import matplotlib.pyplot as plt

protocolos = []
ips_src_arp = []
ips_dst_arp = []
cantProtocolos = 0.0
cantIpsSrcArp = 0.0
cantIpsDstArp = 0.0

def imprime_salida(counter, file_name_prefix, file_name_suffix):
  f = open('../mediciones/' + file_name_prefix + file_name_suffix + '.txt', 'w')
  map(lambda x: imprimir(f,counter,x), counter)

def imprimir(file, counter, key):
  file.write(str(key) + "\t" + str(counter[key]) + "\n")

def map_number_to_name(type_int):
  try:
    ret = {
      0x0800: 'IPv4',
      0x0806: 'ARP',
      0x0842: 'WakeOn LAN',
      0x22F3: 'IETF TRILL',
      0x6003: 'DECnet',
      0x8035: 'RARP',
      0x809B: 'Ethertalk',
      0x80F3: 'AARP',
      0x8100: '802.1Q',
      0x8137: 'IPX',
      0x8204: 'QNX Qnet',
      0x86DD: 'IPv6',
      0x8808: 'EFC',
      0x8819: 'CobraNet',
      0x8847: 'MPLS Unicast',
      0x8848: 'MPLS Multicast',
      0x8863: 'PPPoE Discovery',
      0x8864: 'PPPoE Session',
      0x8870: 'Jumbo',
      0x887B: 'HomePlug 1.0',
      0x888E: '802.1X',
      0x8892: 'PROFINET',
      0x889A: 'SCSI',
      0x88A2: 'ATA',
      0x88A4: 'EtherCAT',
      0x88A8: '802.1ad',
      0x88AB: 'Powerlink',
      0x88CC: 'LLDP',
      0x88CD: 'SERCOS III',
      0x88E1: 'HomePlug AV',
      0x88E3: 'MRP',
      0x88E5: 'MAC security',
      0x88E7: 'PBB',
      0x88F7: 'PTP',
      0x8902: 'CFM',
      0x8906: 'FCoE',
      0x8914: 'FCoE Init',
      0x8915: 'RoCE',
      0x891D: 'TTE',
      0x892F: 'HSR',
      0x9000: 'ECTP'
    }[type_int]
  except:
    ret = 'Other(' + str(type_int) + ')'
  return ret

def monitor_callback(pkt):
  global cantProtocolos
  global protocolos
  global cantIpsSrcArp
  global ips_src_arp
  global cantIpsDstArp
  global ips_dst_arp
  try:
    current_type = pkt.type
  except:
    # Asumimos que el type 0 no se usa y lo usamos para los casos que
    # nos vienen sin type, como por ejemplo STP
    pkt.show()
    current_type = 0x0000
  cantProtocolos = cantProtocolos + 1.0

  protocolos.append(map_number_to_name(current_type))
  if pkt.haslayer(ARP): # Sera lo mismo que 'if ARP in pkt:'?
    ips_src_arp.append(pkt[ARP].psrc)
    cantIpsSrcArp += 1.0
    ips_dst_arp.append(pkt[ARP].pdst)
    cantIpsDstArp += 1.0

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

  sniff(prn=monitor_callback, timeout=to)

  protocolosCounter = Counter(protocolos)
  ipsSrcArpCounter = Counter(ips_src_arp)
  ipsDstArpCounter = Counter(ips_dst_arp)
  print protocolosCounter
  print ipsSrcArpCounter
  print ipsDstArpCounter

  probProtoclos = map(lambda x: protocolosCounter[x]/cantProtocolos, protocolosCounter.keys())

  entropiaProtocolos = 0.0
  for p in probProtoclos:
    entropiaProtocolos = entropiaProtocolos - (p * math.log(p,2.0))
  print "entropia de los protocolos: " + str(entropiaProtocolos)

  probIpsSrcArp = map(lambda x: ipsSrcArpCounter[x]/cantIpsSrcArp, ipsSrcArpCounter.keys())

  entropiaIpsSrcArp = 0.0
  for p in probIpsSrcArp:
    entropiaIpsSrcArp = entropiaIpsSrcArp - (p * math.log(p,2.0))
  print "entropia de las IPs origen de ARP: " + str(entropiaIpsSrcArp)

  probIpsDstArp = map(lambda x: ipsDstArpCounter[x]/cantIpsDstArp, ipsDstArpCounter.keys())

  entropiaIpsDstArp = 0.0
  for p in probIpsDstArp:
    entropiaIpsDstArp = entropiaIpsDstArp - (p * math.log(p,2.0))
  print "entropia de las IPs destino de ARP: " + str(entropiaIpsDstArp)

  imprime_salida(protocolosCounter, file_name_prefix, 'Protocolos')
  imprime_salida(ipsSrcArpCounter, file_name_prefix, 'IpsSrcArp')
  imprime_salida(ipsDstArpCounter, file_name_prefix, 'IpsDstArp')

