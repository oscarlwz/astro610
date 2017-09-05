import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np


m0=1.
j0=0.

dm=1e-5
m=m0
j=j0
nn=2000000
x=np.zeros(nn)
y=np.zeros(nn)

for i in np.arange(nn):
    a=j*m
    z1=1.+(1.-j*j)**(1./3.)*((1.+j)**(1./3.)+(1-j)**(1./3.))
    z2=(3*j*j+z1*z1)**0.5
    r=m*(3+z2-((3-z1)*(3+z1+2*z2))**0.5)
    
    k11=(m*r)**0.5*(r**2-2.*a*(m*r)**0.5+a*a)
    
    k12=r*(r*r-3*m*r+2*a*(m*r)**0.5)**0.5
    
    k1=k11/k12
    
    k21=2*(r*r-2*m*r+a*(m*r)**0.5)*m*j
    
    k22=r*(r*r-3*m*r+2*a*(m*r)**0.5)**0.5
    
    k2=k21/k22
    k=(k1-k2)/m/m
    dj=k*dm
    m=m+dm
    j=j+dj
    y[i]=m
    x[i]=j
    #print(z1,z2,r,k11,k12,k22,k21)
    print(j,m,i)
plt.figure()
plt.xlim(0.,1.)
plt.ylim(0.,4.)
plt.plot(x,y,'-')
plt.plot([0.9,0.9],[0,10],label='j=0.9')
plt.plot([0.5,0.5],[0,10],label='j=0.5')
plt.legend(loc=0)


plt.xlabel('j')
plt.ylabel('M')
plt.title('prograde')

#print(x)
plt.show()
