import numpy as np
import matplotlib.pyplot as plt
from rec import recen as recen
from scipy import signal as sg
pi=np.pi


nn=1280
x=np.arange(nn)/10.
fx=np.zeros(nn)
ind=np.where((x >= 0.) & (x <= 128))
fx[ind]=np.exp(0.15)*(20.)*(np.exp(-10./20.)-np.exp(-127./20.))*np.exp(x[ind]*-0.05)
#fx=np.exp(x*-0.5)
plt.figure()
plt.subplot(2,1,1)
plt.plot(x,fx)

xi=np.zeros(128)
yi=xi
yyi=xi
ii=np.arange(118)+10
xi[10:]=np.exp((-1.*ii+10.)/10.) 
yi[10:]=np.exp((-1.*ii+10.)/20.)
yyi[10:]=np.exp(128-ii-10.)/20.
cc=sg.fftconvolve(xi,yi)
t1=np.fft.fft(xi)
t2=np.fft.fft(yi)

plt.subplot(2,1,2)
plt.plot(np.arange(128),np.fft.ifft(t1*t2))
#print(np.size(cc))
#plt.plot(np.arange(128),cc)

plt.figure('zeros')
x1=np.append(np.zeros(128),xi)
x2=np.append(np.append(np.zeros(64),xi),np.zeros(64))
x3=np.append(xi,np.zeros(128))

y1=np.append(np.zeros(128),yi)
y2=np.append(np.append(np.zeros(64),yi),np.zeros(64))
y3=np.append(yi,np.zeros(128))

print(np.size(x2),np.size(y2),np.size(x3),np.size(y3))
t11=np.fft.fft(x1)
t21=np.fft.fft(y1)
t12=np.fft.fft(x2)
t22=np.fft.fft(y2)
t13=np.fft.fft(x3)
t23=np.fft.fft(y3)

plt.plot(np.arange(256),np.fft.ifft(t11*t21),label='head')
plt.plot(np.arange(256),np.fft.ifft(t12*t22),label='middle')
plt.plot(np.arange(256),np.fft.ifft(t13*t23),'--',label='tail')
plt.legend()

plt.show()

plt.figure('512zeros')
x1=np.append(np.zeros(384),xi)
x2=np.append(np.append(np.zeros(192),xi),np.zeros(192))
x3=np.append(xi,np.zeros(384))

y1=np.append(np.zeros(384),yi)
y2=np.append(np.append(np.zeros(192),yi),np.zeros(192))
y3=np.append(yi,np.zeros(384))

print(np.size(x1),np.size(y1),np.size(x3),np.size(y3))
t11=np.fft.fft(x1)
t21=np.fft.fft(y1)
t12=np.fft.fft(x2)
t22=np.fft.fft(y2)
t13=np.fft.fft(x3)
t23=np.fft.fft(y3)

plt.plot(np.arange(512),np.fft.ifft(t11*t21),label='head')
plt.plot(np.arange(512),np.fft.ifft(t12*t22),label='middle')
plt.plot(np.arange(512),np.fft.ifft(t13*t23),label='tail')
plt.legend()



plt.show()







plt.show()
