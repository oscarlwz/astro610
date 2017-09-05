from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb
from lwz import *

t1=1e8
t2=5e7
k=1.38e-16
g=6.67e-8
pi=np.pi
l0=3.086e24
mh=1.67e-24
gb=1.1

#sm2=2*k*t/mh

r0=np.arange(1000)/1000.

r=r0*l0

#ro=sm2/2./pi/g/r/r
#n=ro/mh
#be=1.4e-27*(t**0.5)*n*n*g
#e=n*k*t


n=k*t1/pi/g/mh/mh/r/r
xishu=20*pi*g*r*r*mh*mh/(1.4e-27)/gb


ct=xishu*(t2**(-0.5)-t1**(-0.5))

ct2=ct/365./24./3600.
plt.figure()
#plt.plot(v,tau2)
#plt.plot(v,tau1)


tt=10**10*365.*24.*3600.
rtt=tt/(20*pi*g*mh*mh)*(1.4e-27)*gb/(t2**(-0.5)-t1**(-0.5))
rtt=rtt**0.5

plt.plot(r0,ct2)
plt.ylabel("cooling time/yr")
plt.xlabel("radius/Mpc")
plt.plot([0.0,1.0],[1e10,1e10])
#print(n[1],be[1],e[1])
print(rtt,rtt/l0)
plt.show()
