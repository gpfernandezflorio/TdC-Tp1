set terminal png
set output 'plot.png'

set style fill solid 0.5

plot 'mediciones/aabProtocolos.txt' using 2:xticlabels(1) with boxes ls 1 title ''
