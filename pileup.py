from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb
import scipy.stats as scs

#read in data
data=np.loadtxt("charge.txt")

t=np.arange(0,np.size(data),1)
data=np.array(data)

#create poisson array
po1=np.random.poisson(lam=1.,size=1E6)
po2=np.random.poisson(lam=0.1,size=1E6)
po3=np.random.poisson(lam=0.01,size=1E6)
po4=np.random.poisson(lam=0.001,size=3E6)





#pile up
#print(po1)
#print(data[0:20])
pu1=np.zeros(1e6)
pu2=np.zeros(1e6)
pu3=np.zeros(1e6)
pu4=np.zeros(3e6)
print(np.min(po2))


ii=0
j=0
for i in np.arange(np.size(po1)): 
#    print('haha ',po1[i])
    k=0
    if po1[i] > 0 and j < np.size(data)-1:
        print('ca',po1[i])
        while (k < po1[i] and j+k < np.size(data)-1):
            pu1[ii]=pu1[ii]+data[j+k]
            print(ii,j,k)
            k=k+1
        print(k)
        j=j+k
        ii=ii+1
print(j)
ii=0
j=0
for i in np.arange(np.size(po2)):
    k=0
    if po2[i] > 0 and j < np.size(data)-1:
        while (k < po2[i] and j+k < np.size(data)-1):
            pu2[ii]=pu2[ii]+data[j+k]
            k=k+1
#        print('yi?',j,po2[i])
        j=j+k
        ii=ii+1
print(j)

print(data[0:20])
print(po1[0:20])
print(pu1[0:20])

#pdb.set_trace()


ii=0
j=0
for i in np.arange(np.size(po3)):
    k=0
    if po3[i] > 0 and j < np.size(data)-1:
        while (k < po3[i] and j+k < np.size(data)-1):
            pu3[ii]=pu3[ii]+data[j+k]
            k=k+1
        j=j+k
        ii=ii+1
print(j)

ii=0
j=0
for i in np.arange(np.size(po4)):
    k=0
    if po4[i] > 0 and j < np.size(data)-1:
        while (k < po4[i] and j+k < np.size(data)-1):
            pu4[ii]=pu4[ii]+data[j+k]
            #print('heihei ',ii,j,k,i)
            k=k+1
        j=j+k
        ii=ii+1
print(j)

pu1=pu1[np.where(pu1 > 0.)]
pu2=pu2[np.where(pu2 > 0.)]
pu3=pu3[np.where(pu3 > 0.)]
pu4=pu4[np.where(pu4 > 0.)]
print(po1)
print(np.min(po1))



#plot spectrum
ee=data
histe,be = np.histogram(ee,bins=20)
ben=np.array(be[:20])+0.05

num_bins=20
plt.figure('histogram')
n = plt.hist(ee, num_bins)

#plot spectrum in log scale
lbe=np.log(ben)
lhiste=np.log(histe)
plt.figure("flux-log")
line,=plt.plot(lbe,lhiste,'--',linewidth=3,label='data')
#linear fit to the data in log scale 
indf=np.isfinite(lhiste)
lhiste=lhiste[indf]
lbe=lbe[indf]
pp=np.polyfit(lbe,lhiste,1)
line2,=plt.plot(lbe,lbe*pp[0]+pp[1],'-',color='r',label='fit')
plt.ylabel('flux')
plt.xlabel('photon energy')
plt.legend()
print('parameters: ',pp)




#plot spectrum
ee=pu1
#pdb.set_trace()
num_bins=20
plt.figure('histogram-1us')
n = plt.hist(ee, num_bins)

histe,be = np.histogram(ee,bins=20)
plt.figure("flux-1us")
ben=np.array(be[:20])+0.05
#resample in 0.1 Mev channels
line,=plt.plot(ben,histe,'ro',linewidth=3)
plt.xlabel('Photon Energy')
plt.ylabel('Flux')

#plot spectrum in log scale
lbe=np.log(ben)
lhiste=np.log(histe)
plt.figure("flux-log-1us")
line,=plt.plot(lbe,lhiste,'ko',linewidth=3,label='data')
#linear fit to the data in log scale 

indf=np.isfinite(lhiste)
lhiste=lhiste[indf]
lbe=lbe[indf]
pp=np.polyfit(lbe,lhiste,1)
line2,=plt.plot(lbe,lbe*pp[0]+pp[1],'-',color='r',label='fit')
plt.ylabel('flux')
plt.xlabel('photon energy')
plt.legend()
print('parameter2s: ',pp)

