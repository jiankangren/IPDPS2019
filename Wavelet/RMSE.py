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
	

#list1=["Wave"]
list1=["Heat3d","Laplace","Wave","umbrella","Virtual-Sites","astro","fish","sedov-pres","yf17_temp"]
#list1=["Heat3d","Laplace","Wave","Free-energy","lysozyme","protein-Ligand","umbrella","Virtual-Sites","astro","blast2-pres","bump_dense","dpot","eddy_velx_f4","fish","sedov-pres","yf17_pres","yf17_temp"]
#list1=["astro","blast2-pres","bump_dense","dpot","eddy_velx_f4","fish","sedov-pres","yf17_pres","yf17_temp"]
err=16
err1=8

fp=open("RMSE.txt","w")
for filename in list1:
        print "*******************"
        print filename
        print "*******************"
        vals=loadDataSet("Inputdata/"+filename+".dat")
        row=np.shape(vals)[0]
        col=np.shape(vals)[1]
	fin =  open('base', 'wb')
	fin.write(vals)
	fin.close()
	vals_0=vals.flatten()
        #vals_0=np.reshape(vals,(1,-1))
        vals_0=np.array(vals_0)
        print np.shape(vals_0)
        
        zfpcmpresscmd = '/home/luo/Tao/LossyCompressStudy/zfp/examples/zfp -p '+str(err)+' -s -d -1 '+str(row*col)+' -i base -z base.zfp'
	zfpdecmp = '/home/luo/Tao/LossyCompressStudy/zfp/examples/zfp -p  '+str(err)+' -d -1 '+str(row*col)+ ' -z base.zfp -o base.zfp.out'
        #print zfpdecmp
	os.system(zfpcmpresscmd)

	os.system(zfpdecmp)

	fin = open('base.zfp.out', 'rb')
        vals_1 = array.array('d', row*col*[0])
	fin.readinto(vals_1)
	fin.close()
         
        print np.shape(vals_1)
        
        RMSE= np.sqrt(((vals_1 - vals_0) ** 2).mean())
        print RMSE
        fp.write(str(RMSE)+" ")        
 
        SVD_cmd="python wavelet.py "+ "Inputdata/"+filename+".dat" 
        os.system(SVD_cmd)

        delta=loadDataSet("delta.txt")

        fin =  open('delta', 'wb')
        fin.write(delta)
        fin.close()
	
        zfpcmpresscmd = '/home/luo/Tao/LossyCompressStudy/zfp/examples/zfp -p '+str(err1)+' -s -d -1 '+str(row*col)+' -i delta -z delta.zfp'
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

        reconMat=loadDataSet("recdata.txt")
        recoverMat=reconMat+delta_1
         
        reconVals=recoverMat.flatten()
        #vals_0=np.reshape(vals,(1,-1))
        reconVals_0=np.array(reconVals)

 
        RMSE_final= np.sqrt(((reconVals_0 - vals_0) ** 2).mean())
        print RMSE_final
        fp.write(str(RMSE_final)+" ")

        szcmpresscmd = '/home/luo/Tao/LossyCompressStudy/SZ/example/testdouble_compress sz.config base '+str(row*col)
        szdecmp = '/home/luo/Tao/LossyCompressStudy/SZ/example/testdouble_decompress sz.config base.sz '+str(row*col)        #print zfpdecmp
        os.system(szcmpresscmd)

        os.system(szdecmp)

        fin = open('base.sz.out', 'rb')
        vals_sz = array.array('d', row*col*[0])
        fin.readinto(vals_sz)
        fin.close()


        RMSE_sz= np.sqrt(((vals_sz- vals_0) ** 2).mean())
        print RMSE
        fp.write(str(RMSE_sz)+" ")



        szcmpresscmd = '/home/luo/Tao/LossyCompressStudy/SZ/example/testdouble_compress sz1.config delta '+str(row*col)
        szdecmp = '/home/luo/Tao/LossyCompressStudy/SZ/example/testdouble_decompress sz1.config delta.sz '+str(row*col)

        #szcmpresscmd = '/home/luo/Tao/LossyCompressStudy/zfp/examples/zfp -p '+str(err1)+' -s -d -1 '+str(row*col)+' -i delta -z delta.zfp'
        #szdecmp = '/home/luo/Tao/LossyCompressStudy/zfp/examples/zfp -p  '+str(err1)+' -d -1 '+str(row*col)+ ' -z delta.zfp -o delta.zfp.out'
        #print zfpdecmp
        os.system(szcmpresscmd)

        os.system(szdecmp)

        fin = open('delta.sz.out', 'rb')
        delta_1 = array.array('d', row*col*[0])

        fin.readinto(delta_1)
        fin.close()

        delta_sz=np.reshape(delta_1,(row,col))

       # RMSE_delta= np.sqrt(((delta_sz- delta) ** 2).mean())

        #print "RMSE_delta_sz", RMSE_delta

        reconMat=loadDataSet("recdata.txt")
        recoverMat=reconMat+delta_sz

        reconVals_sz=recoverMat.flatten()
        #vals_0=np.reshape(vals,(1,-1))
        reconVals_sz=np.array(reconVals_sz)


        RMSE_final_sz= np.sqrt(((reconVals_sz - vals_0) ** 2).mean())
        print RMSE_final
        fp.write(str(RMSE_final_sz)+"\n")


fp.close()
