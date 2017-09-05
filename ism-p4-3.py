from scipy.optimize import broyden1 as bro1
from sympy import *
from sympy.solvers import solve
from sympy.solvers import nsolve

#from sympy.solvers.solveset import nonlinsolve

from sympy import Symbol
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb
from lwz import *

def fr1(x,y=30.):
    return x**2/2.-np.log(x)-y

r=1.
r=4./3.
r=7./5.


r=5./3.

n1=100
n2=100

m=np.arange(n1)/50.
ksi=np.arange(n2)/150.+0.01
ksir1=np.arange(n2)/150.+0.01
fg=np.zeros((n1,n2))
mxin=np.zeros(n1)
mnew=np.zeros(n1)

r0=[4./3.,7./5.,5./3.]
ladas0=[0.7071067811865477,0.625,0.25]

print('yooooooooooooo')
#print(ksi)
plt.figure()
r=1.
ksi1=0.5
ksi0=ksi1
ladas=1.12
lmax=1./ladas
gksi=2*np.log(ksir1)+1./ksir1
for jj in np.arange(n1):
    fm=np.log(1./ladas)+gksi[jj]
    x=Symbol('x')
    jie=solve(exp(x)**2/2.-x-fm)
    #jie0=1.
    #def fr1(x,y=fm):
    #    return x**2/2.-np.log(x)-y
    #jie=bro1(fr1,jie0,f_tol=1e-14)   
    
    jien=jie[0]
    print(np.exp(1))
    print(jien)
    jien=float(jien)
    print('jien',jien)
    mnew[jj]=np.exp(jien)
#pdb.set_trace()
rour1=ladas**(2./(r+1.))*np.exp(mnew)**(-2./(r+1.))*ksir1**(-4./(r+1.))
plt.plot(np.log10(ksir1),np.log10(rour1),label=r'$\gamma$='+str(r))
plt.xlabel(r'$\xi$')
plt.ylabel(r'$\rho/\rho1$')
plt.legend(loc=0)


for kk in [0,1,2]:
    r=r0[kk]
    ladas=ladas0[kk]
    f2g=ladas**(-2.*(r-1.)/(r+1.))
    gksi=ksi**(-1.*(5.-3.*r)/(r+1.))+1./(r-1.)*ksi**(4.*(r-1.)/(r+1.))
    print('!!!!!!!!!!!!!!!!!')
    print(r,ladas)
    for jj in np.arange(n1):
        fm=np.log(f2g)+np.log(gksi[jj])
        x=Symbol('x')
        print(jj)
        #jie=solve(0.5*x**(4./(r+1))+(x**(-2.*(r-1.)/(r+1.)))/(r-1.)-fm,x)
        jie=solve(np.log(0.5)+4./(r+1.)*x+np.log(1./(r-1.))-2.*(r-1.)/(r+1.)*x-fm)
        print('jie',jie)
        mxin[jj]=jie[0]
    rou=ladas**(2./(r+1.))*np.exp(mxin)**(-2./(r+1.))*ksi**(-4./(r+1.))
    #vc1=m*rou**((r-1.)/2.)
    
    plt.plot(np.log10(ksi),np.log10(rou),label=r'$\gamma$='+str(r))
    #plt.yrange()
    plt.xlabel(r'$\xi$')
    plt.ylabel(r'$\rho/\rho1$')
    plt.legend(loc=0)

plt.figure()
r=1.
ksi1=0.5
ksi0=ksi1
ladas=1.12
lmax=1./ladas
vc1r1=mnew*rour1**((r-1.)/2.)
plt.plot(np.log10(ksir1),np.log10(vc1r1),label=r'$\gamma$='+str(r))
plt.xlabel(r'$\xi$')
plt.ylabel(r'$\rho/\rho1$')
plt.legend(loc=0)

for kk in [0,1,2]:
    r=r0[kk]
    ladas=ladas0[kk]
    #rou=ladas**(2./(r+1.))*m**(-2./(r+1.))*ksi**(-4./(r+1.))
    vc1=np.exp(mxin)*rou**((r-1.)/2.)

    plt.plot(np.log10(ksi),np.log10(vc1),label=r'$\gamma$='+str(r))
    plt.ylim(-2.,1.)
    plt.xlabel(r'$\xi$')
    plt.ylabel('v/c1')
    plt.legend(loc=0)
#plt.title('v/c vs xi'+str(r))


plt.show()


