import matplotlib.pyplot as plt
import matplotlib.axis as ax
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb
import scipy.misc as misc


pop=[0.,20.,17.,35.,50.,45.,65.,40.,15.,0.]
k00=2
k0=k00
x1=pop[k0]
nn=1000
j=0
i=1
q=-1
kc=np.zeros(nn)
while j < nn:
    a=np.random.rand(1)
    
    if a < 0.5: 
        xx=pop[k0+i]
        c=k0+i
    if a >= 0.5: 
        xx=pop[k0-i]
        c=k0-i
    r=xx/x1
    if r >= 1.:
        x2=xx
        city=c
    if r < 1.:
        q=np.random.rand(1)
        if q < r:
            x2=xx
            city=c
        if q >= r: 
            x2=x1
            city=k0
    k0=city
    kc[j]=k0
    j=j+1
    x1=x2
    print(k0,a,r,q)
#plt.subplots(1,2,sharey=True)
#plt.axes([0.2,0.2,0.8,0.8])
#plt.plot(np.arange(np.size(kc))+1,kc,'.-.')    
plt.figure('step'+str(k00)+str(nn))

plt.title(str(nn)+' steps')
plt.axes([0.7,0.1,0.2,0.8], frameon=False,axisbg=None)
#ax.Tick(label1On=False)
#.yticks([])
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are off
#plt.barh(np.arange(np.size(pop)),np.array(pop),color='r',align='center')   
#plt.ylim(0,9)
#plt.xlabel('city population')
#plt.axes([0.1,0.1,0.6,0.8])
#plt.tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off')
#plt.xticks([]), plt.yticks([])
#plt.plot(np.arange(np.size(kc))+1,kc,'o-')
#plt.ylim(0,9)
#plt.ylabel('city')
#plt.xlabel('step')


plt.figure('hist'+str(k00)+str(nn))


plt.hist(kc-0.25,bins=np.arange(11)-0.5,histtype='bar',label='time spent')
#plt.hist(kc,10,histtype='bar')

scale=np.size(kc)*1./np.sum(pop)
plt.bar(np.arange(np.size(pop))-0.25,np.array(pop)*scale,width=0.5,color='r',label='population')   
plt.xlabel('city')
plt.ylabel('time spent / scaled population')
plt.title('comparison of time spent in cities and their population')
plt.legend(loc=0)

#plt.plot(np.arange(np.size(pop)),np.array(pop)*scale,'r')
plt.show()    
