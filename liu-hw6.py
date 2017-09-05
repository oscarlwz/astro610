import matplotlib.pyplot as plt
import numpy as np


gg=6.67e-8
c=3.e10
rn=1.e6

msun=2e33
mn=1.4*msun

nn=201
j0=np.arange(nn)/100.-1.
mbh=np.arange(nn)/100.-1.

for k in np.arange(nn):
    j=j0[k]
    z1=1.+(1.-j*j)**(1./3.)*((1.+j)**(1./3.)+(1-j)**(1./3.))
    z2=(3*j*j+z1*z1)**0.5
    fj=gg/c/c*(3+z2+((3-z1)*(3+z1+2*z2))**0.5)
    x=(rn*((2./mn)**(1./3.))/fj)**1.5
    mbh[k]=x/msun
plt.figure
plt.plot(j0,mbh)
plt.xlabel('j')
plt.ylabel('max_BH_mass(solar)') 
plt.show()   
