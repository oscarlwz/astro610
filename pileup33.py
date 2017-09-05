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

pu1=np.zeros(1e6)
pu2=np.zeros(1e6)
pu3=np.zeros(1e6)
pu4=np.zeros(3e6)


#do the simulated "pile up"
ii=0
j=0
for i in np.arange(np.size(po1)): 
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
ii=0
j=0
for i in np.arange(np.size(po2)):
    k=0
    if po2[i] > 0 and j < np.size(data)-1:
        while (k < po2[i] and j+k < np.size(data)-1):
            pu2[ii]=pu2[ii]+data[j+k]
            k=k+1
        j=j+k
        ii=ii+1


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

ii=0
j=0
for i in np.arange(np.size(po4)):
    k=0
    if po4[i] > 0 and j < np.size(data)-1:
        while (k < po4[i] and j+k < np.size(data)-1):
            pu4[ii]=pu4[ii]+data[j+k]
            k=k+1
        j=j+k
        ii=ii+1

pu1=pu1[np.where(pu1 > 0.)]
pu2=pu2[np.where(pu2 > 0.)]
pu3=pu3[np.where(pu3 > 0.)]
pu4=pu4[np.where(pu4 > 0.)]


#plot histograms of the spectra
plt.figure('histogram')
ee=data
histe,be = np.histogram(ee,bins=20,range=[1.,3.])
ben=np.array(be[:20])+0.05
num_bins=20
n = plt.hist(ee, num_bins)

ee=pu1
histe1,be = np.histogram(ee,bins=20,range=[1.,3.])
ben1=np.array(be[:20])+0.05
num_bins=20
n = plt.hist(ee, num_bins)

ee=pu2
histe2,be = np.histogram(ee,bins=20,range=[1.,3.])
ben2=np.array(be[:20])+0.05
num_bins=20
n = plt.hist(ee, num_bins)
print(np.size(be))


ee=pu3
histe3,be = np.histogram(ee,bins=20,range=[1.,3.])
ben3=np.array(be[:20])+0.05
num_bins=20
n = plt.hist(ee, num_bins)
print(np.size(be))


ee=pu4
histe4,be = np.histogram(ee,bins=20,range=[1.,3.])
ben4=np.array(be[:20])+0.05
num_bins=20
n = plt.hist(ee, num_bins)


#plot spectrum in log scale
lbe=np.log(ben)
lhiste=np.log(histe)
plt.figure("flux-log-zoom")
plt.axis=([0.,1.2,0.,7.])

line,=plt.plot(lbe,lhiste,marker='o',color='k',linestyle='-',linewidth=3,label='data',)

#linear fit to the data in log scale 
indf=np.isfinite(lhiste)
lhiste=lhiste[indf]
lbe=lbe[indf]
xiao=np.where(lbe < np.log(3.))
lbe=lbe[xiao]
lhiste=lhiste[xiao]
pp=np.polyfit(lbe,lhiste,1)
line2,=plt.plot(lbe,lbe*pp[0]+pp[1],'-',color='r')
plt.ylabel('flux')
plt.xlabel('photon energy')
plt.legend()
print('parameters: ',pp)


#plot spectrum in log scale
lbe=np.log(ben1)
lhiste=np.log(histe1)
line,=plt.plot(lbe,lhiste,marker='o',color='b',linestyle='-',linewidth=3,label='data_1us')
#linear fit to the data in log scale 
indf=np.isfinite(lhiste)
lhiste=lhiste[indf]
lbe=lbe[indf]
xiao=np.where(lbe < np.log(3.))
lbe=lbe[xiao]
lhiste=lhiste[xiao]
pp=np.polyfit(lbe,lhiste,1)
line2,=plt.plot(lbe,lbe*pp[0]+pp[1],'-',color='r')
plt.ylabel('flux')
plt.xlabel('photon energy')
plt.legend()
print('parameters: ',pp)

lbe=np.log(ben2)
lhiste=np.log(histe2)
line,=plt.plot(lbe,lhiste,marker='o',color='c',linestyle='-',linewidth=3,label='data_10us')
#linear fit to the data in log scale 
indf=np.isfinite(lhiste)
lhiste=lhiste[indf]
lbe=lbe[indf]
xiao=np.where(lbe < np.log(3.))
lbe=lbe[xiao]
lhiste=lhiste[xiao]

pp=np.polyfit(lbe,lhiste,1)
line2,=plt.plot(lbe,lbe*pp[0]+pp[1],'-',color='r')
plt.ylabel('flux')
plt.xlabel('photon energy')
plt.legend(loc=0)
print('parameters: ',pp)
lbe=np.log(ben3)
lhiste=np.log(histe3)
line,=plt.plot(lbe,lhiste,marker='o',color='y',linestyle='-',linewidth=3,label='data_100us')

#linear fit to the data in log scale 
indf=np.isfinite(lhiste)
lhiste=lhiste[indf]
lbe=lbe[indf]
xiao=np.where(lbe < np.log(3.))
lbe=lbe[xiao]
lhiste=lhiste[xiao]
pp=np.polyfit(lbe,lhiste,1)
line2,=plt.plot(lbe,lbe*pp[0]+pp[1],'-',color='r')
plt.ylabel('flux')
plt.xlabel('photon energy')
plt.legend()
print('parameters: ',pp)

#plot spectrum in log scale
lbe=np.log(ben4)
lhiste=np.log(histe4)
line,=plt.plot(lbe,lhiste,marker='o',color='g',linestyle='-',linewidth=3,label='data_1000us')
#linear fit to the data in log scale 
indf=np.isfinite(lhiste)
lhiste=lhiste[indf]
lbe=lbe[indf]
xiao=np.where(lbe < np.log(3.))
lbe=lbe[xiao]
lhiste=lhiste[xiao]
pp=np.polyfit(lbe,lhiste,1)
line2,=plt.plot(lbe,lbe*pp[0]+pp[1],'-',color='r',label='fit')
plt.ylabel('flux')
plt.xlabel('photon energy')
plt.legend()
print('parameters: ',pp)

#show image
plt.show()





