import numpy as np
import matplotlib.pyplot as plt

pi=np.pi
a=200.

x=np.arange(1000)/10000.-0.05
plt.figure()

plt.xlabel('theta')
plt.ylabel('power')
plt.plot(x,(a*np.sinc(100*x))**2,label='grade1')
plt.plot(x,(a*(np.sinc(100*x+a/200./pi)))**2,label='grade2')
plt.plot(x,(a*(np.sinc(100*x+a/40./pi)))**2,label='grade3')


y41=400*pi*x/a*np.sin(100*pi*x)-0.02*np.sin(a/200.)
y42=2/100.*(np.cos(a/200.)-np.cos(pi*x*100.))
y43=(200.*pi*x/a)**2-0.0001
y4=(y41**2+y42**2)/(y43**2)

plt.plot(x,y4,'--k',label='grade4')

y5=0.5*a*np.sinc(0.5+100*x)+0.5*a*np.sinc(100*x-0.5)
plt.plot(x,y5**2,'orange',label='grade5')
y6=0.5*a*(np.sinc(100*x+0.5)+np.sinc(100*x-0.5))-0.25*a*(np.sinc(50*x+0.25)+np.sinc(50*x-0.25))
plt.plot(x,y6**2,'k',label='grade6')
plt.legend()

plt.show()
print(a)
