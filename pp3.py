import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pdb

#setting initial condition and calculate related numbers
g2=8.
g1=2.
kt=5.0
e=10.4
ekt=np.exp(e/kt)
ekt2=np.exp(-1.*e/kt)

x=0.001
dx=0.001
n10=10000.
n20=0.
n1=n10
n2=n20
t=10.

print(g2*ekt2/(g1+g2*ekt2))
pdb.set_trace()

#do the iteration
num=np.floor(t/dx)-1
plt.figure('f2')
plt.xlabel('x=dt/t0')
plt.ylabel('f2')
plt.plot(x,np.log10(n2/n10),'k.',label='f2(x)')
for i in np.arange(num):
    plt.plot(x,(n2/n10),'k.')
    p12=g2/g1*dx/(ekt-1.)
    p21=ekt/(ekt-1.)*dx
    n1=n1-n1*p12+n2*p21
    n2=n2-n2*p21+n1*p12
    x=x+dx
#plot value of f2 from explicit derivation
plt.plot(np.arange(11),(np.zeros(11)+g2*ekt2/(g1+g2*ekt2)),'r-',label='explicit derivation')
plt.legend(loc=0)


#set A21 to be zero
x=0.001
plt.figure('f2A21=0')
plt.xlabel('x=dt/t0')
plt.ylabel('f2')
plt.plot(x,n2/n10,'ko',label='f2(x)')
for j in np.arange(num):
    plt.plot(x,n2/n10,'ko')
    p12=g2/g1*dx/(ekt-1.)
    p21=1./(ekt-1.)*dx
    n1=n1-n1*p12+n2*p21
    n2=n2-n2*p21+n1*p12
    x=x+dx
#plot value of f2 from explicit derivation
plt.ylim([0.3,0.85])
plt.plot(np.arange(11),np.zeros(11)+g2/(g2+g1),'r-',label='explicit derivation')
plt.legend(loc=0)
plt.show()    
