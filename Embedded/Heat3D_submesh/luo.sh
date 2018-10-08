mpirun -n 32 ./explicitPar_reduced 32 : -n 64 ./explicitPar 32
mv outputPar.dat 32_outputPar.dat
run -n 16 ./explicitPar_reduced 16 : -n 64 ./explicitPar 16
mv outputPar.dat 16_outputPar.dat
mpirun -n 8 ./explicitPar_reduced 8 : -n 64 ./explicitPar 8
mv outputPar.dat 8_outputPar.dat
mpirun -n 4 ./explicitPar_reduced 4 : -n 64 ./explicitPar 4
mv outputPar.dat 4_outputPar.dat
mpirun -n 2 ./explicitPar_reduced 2 : -n 64 ./explicitPar 2
mv outputPar.dat 2_outputPar.dat
mpirun -n 1 ./explicitPar_reduced 1 : -n 64 ./explicitPar 1
mv outputPar.dat 1_outputPar.dat
