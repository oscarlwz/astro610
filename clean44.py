import numpy as np
import matplotlib.pyplot as plt
import lwz
import pdb
from scipy import signal


pi=np.pi
n=256
x=np.arange(n)
nn=30
fwhm=5.
num=np.arange(nn)
ii=np.zeros(1)


db=np.sinc(0.05*(x-127))
dm0=np.zeros(n)
dm0[127]=1.
dm0[95]=0.5


dm=signal.fftconvolve(dm0,db,mode='same')



for i in num: 
    if i == 0:
        ii=np.array([i])+1
        
        mch=np.where(np.abs(dm) == np.max(np.abs(dm)))
        mch=(mch[0])[0]
        xm=x[mch]
        xmall=xm
        cb0=lwz.gauss(x,127.5,fwhm/2.35)
        bili=np.max(db)/np.max(cb0)
        cb=cb0*bili
        lg=0.05
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
        mch=np.where(np.abs(res) == np.max(np.abs(res)))
        mch=(mch[0])[0]
        xm=x[mch]
        xmall=np.append(xmall,xm)
        cb0=lwz.gauss(x,127.5,fwhm/2.35)
        bili=np.max(db)/np.max(cb0)
        cb=cb0*bili
        lg=0.05
        lgall=np.append(lgall,lg)
        cc=np.zeros(n)
        cc[mch]=lg
        ccall=ccall+cc
        print('dewf3',ccall)
        cccb=signal.fftconvolve(ccall,cb,mode='same')
        res=lwz.yi(lg*db,res)
        rs=lwz.rms(res)
        rsall=np.append(rsall,rs)
cm=res+cccb
plt.subplot(3,3,1)
plt.title('Dirty map')
plt.plot(x,dm)


plt.subplot(3,3,2)
plt.title('Dirty beam')
plt.plot(x,db)


plt.subplot(3,3,3)
plt.title('Max channel')
plt.plot(ii,xmall,'bo')
plt.plot(ii,xmall)


plt.subplot(3,3,4)
plt.title('Map rms')
plt.plot(ii,rsall)
plt.plot(ii,rsall,'bo')


plt.subplot(3,3,5)
plt.title('Clean components')
plt.plot(x,ccall)
plt.plot(x,ccall,'bo')


plt.subplot(3,3,6)
plt.title('Clean beam')
plt.plot(x,cb)
plt.plot(x,db)

plt.subplot(3,3,7)
plt.title('Clean comp * clean beam')
#plt.plot(x,cccb)
y1=np.zeros(256)
y2=np.zeros(256)
y1[128-10:128+10]=2
y2[128-20:128+20]=4
print(y1)
#plt.plot(x,y1)
#plt.plot(x,y2)
#plt.plot(x,signal.convolve(y1,y2,mode='same'))
plt.plot(x,cccb)

plt.subplot(3,3,8)
plt.title('Residual')
plt.plot(x,res)
plt.subplot(3,3,9)
plt.title('Cleaned map')
plt.plot(x,cm)
plt.show()
