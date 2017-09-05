import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

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


num=np.floor(t/dx)-1
plt.figure('f2')
for i in np.arange(num):
    plt.plot(x,n2/n10,'ko')
    p12=g2/g1*dx/(ekt-1.)
    p21=ekt/(ekt-1.)*dx
    n1=n1-n1*p12+n2*p21
    n2=n2-n2*p21+n1*p12
    #n1=round(n1)
    #n2=n10-n1
    
    #if i < 3000: 
    #   print(x,n1+n2,n1,n2,p12,p21)
    x=x+dx
#plot fraction of f2
    plt.plot(np.arange(10),np.zeros(10)+g2*ekt2/(g1+g2*ekt2),'r-')


#plt.show()
x=0.001
plt.figure('f2A21=0')
for j in np.arange(num):
    plt.plot(x,n2/n10,'ko')
    p12=g2/g1*dx/(ekt-1.)
    p21=1./(ekt-1.)*dx
    n1=n1-n1*p12+n2*p21
    n2=n2-n2*p21+n1*p12
    if j > 2700 and j < 3000:
        print(x,n1,n2,p12,p21)
    x=x+dx
plt.show()    
