import sys
from collections import *
import math

if __name__ == '__main__':
  if len(sys.argv) == 2:
    file_name = sys.argv[1]
  else:
    print 'Se debe pasar como minimo nombre del archivo de salida y opcionalmente el timeout'
    sys.exit()

  f = open(file_name, 'r')

  counter = map(lambda x: (x.split('\t')[0], float(x.split('\t')[1].split('\n')[0])), f)
  print counter
  cant = sum(map(lambda x: x[1],counter))
  print cant
  probs = map(lambda x: x[1]/cant, counter)
  print probs

  entropia = 0.0
  for p in probs:
    entropia = entropia - (p * math.log(p,2.0))
  print "entropia: " + str(entropia)
