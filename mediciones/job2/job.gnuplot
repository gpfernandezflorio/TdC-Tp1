set terminal png
set output 'type.png'

set style fill solid 0.5
set ylabel 'Cantidad de paquetes'

set xlabel 'Tipo de protocolo'
plot 'type.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+2700):2 with labels title ''

set terminal png size 2000,480
set xtics rotate by 270

set output 'src.png'
set xlabel 'IP emisor del paquete'
plot 'src.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+300):2 with labels title ''

set output 'dst.png'
set xlabel 'IP destinatario del paquete'
plot 'dst.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+30):2 with labels title ''
