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
print(s1,s2)

#plt.figure()
#plt.plot(v,de)
#plt.title('')
#plt.xlabel('rotation frequency(Hz)')
#plt.ylabel('specific energy released(erg)')

plt.figure()

x=np.arange(1000)/500.
y=((1-2./x)*(1-9./8.*(1-2./x)*(1+4./x/x)))**2
y2=(27./2.)**0.5*(1-2./x)/x

y3=(2.-2./x)/(1-2./x)
plt.plot(x,(y3))
#plt.plot(x,(y2))


plt.show()
print(rs)
