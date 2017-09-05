import numpy as np
import matplotlib.pyplot as plt

#set initial parameters
pi=np.pi
c2=(3.E10)**2
hw0=2.
v=0.1
n=100000
n2=1000

epf=np.zeros(n)
ii=0
while (ii < n):
    ep0=0.001*hw0
    beta=0.1
    gamma=(1./(1.-beta**2)**0.5)
    ee0=gamma
    jj=0
    while(jj < n2):
        beta=0.1
        gamma=(1./(1.-beta**2)**0.5)
        ee0=gamma
        theta0=np.random.rand(1)*2*pi
        epm0=ep0*(gamma*(1-beta*np.cos(theta0)))
        #print((gamma*(1-beta*np.cos(theta0))))
        epm1=epm0/(1+(epm0/hw0)*(1-np.cos(theta0)))

        gamma1=gamma-(epm1-ep0)
        beta1=(1-gamma1**-2.)**0.5
        #print(gamma1,gamma1**-2.,(1-gamma1**-2.),beta1)
        theta0=np.random.rand(1)*2*pi
        ep1=epm1*(gamma1*(1-beta1*np.cos(theta0)))
        ee1=ee0+(ep1-ep0)
        #print(ep1,gamma,beta,(gamma*(1-beta*np.cos(theta0))),ee0,ee0+ep0,ep1-epm1,epm1-ep0)
        #        gamma=ee1
        #        beta=(1-1./gamma)**0.5
        #print(ep1-ep0,epm0,epm1,ep1,ep0,beta,beta1,gamma,gamma1)
        ep0=ep1
        jj=jj+1
    print(ii,ep1)
    epf[ii]=ep1
    ii=ii+1    

plt.figure
plt.hist(np.log10(epf))


plt.figure
plt.hist(np.log10(epf), log=True)
plt.show()
