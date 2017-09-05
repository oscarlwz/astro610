import numpy as np
import matplotlib.pyplot as plt

#set initial parameters
pi=np.pi
hw0=1.  #set the energy of electron at rest to be 1    
n=100000
n2=10

epf=np.zeros(n)
ii=0
while (ii < n):
    ep0=0.001*hw0     #initialize and photon energy   
    jj=0
    print(ii)
    while(jj < n2):
        beta=0.1        
        gamma=(1./(1.-beta**2)**0.5) #initialize electron velocity
        cost=np.random.rand(1)*2.-1.
        epm0=ep0*(gamma*(1-beta*cost))
        cost2=(cost+beta)/(1+beta*cost)
        epm1=epm0/(1+(epm0/hw0)*(1-cost))#doppler boost for photon before collision 
        epm1=epm0/(1+(epm0/hw0)*(1-cost2))
        gamma1=gamma-(epm1-ep0) #update energy of electron right after collision  
        beta1=(1-gamma1**-2.)**0.5
        #calculate new angle between photon and electron
        cost3=np.random.rand(1)*2.-1.
        phi=np.random.rand(1)*2*pi
        cosphi=np.cos(phi)
        cost4=(cost3**2+cosphi**2)**0.5
        ep1=epm1*(gamma1*(1-beta1*cost4))# doppler boost for photon after collision
        ep0=ep1
        jj=jj+1
    epf[ii]=ep1 #record the photon energy
    ii=ii+1    

plt.figure

nb=np.fix(np.max(np.log10(epf))-np.min(np.log10(epf)))/0.1+1
plt.hist(np.log10(epf), log=True,bins=100)
plt.title('comptonization_'+str(n2)+'scatterings')
plt.xlabel('log(energy)')
plt.ylabel('number of photons')
plt.show()
