from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb
from lwz import *

s1=10./2.35
s2=1.5/2.35
v1=0.
v2=2.0
ts1=1000
ts2=20
n1=6e20
n2=1e20
tcmb=2.7
tcmb2=0.
v=np.arange(4000)/100.-20.

f1=gauss(v,v1,s1)
f2=gauss(v,v2,s2)

#tau1=5.489e-14*n1/ts1*f1
#tau2=5.489e-14*n2/ts2*f2
tau1=0.03/gauss(v1,v1,s1)*f1
tau2=1.72/gauss(v2,v2,s2)*f2


tb1=ts1*(1-np.exp(-1.*tau1))*np.exp(-1.*tau2)
tb2=ts2*(1-np.exp(-1.*tau2))
tb=tb1+tb2


plt.figure()
#plt.plot(v,tau2)
#plt.plot(v,tau1)
plt.ylim(0,50)
plt.plot(v,tb)

print(gauss(v1,v1,s1))
plt.figure()


#tb1b=(tcmb*np.exp(-1.*tau2)+ts2*(1-np.exp(-1.*tau2)))*np.exp(-1.*tau1)
#tb2b=ts1*(1-np.exp(-1.*tau1))
#tbb=tb1b+tb2b

tb1c=ts2*(1-np.exp(-1.*tau2))*np.exp(-1.*tau1)
tb2c=ts1*(1-np.exp(-1.*tau1))
tbc=tb1c+tb2c
plt.ylim(0,50)
plt.plot(v,tbc)
#plt.plot(v,tbc)

plt.show()
