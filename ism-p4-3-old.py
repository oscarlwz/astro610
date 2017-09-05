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
r=7./5.


r=5./3.

n1=100
n2=100

m=np.arange(n1)/50.
ksi=np.arange(n2)/150.
fg=np.zeros((n1,n2))


ksi1=(5.-3.*r)/4.
#ksi2=0.5
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


#fg=lada**(-2.*(r-1.)/(r+1.))

mxin=np.zeros(n1)


r=5./3.
ladas=0.25 #r=5/3
f2g=ladas**(-2.*(r-1.)/(r+1.))
gksi=ksi**(-1.*(5.-3.*r)/(r+1.))+1./(r-1.)*ksi**(4.*(r-1.)/(r+1.))


print('yooooooooooooo')
print(ladas)
print(ksi)
#for kk in np.arange(n1):
#    fm=f2g*gksi[kk]
#    x=Symbol('x')
#    jie=solve(0.5*x**(4./(r+1))+(x**(-2.*(r-1.)/(r+1.)))/(r-1.)-fm,x)
#    print('jie',jie)
#    mxin[kk]=jie[0]

#plt.figure()
#CS = plt.contour(ksi,m,fg,ll)
#plt.clabel(CS, inline=1, fontsize=10)
#plt.title('Gamma='+str(r))

rou=ladas**(2./(r+1.))*m**(-2./(r+1.))*ksi**(-4./(r+1.))
vc1=m*rou**((r-1.)/2.)

plt.figure()
plt.plot(np.log(ksi),np.log(rou))
plt.xlabel(r'$\xi$')
plt.ylabel(r'$\rho/\rho1$')
#plt.title=('')
plt.figure()
plt.plot(np.log(ksi),np.log(rou))
plt.xlabel(r'$\xi$')
plt.ylabel('v/c1')
#plt.title('v/c vs xi'+str(r))


plt.show()


