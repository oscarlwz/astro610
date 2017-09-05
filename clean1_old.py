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
lg0=0.05

#data=np.loadtxt("clean2_psdat.dat.txt")

#dm=data[:,0]
#db=data[:,1]
#ori=data[:,2]
db=np.sinc(0.2*(x-127))
dm=np.sinc(0.2*(x-127))+0.5*np.sinc(0.2*(x-95))

#cb=lwz.gauss(x,xm,fwhm/2.35)

print(num)
#plt.figure()

for i in num: 
    if i == 0:
        ii=np.array([i])+1
        
        print(dm.shape)
        mch=np.where(np.abs(dm) == np.max(np.abs(dm)))
        print(np.max(dm))
        print(mch,(mch[0])[0])
        print('fwrfw',(mch[0])[0])
        mch=(mch[0])[0]
        xm=x[mch]
        xmall=xm
        print('asdwe',xm)
        cb0=lwz.gauss(x,127.5,fwhm/2.35)
        bili=np.max(db)/np.max(cb0)
        cb=cb0*bili
        lg=lg0
        lgall=lg
        cc=np.zeros(n)
        cc[mch]=lg
        ccall=cc
        #cccb=lwz.convolve(ccall,cb)
        cccb=signal.fftconvolve(ccall,cb,mode='same')
        res=lwz.yi(lg*db,dm)
        #res=dm-lg*db
        
        rs=lwz.rms(res)
        rsall=rs
        print(xm)

    if i > 0:
        ii=np.append(ii,i+1)
        #dbdm=lwz.convolve(res,dm)

        mch=np.where(np.abs(res) == np.max(np.abs(res)))
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
        print('dewf3',ccall)
        #cb=lwz.gauss(x,xm,fwhm/2.35)
        #cccb=lwz.convolve(cb,ccall)
        cccb=signal.fftconvolve(ccall,cb,mode='same')
        #res=res-lg*db
        res=lwz.yi(lg*db,res)
        rs=lwz.rms(res)
        rsall=np.append(rsall,rs)
        print('!!!!!!!!!!!!!!',np.max(cb))
plt.figure('')
plt.title('loopgain='+str(lg0))
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
#os=np.max(cm)/np.max(ori)
#plt.plot(x,ori*os)
#print(os)
plt.show()
