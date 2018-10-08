import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import collections
import sys

#objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
import scipy.stats
import struct
import array
import os

Dpot=[7.28,7.72,-0.01]
Astro=[6.63,7.48,0.12]
Fish=[1.80,5.09,0.73]
Sedov=[3.90,4.95,0.43]
Blast2=[2.43,2.58,0.51]
Eddy=[6.69,7.66,0.29]
YF17_p=[4.41,7.00,0.35]
YF17_t=[4.21,6.52,0.42]
Bump=[7.34,7.77,-0.16]

p = [0.01, 0.1, 1, 5, 10, 20, 30, 40, 50, 60,70,80,90,95,99,99.9]

statinfo = os.stat(sys.argv[1])
fsize = statinfo.st_size

a = array.array('d', int(fsize / 8) * [0])


fin =  open(sys.argv[1], 'rb')
fin.readinto(a)


slot = 1000
data = []
m1 = min(a)
m2 = max(a)
print (max(a), min(a))
r = max(a) - min(a)
intv = r / slot
print (intv)

for i in a:
    data.append(int((i-m1) / intv))

d = dict()
for i in data:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print (d)
od = collections.OrderedDict(sorted(d.items()))


#m = int(sys.argv[2])
m = slot/2
l = int(m * 0)
r = int(m * 2)
#maxy = 1000

maxx = 0
maxy = 0
for k in d:
    if d[k] > maxy:
        maxy = d[k]
        maxx = k

print (maxx, maxy)

#maxy = max(d.values()) + 50
maxy = 1.02
print (maxy)


#od[0] = 0
for i in range(slot):
    if i not in od:
        od[i] = 0 

k, v = [], []
for i in od:
    k.append(i)
    v.append(float(od[i]))
    #if key >= l and key <= r:
    #print (i, od[i])
    #    k.append(key)
    #    v.append(val)

print (v)
cv = np.cumsum(v)
s = float(cv[-1])
for i in range(len(cv)):
    cv[i] /= s 

print (cv)
#print k, v
plt.figure(num=None, figsize=(5.5, 5), dpi=120, facecolor='w', edgecolor='k')
#plt.bar(k, v, align='center', alpha=0.5, color='black')
plt.plot(cv, color='black')
#plt.bar(k, v, align='center', alpha=0.5, color='black')
plt.ylim(0, maxy)
#plt.ylim(0, 600)
#plt.xticks([l,m,r])
#plt.xticks([l,r], [float("{0:.5f}".format(l*intv+m1)), float("{0:.5f}".format(r*intv+m1))])
plt.xticks([l,r], [float("{0:.4f}".format(l*intv+m1)), str(float("{0:.1f}".format((r*intv+m1)/1000000)))+'M'])
#plt.xticks([l,m,r], [float("{0:.4f}".format(l*intv+m1)), float("{0:.4f}".format(m*intv+m1)), float("{0:.4f}".format(r*intv+m1))])
#plt.xticks(k)
plt.tick_params(axis='both', which='major', labelsize=28)
plt.xlabel('Value', fontsize=28)

if sys.argv[2] == 'Dpot':
    ent = 'ent='+str(Dpot[0])
    core = 'coreset='+str(Dpot[1])
    corr = 'corr='+str(Dpot[2])
if sys.argv[2] == 'Astro':
    ent = 'ent='+str(Astro[0])
    core = 'coreset='+str(Astro[1])
    corr = 'corr='+str(Astro[2])
if sys.argv[2] == 'Fish':
    ent = 'ent='+str(Fish[0])
    core = 'coreset='+str(Fish[1])
    corr = 'corr='+str(Fish[2])
if sys.argv[2] == 'Sedov':
    ent = 'ent='+str(Sedov[0])
    core = 'coreset='+str(Sedov[1])
    corr = 'corr='+str(Sedov[2])
if sys.argv[2] == 'Blast2':
    ent = 'ent='+str(Blast2[0])
    core = 'coreset='+str(Blast2[1])
    corr = 'corr='+str(Blast2[2])
if sys.argv[2] == 'YF17_p':
    ent = 'ent='+str(YF17_p[0])
    core = 'coreset='+str(YF17_p[1])
    corr = 'corr='+str(YF17_p[2])
if sys.argv[2] == 'YF17_t':
    ent = 'ent='+str(YF17_t[0])
    core = 'coreset='+str(YF17_t[1])
    corr = 'corr='+str(YF17_t[2])
if sys.argv[2] == 'Bump':
    ent = 'ent='+str(Bump[0])
    core = 'coreset='+str(Bump[1])
    corr = 'corr='+str(Bump[2])
if sys.argv[2] == 'Eddy':
    ent = 'ent='+str(Eddy[0])
    core = 'coreset='+str(Eddy[1])
    corr = 'corr='+str(Eddy[2])


plt.text(0.9*m,0.4,ent, fontsize=23)
plt.text(0.9*m,0.25,core, fontsize=23)
plt.text(0.9*m,0.1,corr, fontsize=23)
#plt.ylabel('Occurence Count', fontsize=28)
plt.title(sys.argv[2], fontsize=28)
plt.tight_layout()
#plt.show()

plt.savefig('/home/qliu/Dropbox/DataReductionEvaluate-2018/figures/Figure12-' + sys.argv[2] + '_dist.png')


