#List=" Heat3d Laplace protein-Ligand Free-energy lysozyme umbrella Virtual-Sites"
List="Heat3d	Laplace	Wave	umbrella	Virtual-Sites	astro	fish	sedov-pres	yf17_temp"
#List="Heat3d Laplace Wave Free-energy lysozyme protein-Ligand umbrella Virtual-Sites astro blast2-pres bump_dense dpot eddy_velx_f4 fish sedov-pres yf17_pres yf17_temp"

set -- $List
err=16
err1=8
for i
do

    echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    echo $i
    echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

#./transfer $i.dat $i.dat.b
#./transfer $i.dat.1 $i.dat.1.b
    python  pca.py Inputdata\_sampling/$i\_sample.dat
    echo "PCA  Finish!"
   # base_size='0'
   # base_size=$(( $base_size+ $(stat -c%s $i) ))
    
   Inputdata/transfer  Inputdata\_sampling/$i\_sample.dat base
   size='0'
   size=$(( $size+ $(stat -c%s base)/8 ))
   echo $size 
   /home/luo/Tao/LossyCompressStudy/zfp/examples/zfp -p $err -s -d -1 $size -i base -z base.zfp
   /home/luo/Tao/LossyCompressStudy/SZ/example/testdouble_compress sz.config base  $size
   /home/luo/Tao/LossyCompressStudy/fpc/fpc 20 < base > base.fpc
   #echo $(stat -c%s base)/$(stat -c%s ori_$i.fpc) |bc -l

   Inputdata/transfer  lowDDataMat.txt low_base
   size='0'
   size=$(( $size+ $(stat -c%s low_base)/8 ))

   /home/luo/Tao/LossyCompressStudy/zfp/examples/zfp -p $err -s -d -1 $size -i low_base -z low_base.zfp
/home/luo/Tao/LossyCompressStudy/SZ/example/testdouble_compress sz.config low_base  $size
   /home/luo/Tao/LossyCompressStudy/fpc/fpc 20 < low_base > low_base.fpc

   Inputdata/transfer  delta.txt delta
   size='0'
   size=$(( $size+ $(stat -c%s delta)/8 ))

   /home/luo/Tao/LossyCompressStudy/zfp/examples/zfp -p $err1 -s -d -1 $size -i delta -z delta.zfp
/home/luo/Tao/LossyCompressStudy/SZ/example/testdouble_compress sz1.config delta  $size
   /home/luo/Tao/LossyCompressStudy/fpc/fpc 20 < delta > delta.fpc

   base_size=$((  $(stat -c%s base) ))
   zfp_size=$(( $(stat -c%s low_base.zfp)+ $(stat -c%s delta.zfp) ))
   sz_size=$(( $(stat -c%s low_base.sz) + $(stat -c%s delta.sz) ))
   fpc_size=$(( $(stat -c%s low_base.fpc) + $(stat -c%s delta.fpc)  ))
   echo $base_size/$zfp_size |bc -l
   echo $(stat -c%s base)/$(stat -c%s base.zfp) |bc -l
   echo $base_size/$sz_size |bc -l
  # echo $base_size/$fpc_size |bc -l
   echo $(stat -c%s base)/$(stat -c%s base.sz) |bc -l
   #echo $(stat -c%s base)/$(stat -c%s base.fpc) |bc -l 
   #echo $(stat -c%s delta)/$(stat -c%s delta.zfp) |bc -l
   #echo $(stat -c%s delta)/$(stat -c%s delta.sz) |bc -l
   #echo $(stat -c%s delta)/$(stat -c%s delta.fpc) |bc -l
done

