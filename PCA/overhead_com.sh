#List=" Heat3d Laplace protein-Ligand Free-energy lysozyme umbrella Virtual-Sites"
List="Heat3d	Laplace	Wave	umbrella	Virtual-Sites	astro	fish	sedov-pres	yf17_temp"
#List="Heat3d Laplace Wave Free-energy lysozyme protein-Ligand umbrella Virtual-Sites astro blast2-pres bump_dense dpot eddy_velx_f4 fish sedov-pres yf17_pres yf17_temp"
start=`date +%s.%N`

set -- $List
err=32
err1=4
for i
do

    echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    echo $i
    echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

#./transfer $i.dat $i.dat.b
#./transfer $i.dat.1 $i.dat.1.b
    echo "PCA  Finish!"
   # base_size='0'
   # base_size=$(( $base_size+ $(stat -c%s $i) ))
    
   Inputdata/transfer  Inputdata/$i.dat base
   size='0'
   size=$(( $size+ $(stat -c%s base)/8 ))
#   /home/luo/Tao/LossyCompressStudy/zfp/examples/zfp -p $err -s -d -1 $size -i base -z base.zfp
   /home/luo/Tao/LossyCompressStudy/SZ/example/testdouble_compress sz.config base  $size
   #echo $(stat -c%s base)/$(stat -c%s ori_$i.fpc) |bc -l

done

end=`date +%s.%N`

start_s=$(echo $start | cut -d '.' -f 1)

    start_ns=$(echo $start | cut -d '.' -f 2)

    end_s=$(echo $end | cut -d '.' -f 1)

    end_ns=$(echo $end | cut -d '.' -f 2)


    time_micro=$(( (10#$end_s-10#$start_s)*1000000 + (10#$end_ns/1000 - 10#$start_ns/1000) )) 

    time_ms=`expr $time_micro/1000  | bc ` 

  

    echo "$time_micro microseconds"

    echo "$time_ms ms"

