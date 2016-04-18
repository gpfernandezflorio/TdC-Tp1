set terminal png
set output 'altop10Protocolos.png'

set style fill solid 0.5
set ylabel 'Cantidad de paquetes'

set xlabel 'Tipo de protocolo'
plot 'altop10Protocolos.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+600):2 with labels title ''

set output 'altop10IpsSrcArp.png'
set xlabel 'IP emisor del paquete'
plot 'altop10IpsSrcArp.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+20):2 with labels title ''

set terminal png size 1000,480
set xtics rotate by 270

set output 'altop10IpsDstArp.png'
set xlabel 'IP destinatario del paquete'
plot 'altop10IpsDstArp.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+3):2 with labels title ''
