from __future__ import division
import sys
import array
import os
import numpy as np


def storeMatrix(filename,m1):
    mat1 = np.matrix(m1)
    with open(filename,'wb') as f:
    	for line in mat1:
                np.savetxt(f, line.real, fmt='%f')

def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split() for line in fr.readlines()]
    print np.shape(stringArr)
   # print stringArr
    datArr = [map(float, line) for line in stringArr]
    return np.mat(datArr)


#list1=["dpot","fish","astro","blast2-pres","bump_dense","eddy_velx_f4","sedov-pres","yf17_pres","yf17_temp"];
list1=["Wave"];
for filename in list1:
        vals=loadDataSet(filename+".dat")
	len_x=int(np.sqrt(np.shape(vals)[1]))
        print len_x
        vals_sub=vals[0,0:len_x*len_x]
        A=np.reshape(vals_sub,(len_x,len_x))
	storeMatrix("Inputdata/"+filename+".dat",A)
	print np.shape(vals)






