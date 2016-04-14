set terminal png
set output 'home-eth-10Protocolos.png'

set style fill solid 0.5

plot 'home-eth-10Protocolos.txt' using 2:xticlabels(1) with boxes ls 1 title ''

set output 'home-eth-10IpsDstArp.png'
plot 'home-eth-10IpsDstArp.txt' using 2:xticlabels(1) with boxes ls 1 title ''

set output 'home-eth-10IpsSrcArp.png'
plot 'home-eth-10IpsSrcArp.txt' using 2:xticlabels(1) with boxes ls 1 title ''
