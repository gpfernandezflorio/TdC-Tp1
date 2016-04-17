set terminal png
set output 'home-eth-10Protocolos.png'

set style fill solid 0.5
set ylabel 'Cantidad de paquetes'

set xlabel 'Tipo de protocolo'
plot 'home-eth-10Protocolos.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+2000):2 with labels title ''

set output 'home-eth-10IpsSrcArp.png'
set xlabel 'IP emisor del paquete'
plot 'home-eth-10IpsSrcArp.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+2):2 with labels title ''

set output 'home-eth-10IpsDstArp.png'
set xlabel 'IP destinatario del paquete'
plot 'home-eth-10IpsDstArp.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+1):2 with labels title ''
