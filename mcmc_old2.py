import matplotlib.pyplot as plt
import matplotlib.axis as ax
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb
import scipy.misc as misc

#set initial conditions
pop=np.array([0.,20.,17.,35.,50.,45.,65.,40.,15.,0.])
k00=3
k0=k00
x1=pop[k0]
nn=1000
j=0
i=1
q=-1
kc=np.zeros(nn)

#loop to decide the step
while j < nn:
    a=np.random.rand(1)   # toss the coin
    
    if a < 0.5: 
        xx=pop[k0+i]
        c=k0+i
    if a >= 0.5: 
        xx=pop[k0-i]
        c=k0-i
    r=xx/x1               # compute R
    if r >= 1.:           # judging R and do corresponding things
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
    k0=city               # take the step and renew all the variables.
    kc[j]=k0
    j=j+1
    x1=x2


#plot the steps friend has taken
plt.figure('step'+str(k00)+str(nn))
plt.title(str(nn)+' steps')
plt.axes([0.7,0.1,0.2,0.8], frameon=False,axisbg=None)
plt.barh(np.arange(np.size(pop)),np.array(pop),color='r',align='center')   
plt.ylim(0,9)
plt.xlabel('city population')
plt.axes([0.1,0.1,0.6,0.8])
plt.plot(np.arange(np.size(kc))+1,kc,'o-')
plt.ylim(0,9)
plt.ylabel('city')
plt.xlabel('step')


#plot the histogram of time spent distribution and population distribution
plt.figure('hist'+str(k00)+str(nn))
hist0,b0,p0=plt.hist(kc-0.25,bins=np.arange(11)-0.5,histtype='bar',label='time spent')
scale=np.size(kc)*1./np.sum(pop)
plt.bar(np.arange(np.size(pop))-0.25,np.array(pop)*scale,width=0.5,color='r',label='population')   
plt.xlabel('city')
plt.ylabel('time spent ( scaled population )')
plt.title('comparison of time spent in cities and their population')
plt.legend(loc=0)

# comparison between different trials, namely different number of steps, different initial values.
plt.figure('bijiao3')
hist0=np.array(hist0)
plt.plot(np.arange(np.size(hist0)),hist0/(pop*scale),'ro',label='start35000')
plt.title('ratio of (time spent)/(scaled population)')
plt.xlabel('city')
plt.ylabel('ratio of (time spent)/(scaled population)')
plt.plot([0.,10],[1,1],'--')
plt.plot([1,2,3,4,5,6,7,8],[1.03,1.04,1.11,1.09,1.04,0.95,0.92,1.19],'bo',label='start17000')
plt.legend(loc=0)
plt.show()    
