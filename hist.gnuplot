set terminal png
set output 'plot.png'

set style fill solid 0.5

set yrange [0:35]

plot 'data.txt' using 2:xticlabels(1) with boxes ls 1 title ''
