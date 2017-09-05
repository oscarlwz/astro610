import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np


n0=100.
sm=6.4e-18
a2=3.09e-13
co=['b','r']
i=0
plt.figure()
plt.title('ionization fraction vs radius')
plt.xlabel('r(pc)')
plt.ylabel('x')
la=['O5','B0']
for nu in [51e48,0.43e48]:
    
    x0=1.
    x1=6.4e-18
    
    rs=(3.*nu/4./np.pi/n0/n0/a2)**(1./3.)
    ts=sm*n0*rs
    print('ts   ',rs,ts)
    dy=-0.0001
    x=0.0
    y=1.
    t=100.
    print(t,t*np.exp(-1*t))
    xt=np.zeros(10001)
    yt=np.zeros(10001)
    
    for j in np.arange(10000):
        k=np.exp(-1*t)*ts/y/y
        x=(-1.*k+(k*k+12*k)**0.5)/6.
        dt=ts*(1-x)*dy
        t=t+dt
        y=y+dy
        yt[j+1]=y
        xt[j+1]=x
    rs0=rs/(3.e18)    
    plt.plot(yt*rs0,xt,co[i],label=la[i])
    i=i+1


plt.xlim(0.0,7.)
plt.ylim(0.0,1.1)
plt.legend(loc=0)

plt.show()

