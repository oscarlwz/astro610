from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb

#read in data
data=np.loadtxt("charge.txt")

t=np.arange(0,np.size(data),1)
data=np.array(data)

#plot readouts in time sequence
plt.figure("charge")
line,=plt.plot(t,data,'-',linewidth=3)
plt.xlabel('time step')
plt.ylabel('readouts')

#plot spectrum
ee=data
histe,be = np.histogram(ee,bins=20)
plt.figure("flux")
ben=np.array(be[:20])+0.05
#resample in 0.1 Mev channels
line,=plt.plot(ben,histe,'--',linewidth=3)
plt.xlabel('Photon Energy')
plt.ylabel('Flux')

#plot spectrum in log scale
lbe=np.log(ben)
lhiste=np.log(histe)
plt.figure("flux-log")
line,=plt.plot(lbe,lhiste,'--',linewidth=3,label='data')
#linear fit to the data in log scale 
pp=np.polyfit(lbe,lhiste,1)
line2,=plt.plot(lbe,lbe*pp[0]+pp[1],'-',color='r',label='fit')
plt.ylabel('flux')
plt.xlabel('photon energy')
#plt.plot([1,2])
plt.legend()
#print fitting results
print('parameters: ',pp)

#correct for instrument sensitivity E^0.7
histc=histe/(ben**0.7)
plt.figure("flux-corrected")
lhistc=np.log(histc)
line,=plt.plot(lbe,lhistc,'--',linewidth=3,label='data')
plt.ylabel('flux-corrected')
plt.xlabel('photon energy')

#linear fit to the corrected data in log scale 
ppc=np.polyfit(lbe,lhistc,1)
plt.plot(lbe,lbe*ppc[0]+ppc[1],'-',color='r',label='fit')
plt.legend()

#print fitting results
print('parameters: ',ppc)


plt.show()


