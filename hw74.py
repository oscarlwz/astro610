import numpy as np
import matplotlib.pyplot as plt

pi=np.pi
f1=1
f2=10
f3=2
f4=4


t=np.arange(1000)/100.-5.001

r11=np.cos(2*pi*t*f3)+np.cos(2*pi*t*f4)
r12=np.sin(2*pi*t*f3)+np.sin(2*pi*t*f4)

plt.figure('1')
plt.subplot(2,1,1)
plt.title('real')
#plt.xlabel('lag')
plt.plot(t,r11)
plt.subplot(2,1,2)

plt.plot(t,-1*r12)
plt.title('imaginary')
plt.xlabel('lag')

r21=f2*np.sinc(2*t*f2)-f1*np.sinc(2*t*f1)
r22=1./2/pi/t*(np.cos(2*pi*t*f2)-np.cos(2*pi*t*f1))



plt.figure('2')
plt.subplot(2,1,1)
plt.plot(t,r21)
plt.title('real')
#plt.xlabel('lag')

#t22=np.arange(2000)/100.-19.9999
#r22=1./2/pi/t*(np.cos(2*pi*t*f2)-np.cos(2*pi*t*f1))

plt.subplot(2,1,2)
plt.plot(t,r22)
plt.xlabel('lag')
plt.title('imaginary')
plt.show()
