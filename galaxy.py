import numpy as np
import matplotlib.pyplot as plt
from lwz import plankcgs

r0=6.96e10
sigma=5.67051e-5
L0=3.828e33

#all 13 Gyr corrsponding to upper limit of 0.9 solar mass

#lower and upper limit of mass
lm=0.08
hm=100.

wav0=np.linspace(3000,8000,1000)
wav=wav0*1e-8
mass=np.linspace(lm,hm,1000)
sed=np.zeros(1000)

#calculate the totoal spectrum of MW
#by adding up stellar spectra with a
#weight of M^-2.35
for m in mass:
    r=r0*(m**0.7)
    L=L0*(m**3.8)
    T=(L/sigma/4/np.pi/r/r)**0.25
    sed=sed+plankcgs(wav,T)*(m**-2.35)

#plot the spectrum
plt.figure()
plt.plot(wav0,sed)
#plt.title('all stars are 13 Gyr old')
plt.title('all stars on Main Sequence')
plt.xlabel('wavelength ($\AA$)')
plt.ylabel('flux density')
plt.show()
