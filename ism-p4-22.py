#python program for part (c) 
from sympy.solvers import solve
from sympy import Symbol
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb
from lwz import *

n1=2000
n2=2000

m=np.arange(n1)/100.+0.1
ksi=np.arange(n2)/100.+0.1
fg=np.zeros((n1,n2))

r0=[1.,4./3.,7./5.,5./3.]
co=['b','k','r','g']
plt.figure()
for ii in [0,1,2,3]:
    r=r0[ii]
    if r != 1:
        ksi1=(5.-3.*r)/4.
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
        ladas=np.exp(1.5)/4.
        lmax=1./ladas
        ll=np.arange(41)/40.*lmax*2.
        for i in np.arange(n1):
            for j in np.arange(n2):
                f=np.exp(0.5*m[i]*m[i]-np.log(m[i]))
                g=np.exp(2*np.log(ksi[j])+1./ksi[j])
                fg[i,j]=f/g
    
    
    mxin=np.zeros(n1)
    
    ll=np.zeros(1)+lmax
    CS= plt.contour(ksi,m,fg,[lmax],colors='w')
    dd=CS.collections[0].get_paths()[0]
    dd2=CS.collections[0].get_paths()[1]
    v=dd.vertices
    x=v[:,0]
    y=v[:,1]
    
    v2=dd2.vertices
    x2=v2[:,0]
    y2=v2[:,1]
    
    x=np.array(x)
    y=np.array(y)
    ind1=np.where((x >= ksi0))
    x1=x[ind1]
    y1=y[ind1]
    ind2=np.where((x2 < ksi0))
    x22=x2[ind2]
    y22=y2[ind2]
    
    rou11=ladas**(2./(r+1.))*y1**(-2./(r+1.))*x1**(-4./(r+1.))
    rou22=ladas**(2./(r+1.))*y22**(-2./(r+1.))*x22**(-4./(r+1.))
    vc11=y1*rou11**((r-1.)/2.)
    vc22=y22*rou22**((r-1.)/2.)

    ff=0
    if ff == 1:
        plt.plot(np.log10(x1),np.log10(rou11),co[ii],label=r'$\gamma$='+str(r))
        plt.plot(np.log10(x22),np.log10(rou22),co[ii])
        plt.title('bondi accretion')
        plt.ylim(0.,1.5)
        plt.xlim(-1,1.)
        plt.xlabel(r'$\xi$')
        plt.ylabel(r'$\rho/\rho1$')
        plt.legend(loc=0)
    if ff == 0:
        plt.plot(np.log10(x1),np.log10(vc11),co[ii],label=r'$\gamma$='+str(r))
        plt.plot(np.log10(x22),np.log10(vc22),co[ii])
        plt.ylim(-1.,1.0)
        plt.xlim(-1.,1.)
        plt.xlabel(r'$\xi$')
        plt.ylabel('v/c1')
        plt.legend(loc=0)
plt.show()