#pp2,  pp3=scs.linregress(lbe,lhiste)
#line3,=plt.plot(lbe,lbe*pp2+pp3,'-',color='g',label='fit2')



plt.figure("poisson1")
n=plt.hist(po1, 20, log=1)
print(i)
print(j)
plt.figure("poisson2")
n=plt.hist(po2, 20, log=1)

plt.figure("poisson3")
n=plt.hist(po3, 20, log=1)

plt.figure("poisson4")
n=plt.hist(po4, 20, log=1)

#plt.show()
#pdb.set_trace()


#plot spectrum
ee=pu2
#pdb.set_trace()
num_bins=20
plt.figure('histogram-10us')
n = plt.hist(ee, num_bins)

histe,be = np.histogram(ee,bins=20)
plt.figure("flux-10us")
ben=np.array(be[:20])+0.05
#resample in 0.1 Mev channels
line,=plt.plot(ben,histe,'ro',linewidth=3)
plt.xlabel('Photon Energy')
plt.ylabel('Flux')

#plot spectrum in log scale
lbe=np.log(ben)
lhiste=np.log(histe)
plt.figure("flux-log-10us")
line,=plt.plot(lbe,lhiste,'ko',linewidth=3,label='data')
#linear fit to the data in log scale 
indf=np.isfinite(lhiste)
lhiste=lhiste[indf]
lbe=lbe[indf]

pp=np.polyfit(lbe,lhiste,1)
line2,=plt.plot(lbe,lbe*pp[0]+pp[1],'-',color='r',label='fit')
plt.ylabel('flux')
plt.xlabel('photon energy')
plt.legend()
print('parameters: ',pp)
#pp2, pp3=scs.linregress(lbe,lhiste)
#line3,=plt.plot(lbe,lbe*pp2+pp3,'-',color='g',label='fit2')


#plot spectrum
ee=pu3
#pdb.set_trace()
num_bins=20
plt.figure('histogram-100us')
n = plt.hist(ee, num_bins)

histe,be = np.histogram(ee,bins=20)
plt.figure("flux")
ben=np.array(be[:20])+0.05
#resample in 0.1 Mev channels
line,=plt.plot(ben,histe,'ro',linewidth=3)
plt.xlabel('Photon Energy')
plt.ylabel('Flux')

#plot spectrum in log scale
lbe=np.log(ben)
lhiste=np.log(histe)
plt.figure("flux-log-100us")
line,=plt.plot(lbe,lhiste,'ko',linewidth=3,label='data')
#linear fit to the data in log scale 
indf=np.isfinite(lhiste)
lhiste=lhiste[indf]
lbe=lbe[indf]
pp=np.polyfit(lbe,lhiste,1)
line2,=plt.plot(lbe,lbe*pp[0]+pp[1],'-',color='r',label='fit')
plt.ylabel('flux')
plt.xlabel('photon energy')
plt.legend()
print('parameters: ',pp)
#pp2, pp3=scs.linregress(lbe,lhiste)
#line3,=plt.plot(lbe,lbe*pp2+pp3,'-',color='g',label='fit2')


#plot spectrum
ee=pu4
#pdb.set_trace()
num_bins=20
plt.figure('histogram-1000us')
n = plt.hist(ee, num_bins)

histe,be = np.histogram(ee,bins=20)
plt.figure("flux")
ben=np.array(be[:20])+0.05
#resample in 0.1 Mev channels
line,=plt.plot(ben,histe,'ro',linewidth=3)
plt.xlabel('Photon Energy')
plt.ylabel('Flux')

#plot spectrum in log scale
lbe=np.log(ben)
lhiste=np.log(histe)
plt.figure("flux-log-1000us")
line,=plt.plot(lbe,lhiste,'ko',linewidth=3,label='data')
#linear fit to the data in log scale 
indf=np.isfinite(lhiste)
lhiste=lhiste[indf]
lbe=lbe[indf]
pp=np.polyfit(lbe,lhiste,1)
line2,=plt.plot(lbe,lbe*pp[0]+pp[1],'-',color='r',label='fit')
plt.ylabel('flux')
plt.xlabel('photon energy')
plt.legend()
print('parameters: ',pp)
#pp2, pp3=scs.linregress(lbe,lhiste)
#line3,=plt.plot(lbe,lbe*pp2+pp3,'-',color='g',label='fit2')






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
print('parameters_cor: ',ppc)


plt.show()


