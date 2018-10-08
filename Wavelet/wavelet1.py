# coding: utf-8



import sys
import array
import os



import pywt
import matplotlib.pyplot as plt
import numpy as np


def storeMatrix(filename,m1):
    mat1 = np.matrix(m1)
    with open(filename,'wb') as f:
        for line in mat1:
                np.savetxt(f, line.real, fmt='%f')

def analyse_data(Sigma, loopNum=20):

    Sig2 = Sigma**2
    SigmaSum = sum(Sig2)
    for i in range(loopNum):
        SigmaI = sum(Sig2[:i+1])
        print 'primary: %s, accumulate: %s%%' % (format(i+1, '2.0f'), format(SigmaI/SigmaSum*100, '4.2f'))



def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split() for line in fr.readlines()]
    print np.shape(stringArr)
   # print stringArr
    datArr = [map(float, line) for line in stringArr]
    return np.mat(datArr)

if __name__ == "__main__":

    filename=sys.argv[1]
    dataMat = loadDataSet(filename)

    coeffs = pywt.dwt2(dataMat, 'haar')
    #print coeffs
    #a1,a2= pywt.coeffs_to_array(coeffs)
    #print a1
    #print a2
    cA, (cH, cV, cD) = coeffs
    storeMatrix("coeffs1.txt",cA)
    storeMatrix("coeffs2.txt",cH)
    storeMatrix("coeffs3.txt",cV)
    storeMatrix("coeffs4.txt",cD)
    #coeffs_t=coeffs
    #np.where(coeffs_t > 0, coeffs_t, 0)
    #print coeffs_t
    coeffs_td=[]
    for ii in coeffs:
	a=pywt.threshold(ii, 0.2, 'hard')
        coeffs_td.append(a)
    #print  coeffs_td
    coeffs_td1=np.mat(coeffs_td)
    coeffs1=np.mat(coeffs)
    print np.shape(coeffs_td1)
    print np.shape(coeffs1)
    storeMatrix("coeffs_td.txt",np.mat(np.mat(coeffs)))

    #print coeffs_td
    recdata=pywt.idwt2(coeffs_td, 'haar')
    delta=recdata-dataMat
    storeMatrix("delta.txt",delta)
