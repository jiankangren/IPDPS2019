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
	

#list1=["Heat3d","Laplace","Free-energy","lysozyme","protein-Ligand","umbrella","Virtual-Sites","astro","blast2-pres","bump_dense","dpot","eddy_velx_f4","fish","sedov-pres","yf17_pres","yf17_temp"]
#list1=["Heat3d","Laplace","Wave","umbrella","Virtual-Sites","astro","fish","sedov-pres","yf17_temp"]
list1=["yf17_temp"]
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
        
        print np.shape(vals)
        vals_0=vals.flatten()
        #vals_0=np.reshape(vals,(1,-1))
        vals_0=np.array(vals_0)
        print np.shape(vals_0)
       	RMSE= np.sqrt(((vals_1 - vals_0) ** 2).mean())
        print RMSE
        fp.write(str(RMSE)+" ")        
 
fp.close()
