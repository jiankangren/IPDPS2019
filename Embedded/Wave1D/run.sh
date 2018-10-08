i=0
nstep=6400
while [ $i -le 10 ]
do

mpirun -n 64 ./base_wave $(( $nstep+$i))

mv Wave.dat results/Wave\_$i.dat
i=$(( $i+1 ))
done
