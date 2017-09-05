import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pdb

#0 for high mode, 1 for low mode
n=10000
nd=10000
plh=0.2
phl=0.1
h0=10.
x=0.
h=0.
fl=np.zeros(n)-1
th=np.zeros(n)-1.
print(fl,th)
theta=0.
for k in np.arange(n):
    flag=0
    dx=0.02
    dd=dx
    theta=0.
    h=0.
    print('!!!!!!!!!!!!!!',k,theta,flag,dd,)

    for j in np.arange(nd):
        b=np.random.rand(1)
     #   print(flag,dd,h,theta)

        if flag == 0:
            if b < (1.-np.exp(dd/-1.)):

            #if b < (dd/1.):
         #       print('>>>',b,(1.-np.exp(dd/-1.)),b < (1.-np.exp(dd/-1.)))
                dd=dx
                dtheta=np.random.rand(1)*2.*3.14
                theta=dtheta+theta
                h=h+dx*np.sin(theta)
                e=np.random.rand(1)
                if e < phl:
                    flag=1
                else:
                    flag=0
            else:
                h=h+dx*np.sin(theta)
                dd=dd+dx
        if flag == 1:
            if b < (1.-np.exp(dd/-1000.)):
            #if b < (dd/1000.):
                dd=dx
                theta=np.random.rand(1)*2.*3.14        
                h=h+dx*np.sin(theta)
                e=np.random.rand(1)
                if e < plh:
                    flag=0
                else:
                    flag=1
            else:
                dd=dd+dx  
                h=h+dx*np.sin(theta)
        if h >= h0:
            th[k]=(theta/(2*3.14)-np.floor(theta/(2*3.14)))
            fl[k]=flag
            break

high=np.where(fl == 0)
low=np.where(fl == 1)
nhigh=np.size(high)
nlow=np.size(low)


print(nhigh,nlow,nd,h0,dx)
print(nhigh*1./(nhigh+nlow))

th1=th[np.where(th > -0.1)]
fl1=fl[np.where(th > -0.1)]
indl=np.where(fl1 == 1 )
indh=np.where(fl1==0)
plt.figure()
plt.hist(th1[indh]*360.,20,label='high mode')
plt.hist(th1[indl]*360.,20,color='r',label='low mode',histtype='bar')
plt.xlabel('degree')
plt.ylabel('number of escaping photons')
plt.legend(loc=0)
plt.show()

#plt.figure()
#plt.ylabel('number of ')





