import numpy as np
import matplotlib.pyplot as plt
import lwz
import pdb
from scipy import signal
def clean2(nn,lg0,fl):
    #initial parameters
    plt.figure()
    name='data'+str(fl)
    pi=np.pi
    n=256
    x=np.arange(n)

    fwhm=8.
    num=np.arange(nn)
    ii=np.zeros(1)
    
    #dirty beam and dirty map
    data=np.loadtxt("clean"+str(fl)+"_psdat.dat.txt")

    dm=data[:,0]
    db=data[:,1]
    ori=data[:,2]
    
    for i in num: 
        if i == 0:
            ii=np.array([i])+1
            print(int(n/4.),int(n*0.75)+1)
            #do the clean
            mch=np.where(np.abs(dm) == np.max(np.abs(dm[int(n/4.):int(n*0.75)+1])))
            mch=(mch[0])[0]
            xm=x[mch]
            xmall=xm
            cb0=lwz.gauss(x,127.5,fwhm/2.35)
            bili=np.max(db)/np.max(cb0)
            cb=cb0*bili
            lg=lg0
            lgall=lg
            cc=np.zeros(n)
            cc[mch]=lg
            ccall=cc
            cccb=signal.fftconvolve(ccall,cb,mode='same')
            res=lwz.yi(lg*db,dm)
            
            rs=lwz.rms(res)
            rsall=rs
    
        if i > 0:
            ii=np.append(ii,i+1)
            #do the clean
            mch=np.where(np.abs(res) == np.max(np.abs(res[int(n/4.):int(n*0.75)+1])))
            mch=(mch[0])[0]
            xm=x[mch]
            xmall=np.append(xmall,xm)
            cb0=lwz.gauss(x,127.5,fwhm/2.35)
            bili=np.max(db)/np.max(cb0)
            cb=cb0*bili
            lg=lg0
            lgall=np.append(lgall,lg)
            cc=np.zeros(n)
            cc[mch]=lg
            ccall=ccall+cc
            cccb=signal.fftconvolve(ccall,cb,mode='same')
            res=lwz.yi(lg*db,res)
            rs=lwz.rms(res)
            rsall=np.append(rsall,rs)
    cm=res+cccb
    #plot all figures out
    plt.tick_params(labelsize=20)
    plt.subplot(3,3,1)
    plt.title('Dirty map')
    plt.plot(x,dm)
    plt.tick_params(labelsize=10)
    
    plt.subplot(3,3,2)
    plt.title('Dirty beam')
    plt.plot(x,db)
    plt.tick_params(labelsize=10)
    
    plt.subplot(3,3,3)
    plt.title('Max channel')
    plt.plot(ii,xmall,'bo')
    plt.plot(ii,xmall)
    plt.tick_params(labelsize=10)
    
    plt.subplot(3,3,4)
    plt.title('Map rms')
    plt.plot(ii,rsall)
    plt.plot(ii,rsall,'bo')
    plt.tick_params(labelsize=10)
    
    plt.subplot(3,3,5)
    plt.title('Clean components')
    plt.plot(x,ccall)
    plt.plot(x,ccall,'bo')
    plt.tick_params(labelsize=10)

    plt.subplot(3,3,6)
    plt.title('Clean beam')
    plt.plot(x,cb)
    plt.plot(x,db)
    plt.tick_params(labelsize=10)

    plt.subplot(3,3,7)
    plt.title('Clean comp * clean beam')
    y1=np.zeros(256)
    y2=np.zeros(256)
    y1[128-10:128+10]=2
    y2[128-20:128+20]=4
    plt.tick_params(labelsize=10)
    plt.plot(x,cccb)

    plt.subplot(3,3,8)
    plt.title('  Residual')
    plt.plot(x,res)
    plt.tick_params(labelsize=10)

    plt.subplot(3,3,9)
    plt.title('Cleaned map')
    plt.plot(x,cm)
    os=np.max(cm)/np.max(ori)
    plt.plot(x,ori*os)
    plt.tight_layout()
    plt.tick_params(labelsize=10)
    plt.savefig('/Users/weizheliu/Documents/'+name+'-'+str(lg0)+'-'+str(nn)+'.png')
