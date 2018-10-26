from __future__ import division
import sys
import array
import adios as ad
import scipy.stats as stats
import os


import numpy as np
import matplotlib.pyplot as plt
import os
import array

def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split() for line in fr.readlines()]
    print np.shape(stringArr)
   # print stringArr
    datArr = [map(float, line) for line in stringArr]
    return np.mat(datArr)
def storeMatrix(filename,m1):
    mat1 = np.matrix(m1)
    with open(filename,'wb') as f:
        for line in mat1:
                np.savetxt(f, line.real, fmt='%f')
	

filename="Laplace"
#list1=["Heat3d","Laplace","Wave","umbrella","Virtual-Sites","astro","fish","sedov-pres","yf17_temp"]
#list1=["Heat3d","Laplace","Wave","Free-energy","lysozyme","protein-Ligand","umbrella","Virtual-Sites","astro","blast2-pres","bump_dense","dpot","eddy_velx_f4","fish","sedov-pres","yf17_pres","yf17_temp"]
#list1=["astro","blast2-pres","bump_dense","dpot","eddy_velx_f4","fish","sedov-pres","yf17_pres","yf17_temp"]
vals=loadDataSet("Inputdata/"+filename+".dat")
row=np.shape(vals)[0]
col=np.shape(vals)[1]
fin =  open('base', 'wb')
fin.write(vals)
fin.close()
vals_0=vals.flatten()
statinfo=os.stat("base")
base_fsize=statinfo.st_size
#vals_0=np.reshape(vals,(1,-1))
vals_0=np.array(vals_0)

SVD_cmd="python pca.py "+ "Inputdata/"+filename+".dat" 
os.system(SVD_cmd)
delta=loadDataSet("delta.txt")
fin =  open('delta', 'wb')
fin.write(delta)
fin.close()
        
low_base=loadDataSet("lowDDataMat.txt")
fin =  open('low_base', 'wb')
fin.write(low_base)
fin.close()
statinfo=os.stat("low_base")
low_base_fsize=statinfo.st_size


fp=open("CR_RMSE.txt","w")
for err in range(5,33):
    for err1 in range(5,err+1):
        print "*******************"
        print err, err1 
        print "*******************"
        fp.write(str(err)+" "+ str(err1)+ " ") 
        zfpcmpresscmd = '/home/luo/Tao/LossyCompressStudy/zfp/examples/zfp -p '+str(err)+' -s -d -1 '+str(row*col)+' -i base -z base.zfp'
        statinfo=os.stat("base.zfp")
        base_cmpr_fsize=statinfo.st_size
	zfpdecmp = '/home/luo/Tao/LossyCompressStudy/zfp/examples/zfp -p  '+str(err)+' -d -1 '+str(row*col)+ ' -z base.zfp -o base.zfp.out'
        #print zfpdecmp
	os.system(zfpcmpresscmd)

	os.system(zfpdecmp)

	fin = open('base.zfp.out', 'rb')
        vals_1 = array.array('d', row*col*[0])
	fin.readinto(vals_1)
	fin.close()
         
        
        RMSE= np.sqrt(((vals_1 - vals_0) ** 2).mean())
        print RMSE
        fp.write(str(RMSE)+" ")        
 

	
        zfpcmpresscmd = '/home/luo/Tao/LossyCompressStudy/zfp/examples/zfp -p '+str(err1)+' -s -d -1 '+str(row*col)+' -i delta -z delta.zfp'
        statinfo=os.stat("delta.zfp")
        delta_cmp_fsize=statinfo.st_size
        zfpdecmp = '/home/luo/Tao/LossyCompressStudy/zfp/examples/zfp -p  '+str(err1)+' -d -1 '+str(row*col)+ ' -z delta.zfp -o delta.zfp.out'
        #print zfpdecmp
        os.system(zfpcmpresscmd)

        os.system(zfpdecmp)

        fin = open('delta.zfp.out', 'rb')
        delta_1 = array.array('d', row*col*[0])

        fin.readinto(delta_1)
        fin.close()
        
        delta_1=np.reshape(delta_1,(row,col))
        #storeMatrix("delta_luo.txt",delta_1)
        #RMSE_delta= np.sqrt(((delta_1 - delta) ** 2).mean())
        #print "delta_RMSE", RMSE_delta

        reconMat=loadDataSet("reconMat.txt")
        recoverMat=reconMat+delta_1
         
        reconVals=recoverMat.flatten()
        #vals_0=np.reshape(vals,(1,-1))
        reconVals_0=np.array(reconVals)

 
        RMSE_final= np.sqrt(((reconVals_0 - vals_0) ** 2).mean())
        print RMSE_final
        fp.write(str(RMSE_final)+" ")
        fp.write(str(base_fsize/base_cmpr_fsize)+ " ")
        fp.write(str(base_fsize/(low_base_fsize+delta_cmp_fsize))+ "\n")
         
fp.close()
