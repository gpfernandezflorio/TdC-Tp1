set terminal png
set output 'shopping-wifi-600Protocolos.png'

set style fill solid 0.5
set ylabel 'Cantidad de paquetes'

set xlabel 'Tipo de protocolo'
plot 'altop600Protocolos.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+2000):2 with labels title ''

set output 'altop600IpsSrcArp.png'
set xlabel 'IP emisor del paquete'
plot 'altop600IpsSrcArp.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+2):2 with labels title ''

set output 'altop600IpsDstArp.png'
set xlabel 'IP destinatario del paquete'
plot 'altop600IpsDstArp.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+1):2 with labels title ''
