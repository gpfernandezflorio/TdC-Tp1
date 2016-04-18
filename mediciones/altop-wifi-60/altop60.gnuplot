set terminal png
set output 'altop60Protocolos.png'

set style fill solid 0.5
set ylabel 'Cantidad de paquetes'

set xlabel 'Tipo de protocolo'
plot 'altop60Protocolos.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+2700):2 with labels title ''

set output 'altop60IpsSrcArp.png'
set xlabel 'IP emisor del paquete'
plot 'altop60IpsSrcArp.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+100):2 with labels title ''

set terminal png size 2000,480
set xtics rotate by 270

set output 'altop60IpsDstArp.png'
set xlabel 'IP destinatario del paquete'
plot 'altop60IpsDstArp.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+10):2 with labels title ''
