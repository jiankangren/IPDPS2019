./compareData base.dat 32_outputPar.dat 37636
/home/qliu//zfp/examples/zfp -a 0.01 -d -1 37636 -i delta.dat -z scalar.zfp
/home/qliu/Tao/LossyCompressStudy/SZ/example/testdouble_compress sz.config delta.dat 37636
echo $(stat -c%s delta.dat)/$(stat -c%s delta.dat.sz) |bc -l
./compareData base.dat 16_outputPar.dat 37636
/home/qliu//zfp/examples/zfp -a 0.01 -d -1 37636 -i delta.dat -z scalar.zfp
/home/qliu/Tao/LossyCompressStudy/SZ/example/testdouble_compress sz.config delta.dat 37636
echo $(stat -c%s delta.dat)/$(stat -c%s delta.dat.sz) |bc -l
./compareData base.dat 8_outputPar.dat 37636
/home/qliu//zfp/examples/zfp -a 0.01 -d -1 37636 -i delta.dat -z scalar.zfp
/home/qliu/Tao/LossyCompressStudy/SZ/example/testdouble_compress sz.config delta.dat 37636
echo $(stat -c%s delta.dat)/$(stat -c%s delta.dat.sz) |bc -l
./compareData base.dat 4_outputPar.dat 37636
/home/qliu//zfp/examples/zfp -a 0.01 -d -1 37636 -i delta.dat -z scalar.zfp
/home/qliu/Tao/LossyCompressStudy/SZ/example/testdouble_compress sz.config delta.dat 37636
echo $(stat -c%s delta.dat)/$(stat -c%s delta.dat.sz) |bc -l
./compareData base.dat 2_outputPar.dat 37636
/home/qliu//zfp/examples/zfp -a 0.01 -d -1 37636 -i delta.dat -z scalar.zfp
/home/qliu/Tao/LossyCompressStudy/SZ/example/testdouble_compress sz.config delta.dat 37636
echo $(stat -c%s delta.dat)/$(stat -c%s delta.dat.sz) |bc -l
./compareData base.dat 1_outputPar.dat 37636
/home/qliu//zfp/examples/zfp -a 0.01 -d -1 37636 -i delta.dat -z scalar.zfp
/home/qliu/Tao/LossyCompressStudy/SZ/example/testdouble_compress sz.config delta.dat 37636
echo $(stat -c%s delta.dat)/$(stat -c%s delta.dat.sz) |bc -l
