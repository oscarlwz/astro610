import numpy as np
import matplotlib.pyplot as plt
from rec import recen as recen
pi=np.pi
nn=512.
cyc=30.
ll=1.
x=ll*np.arange(nn)*cyc*2.*pi/nn
fx=np.cos(x)
plt.figure('1')
plt.subplot(4,1,1)
plt.plot(x,fx,label='data')
plt.title('data')

fu=np.fft.fft(fx)
u=np.arange(nn)
plt.subplot(4,1,2)
plt.plot(u,fu.real,label='real')
plt.plot(u,fu.imag,label='imag')
plt.legend(loc=9)

t,ftr=recen(u,fu.real)
t2,ftr2=recen(u,fu.imag)

plt.subplot(4,1,3)
plt.plot(t,ftr,label='real')
plt.plot(t,ftr2,label='imag')
plt.legend(loc=0)

plt.subplot(4,1,4)
amp=((ftr.real)**2+(ftr.imag)**2)
plt.plot(t,amp,label='power')
plt.legend()

plt.show()
