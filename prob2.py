import matplotlib.pyplot as plt
import numpy as np

g=6.67e-8
c=3e10
msun=2E33
m=1.4*msun
r=1e6
v=np.arange(1001)
w=v*1.*2*np.pi


rs=(2*g*1.4*msun/(c**2))**0.5


s1=(1-2*g*m/r/c/c)
s2=(r*w/c)**2
ef=(s1**2/(s1-s2))**0.5
de=1-ef
de=de*c*c

plt.figure()
plt.plot(v,de)
plt.title('')
plt.xlabel('rotation frequency(Hz)')
plt.ylabel('specific energy released(erg)')



plt.show()
