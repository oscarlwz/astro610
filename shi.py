import numpy as np
import matplotlib.pyplot as plt

a1=7323.2
a2=6524.3
a3=6172.9
a4=5989.1

z=np.arange(10000)/200000.+0.48
b01=4861.
b02=6563/(1/25.-1/4.)*(1/9.-1/4.)
b03=6563/(1/36.-1/4.)*(1/9.-1/4.)
b04=6563/(1/49.-1/4.)*(1/9.-1/4.)
b1=b01*(1+z)
b2=b02*(1+z)
b3=b03*(1+z)
b4=b04*(1+z)

x2=(a1-b1)**2+(a2-b2)**2+(a3-b3)**2+(a4-b4)**2
x2=x2/-2./49.

ind=np.where(x2 == np.max(x2))
print('redshift: ',z[ind])
print('error')

zm=(z[ind])[0]

#for i in np.arange(1000):
    
plt.figure()
plt.plot(z,x2)
plt.plot(z,np.zeros(10000)+np.max(x2)-0.5)
plt.plot(np.zeros(100)+z[ind],-1*np.arange(100),label='z='+str(zm))
plt.plot(z,np.zeros(10000)+np.max(x2)-0.5,label='delta(lnL)=0.5')
plt.plot(np.zeros(100)+0.50488,-1*np.arange(100),label='z-sigma='+str(0.50488))
plt.plot(np.zeros(100)+0.50653,-1*np.arange(100),label='z+sigma='+str(0.50653))
#plt.plot(np.zeros(100)+z[ind],-1*np.arange(100))
plt.xlabel('redshift')
plt.ylabel('ln(L)')
plt.ylim(-20,-1)
plt.xlim(0.5,0.515)
plt.legend(loc=0)
plt.show()
