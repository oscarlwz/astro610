from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb


u=3
l=2
m=1


b=1.
k=1.
eul=u*(u+1)*b-(l+1)*l*b
elm=(l+1)*l*b-(m+1)*m*b
t=np.arange(10000)/100.
r1=u*(1.-np.exp(-1.*eul/k/t))
r2=l*(np.exp(elm/k/t)-1.)
r=r1/r2


plt.figure
plt.plot(t,np.zeros(10000)+1.)
plt.xlabel('T(in unit of B/k)')
plt.ylabel('ratio of 2-1 over 1-0')
plt.show()
