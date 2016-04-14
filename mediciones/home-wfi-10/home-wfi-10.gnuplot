set terminal png
set output 'home-wfi-10Protocolos.png'

set style fill solid 0.5

plot 'home-wfi-10Protocolos.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+110):2 with labels title ''

set xtics rotate by 340

set output 'home-wfi-10IpsDstArp.png'
plot 'home-wfi-10IpsDstArp.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+10):2 with labels title ''

set output 'home-wfi-10IpsSrcArp.png'
plot 'home-wfi-10IpsSrcArp.txt' using 2:xticlabels(1) with boxes ls 1 title '',\
  '' using 0:($2+10):2 with labels title ''
