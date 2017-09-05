import numpy as np
import matplotlib.pyplot as plt

pi=np.pi
pi2=pi*pi

i0=1.

u=np.arange(10000)*100.-500000.


print(u)
v1a=0.5*i0+np.zeros(np.size(u))
v1b=i0/162000.*pi2*np.sinc(pi*u/162000.)
v1=v1a+v1b

a1=v1
p1=np.zeros(np.size(v1))

print(np.size(v1a),np.size(v1))

v21a=i0/2*np.cos(pi2*u/32400.)
v21b=i0/16200.*pi2*np.sinc(pi*u/162000.)
v21=v21a+v21b
v22=-0.5*i0*np.sin(pi2*u/32400.)

a2=(v21**2+v22**2)**0.5
p2=np.arctan(v22/v21)


v31aa=np.sinc(pi*u/162000.)/162000.
v31bb=0.25*np.sinc(pi*u/21600.)/21600.-0.25*np.sinc(pi*u/64800.)/64800.
v31a=v31aa*i0*pi2
v31b=v31bb*i0*pi2
v31=v31a+v31b
v32=i0/4./pi/u*(np.cos(pi2*u/64800.)-np.cos(pi2*u/21600.))

a3=(v31**2+v32**2)**0.5
p3=np.arctan(v32/v31)


plt.figure()
plt.subplot(2,1,1)
plt.plot(u,a1)
plt.title('amplitude')
plt.subplot(2,1,2)
plt.plot(u,p1)
plt.title('phase')
plt.xlabel('u(arcsec)')
plt.legend()

plt.figure()
plt.subplot(2,1,1)
plt.plot(u,a2)
plt.title('amplitude')
plt.subplot(2,1,2)
plt.plot(u,p2)
plt.title('phase')
plt.xlabel('u(arcsec)')

plt.legend()

plt.figure()
plt.subplot(2,1,1)
plt.plot(u,a3)
plt.title('amplitude')
plt.subplot(2,1,2)
plt.plot(u,p3)
plt.title('phase')
plt.xlabel('u(arcsec)')

plt.legend()


plt.show()


