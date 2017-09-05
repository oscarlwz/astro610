import matplotlib.pyplot as plt
import numpy as np
#from lwz.py import plank
import lwz

plank=lwz.plank

h=6.626E-34
c=3E8
k=1.38E-24

#plt.figure()
#ax=np.arange(30000)/1E9+1E-9
#f=plank(x,t)


#for t in [3000,5800,8000]:
for t in [5800]:
    
    x=np.arange(300000)/1E9+1E-9
    f=plank(x,t)
    
    xb=470E-9
    xv=540E-9
    xh=1.6E-6
    xk=2.2E-6
    
    plt.figure()
    xm=2.897/5800*1E-2
    
    f0=np.max(f)
    print('f0',f0)
    m0=0.
    m=m0-2.5*np.log10(f/f0)
    
    print(np.max(m))
    
    fb=plank(xb,t)
    fv=plank(xv,t)
    fh=plank(xh,t)
    fk=plank(xk,t)
    
    mb=m0-2.5*np.log10(fb/f0)
    mv=m0-2.5*np.log10(fv/f0)
    mh=m0-2.5*np.log10(fh/f0)
    mk=m0-2.5*np.log10(fk/f0)
    
    print('peak wavelength: ',xm)
    print('B-V: ',mb-mv)
    print('H-K: ',mh-mk)
    plt.figure()
    plt.plot(x,f,'k')
    plt.plot([xm,xm],[0,f0],label='peak')
    plt.xlim(0,0.00002)
    plt.title(str(t)+' K')
    plt.xlabel('wavelength(m)')
    plt.ylabel('flux density')
    plt.legend()
    plt.figure()
    plt.plot(x,m,'k')
    plt.plot([xm,xm],[0,1000],label='peak')
    #plt.plot([xb,xb],[0,1000],label='B')
    #plt.plot([xv,xv],[0,1000],label='V')
    #plt.plot([xh,xh],[0,1000],label='H')
    #plt.plot([xk,xk],[0,1000],label='K')
    
    
    plt.ylim(-1,10)
    plt.gca().invert_yaxis()
    #plt.ylim(np.max(m),np.min(m))
    plt.xlim(1E-10,1E-4)
    plt.title(str(t)+' K')
    plt.xlabel('wavelength(m)')
    plt.ylabel('magnitude')
    plt.legend()
plt.show()
