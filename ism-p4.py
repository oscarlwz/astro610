import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb
from lwz import *



r=1.

ladas=np.exp(1.5)/4.
mass=2e33
mh=1.67e-24
rou1=40*mh
gc=6.67e-8
c1=8e4
dm=4*np.pi*(gc*mass)**2/(c1**3)*rou1*ladas

print('accretion',dm)

ladas=np.exp(1.5)/4.
mass=2e40
mh=1.67e-24
rou1=100*2*mh
gc=6.67e-8
c1=2e4
dm=4*np.pi*(gc*mass)**2/(c1**3)*rou1*ladas

print('accretion',dm,rou1,ladas,c1)


r=4./3.
r=7./5.


r=1.2
ksi1=(5.-3.*r)/4.
#ksi2=0.5
ksi=ksi1
l1=ksi**(-1.*(5.-3.*r)/(r+1.))
l2=1./(r-1.)*ksi**(4.*(r-1.)/(r+1.))
ladas=((0.5+1./(r-1.))/(l1+l2))**(-0.5*(r+1.)/(r-1.))
print(r,ladas)


#mass=2e34
#rou1=(3.6e-31)*6**3
#gc=6.67e-8
#c1=8e4
#dm=4*np.pi*(gc*mass)**2/(c1**3)*rou1*ladas
#
#print('accretion',dm)


r=4./3.
ksi1=(5.-3.*r)/4.
#ksi2=0.5
ksi=ksi1
l1=ksi**(-1.*(5.-3.*r)/(r+1.))
l2=1./(r-1.)*ksi**(4.*(r-1.)/(r+1.))
ladas=((0.5+1./(r-1.))/(l1+l2))**(-0.5*(r+1.)/(r-1.))
print(r,ladas)

r=7./5.
ksi1=(5.-3.*r)/4.
#ksi2=0.5
ksi=ksi1
l1=ksi**(-1.*(5.-3.*r)/(r+1.))
l2=1./(r-1.)*ksi**(4.*(r-1.)/(r+1.))
ladas=((0.5+1./(r-1.))/(l1+l2))**(-0.5*(r+1.)/(r-1.))
print(r,ladas)

r=5./3.
ksi1=(5.-3.*r)/4.
#ksi2=0.5
ksi=ksi1
l1=ksi**(-1.*(5.-3.*r)/(r+1.))
l2=1./(r-1.)*ksi**(4.*(r-1.)/(r+1.))
ladas=((0.5+1./(r-1.))/(l1+l2))**(-0.5*(r+1.)/(r-1.))
print(r,ladas)

mass=2e34
rou1=(3.6e-31)*6**3
gc=6.67e-8
c1=7e5
dm=4*np.pi*(gc*mass)**2/(c1**3)*rou1*ladas

print('accretion',dm)



plt.figure()
#plt.show()
