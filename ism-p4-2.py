#python program for part (b)
from sympy.solvers import solve
from sympy import Symbol
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb
from lwz import *



r=1.
r=4./3.
#r=7./5.
#r=5./3.

n1=100
n2=100

m=np.arange(n1)/50.+0.0001
ksi=np.arange(n2)/150.+0.0001
fg=np.zeros((n1,n2))

if r != 1:
    ksi1=(5.-3.*r)/4.
    ksi1=0.5
    ksi0=ksi1
    l1=ksi0**(-1.*(5.-3.*r)/(r+1.))
    l2=1./(r-1.)*ksi0**(4.*(r-1.)/(r+1.))
    ladas=((0.5+1./(r-1.))/(l1+l2))**(-0.5*(r+1.)/(r-1.))
    lmax=ladas**(-2.*(r-1.)/(r+1.))
    ll=np.arange(41)/40.*lmax*2
    for i in np.arange(n1):
        for j in np.arange(n2):
            f=0.5*m[i]**(4./(r+1))+(m[i]**(-2.*(r-1.)/(r+1.)))/(r-1.)
            g=ksi[j]**(-1.*(5.-3.*r)/(r+1.))+1./(r-1.)*ksi[j]**(4.*(r-1.)/(r+1.))
            fg[i,j]=f/g


if r == 1:
    ksi1=0.5
    ksi0=ksi1
    ladas=1.12
    lmax=1./ladas
    ll=np.arange(41)/40.*lmax*2.
    for i in np.arange(n1):
        for j in np.arange(n2):
            f=np.exp(0.5*m[i]*m[i]-np.log(m[i]))
            g=np.exp(2*np.log(ksi[j])+1./ksi[j])
            fg[i,j]=f/g


mxin=np.zeros(n1)
fig=plt.figure()
CS= plt.contour(ksi,m,fg)
dd=CS.collections[0].get_paths()[0]
dd2=CS.collections[0].get_paths()[1]

plt.clabel(CS, inline=1, fontsize=10)

dd=CS.collections[0].get_paths()
l2=plt.plot([(5.-3.*r)/4.],[1.],'ko',label='sonic point')
plt.title(r'$\gamma$='+str(r))
plt.legend(loc=0,numpoints=1)
plt.xlabel(r'$\xi$')
plt.ylabel('M')

plt.show()


