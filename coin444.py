from gauss import gauss as gs
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb
import scipy.misc as misc

for n in [10,100,1000]:
    #n=10
    tt=0.95
    a=np.random.rand(n)
    b=np.zeros(n)
    head=np.where(a > tt)
    tail=np.where(a < tt)
    b[head]=1
    b[tail]=0
    nh=np.size(head)
    nt=np.size(tail)
    
    x=np.arange(n)
    #plt.figure('T='+str(tt)+str(n)+'gs')
    #plt.plot(x,b,'.k')
    #plt.ylim(-0.1,2.)
    #plt.figure('histogram'+str(tt)+str(n)+'gs')
    #plt.hist(b,bins=2)
    #
    #pdata=misc.comb(n,nt)*(tt**nt)*((1.-tt)**nh)
    #pdatanr=1.
    #ptnr=1.
    #pt=pdata*ptnr
    #plt.plot(tt,pt)
    
    nn=501
    t=np.zeros(nn)
    pt=np.zeros(nn)
    plt.figure('TvsP(T)46'+str(tt))
    
    for ii in np.arange(nn):
        t0=1./(nn-1)*ii
        pdata=(t0**nt)*((1.-t0)**nh)
        if t0 >= 0.4 and t0 <=0.6:
            ptnr=1.
        else:
            ptnr=0.
        t[ii]=t0
        pt[ii]=pdata*ptnr 
        print(t0,pdata,t0**nt,(1.-t0)**nh,nt,nh,misc.comb(n,nt))
    plt.subplot(2,3,int(np.log10(n)))
    plt.title('T='+str(tt)+', 0.4-0.6 prior, unnormalized, '+str(n)+' tosses')
    plt.xlabel('T')
    plt.ylabel('p(T|data,N,R)')
    plt.plot(t,pt,'-')
    
    #plt.figure('normalizedtomaxgs'+str(tt)+str(n))
    mp=np.max(pt)
    pt=1./mp*pt
    plt.subplot(2,3,int(np.log10(n))+3)
    plt.plot(t,pt,'-')
    print(pt[0:10])
    plt.title('T='+str(tt)+', 0.4-0.6 prior, normalized to peak, '+str(n)+' tosses')
    plt.xlabel('T')
    plt.ylabel('p(T|data,N,R)')
plt.show()

