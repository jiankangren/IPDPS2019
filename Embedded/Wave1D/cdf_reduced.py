import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
import sys
import array
import os

if len(sys.argv) < 1 :
    print 'usage: python %s <file.dat' % sys.argv[0]
    sys.exit(0)

statinfo=os.stat(sys.argv[1])
fsize=statinfo.st_size
print fsize
fin = open(sys.argv[1], 'rb')
vals = array.array('d',(int(fsize/8))*[0])
fin.readinto(vals)
fin.close()



x1=min(vals);
x2=max(vals);
plt.figure(5,figsize=(8,4))
plt.rc('xtick', labelsize=24)          # fontsize of the tick labels
plt.rc('ytick', labelsize=24)
plt.ylim((0.0,1.0))   
plt.xlim(x1,x2)

axis_font = {'fontname':'Arial', 'size':'24'}
axes = plt.gca()
plt.xlabel('values', **axis_font)
plt.ylabel('Frequency',**axis_font )
plt.title('Wave (reduced)', **axis_font)
n, bins, patches=plt.hist(vals,bins=1000,normed=True,histtype='bar', label='pdf',facecolor='black')
n, bins, patches=plt.hist(vals,bins=1000,normed=True,histtype='step', cumulative=True, label='cdf',facecolor='black')
plt.savefig('reduced_wave.pdf', format='pdf')
plt.show()
