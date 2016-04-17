import sys
from scapy.all import *
from collections import *
import math
import matplotlib.pyplot as plt

def monitor_callback(pkt):
  print pkt.show()

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

if __name__ == '__main__':
  if len(sys.argv) > 1:
    to = int(sys.argv[1]);
  else:
    to = 10
  l = []
  packets = sniff(timeout=to)

  cantPaquetes = 0.0
  for p in packets:
    try:
      current_type = p.type
    except:
      # Asumimos que el type 0 no se usa y lo usamos para los casos que
      # nos vienen sin type, como por ejemplo STP
      monitor_callback(p)
      current_type = 0x0000
    cantPaquetes = cantPaquetes +1.0
    l.append(map_number_to_name(current_type))

  cantidades = Counter(l)
  print cantidades
  prob = map(lambda x: cantidades[x]/cantPaquetes, cantidades.keys())

  entropia = 0
  for p in prob:
    entropia = entropia - (p * math.log(p,2.0))
  print "entropia: " + str(entropia)
