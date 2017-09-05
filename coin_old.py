
from astropy.io import fits
from scipy.optimize import curve_fit
from astropy.table import Table
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb
import scipy.misc as misc

n=200
t=0.5
a=np.random.rand(n)
b=np.zeros(n)
head=np.where(a > t)
tail=np.where(a < t)
b[head]=1
b[tail]=0
nh=np.size(head)
nt=np.size(tail)

x=np.arange(n)
plt.figure('T=0.5')
plt.plot(x,b,'.k')
plt.ylim(-0.1,2.)
plt.figure('histogram')
plt.hist(b,bins=2)

#pdata=misc.comb(n,nt)(t**nt)*((1.-t)**nh)
pdata=(t**nt)*((1.-t)**nh)
pdatanr=1.
ptnr=1.
pt=pdata*ptnr
plt.plot(t,pt)
#plt.show()


n=256
nn=501
t=np.zeros(nn)
pt=np.zeros(nn)
plt.figure('T vs P(T)')
a=np.random.rand(n)
b=np.zeros(n)

for ii in np.arange(nn):
    t0=1./(nn-1)*ii
    head=np.where(a > 0.5)
    tail=np.where(a < 0.5)
    b[head]=1
    b[tail]=0
    nh=np.size(head)
    nt=np.size(tail)
#    pdata=misc.comb(n,nt)*(t0**nt)*((1.-t0)**nh)
    pdata=(t0**nt)*((1.-t0)**nh)
    ptnr=1.
    
    t[ii]=t0
    pt[ii]=pdata*ptnr 
    print(t0,pdata,t0**nt,(1.-t0)**nh,nt,nh,misc.comb(n,nt))

plt.plot(t,pt,'-')

plt.figure('normalized to max')
mp=np.max(pt)

pt=1./mp*pt
plt.plot(t,pt,'-')
print(pt[0:10])
plt.show()

