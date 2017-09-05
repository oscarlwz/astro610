
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

n=1000
tt=0.5
a=np.random.rand(n)
b=np.zeros(n)
head=np.where(a > tt)
tail=np.where(a < tt)
b[head]=1
b[tail]=0
nh=np.size(head)
nt=np.size(tail)

x=np.arange(n)
plt.figure('T='+str(tt))
plt.plot(x,b,'.k')
plt.ylim(-0.1,2.)
plt.figure('histogram')
plt.hist(b,bins=2)

pdata=misc.comb(n,nt)*(tt**nt)*((1.-tt)**nh)
pdatanr=1.
ptnr=1.
pt=pdata*ptnr
plt.plot(tt,pt)

nn=501
t=np.zeros(nn)
pt=np.zeros(nn)
plt.figure('T vs P(T)')

for ii in np.arange(nn):
    t0=1./(nn-1)*ii
    pdata=(t0**nt)*((1.-t0)**nh)
    ptnr=1.
    
    t[ii]=t0
    pt[ii]=pdata*ptnr 
    print(t0,pdata,t0**nt,(1.-t0)**nh,nt,nh,misc.comb(n,nt))

plt.title('T='+str(tt)+', uniform prior, unnormalized, '+str(n)+' tosses')
plt.xlabel('T')
plt.ylabel('p(T|data,N,R)')

plt.plot(t,pt,'-')

plt.figure('normalized to max')
mp=np.max(pt)
pt=1./mp*pt
plt.plot(t,pt,'-')
print(pt[0:10])
plt.title('T='+str(tt)+', uniform prior, normalized to peak, '+str(n)+' tosses')
plt.xlabel('T')
plt.ylabel('p(T|data,N,R)')
plt.show()

