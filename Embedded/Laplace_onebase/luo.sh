mpirun -n 32 ./laplace_reduced 32 : -n 64 ./laplace_full 32
mv outputPar.dat 32_outputPar_irregular.dat
run -n 16 ./laplace_reduced 16 : -n 64 ./laplace_full 16
mv outputPar.dat 16_outputPar_irregular.dat
mv outputPar_reduced.dat 16_outputPar_reduced.dat
mpirun -n 8 ./laplace_reduced 8 : -n 64 ./laplace_full 8
mv outputPar.dat 8_outputPar_irregular.dat
mpirun -n 4 ./laplace_reduced 4 : -n 64 ./laplace_full 4
mv outputPar.dat 4_outputPar_irregular.dat
mpirun -n 2 ./laplace_reduced 2 : -n 64 ./laplace_full 2
mv outputPar.dat 2_outputPar_irregular.dat
mpirun -n 1 ./laplace_reduced 1 : -n 64 ./laplace_full 1
mv outputPar.dat 1_outputPar_irregular.dat
