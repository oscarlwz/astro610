import numpy as np
from matplotlib import pyplot as plt


def leapfrog(x,xdot,h,*t):
    #print x,xdot,h
    xmid=x+0.5*h*xdot
    xdotnew=xdot+h*(-1.*xmid)
    xnew=xmid+0.5*h*xdotnew
    return xnew   


#euler
x=1.
y=0.
t=0.
step=2.*np.pi/100.
i=0
xe=np.zeros(1001)
ye=np.zeros(1001)
te=np.zeros(1001)
while(t < 20*np.pi+step):
    xnew=x+y*step
    ynew=-1*x*step+y
    xe[i]=x
    ye[i]=y
    te[i]=t
    x=xnew
    y=ynew
    t=t+step
    i=i+1
plt.figure()
plt.plot(te,np.log10(0.5*(xe**2+ye**2)),label='Euler')
#plt.figure()
#plt.plot(xa,ya,label='dx/dt vs t')


#mid-point

xa=np.zeros(1001)
ya=np.zeros(1001)
ta=np.zeros(1001)
x=1.
y=0.
t=0.
i=0
while(t < 20*np.pi):

    xint=step/2.*y+x 
    yint=-1.*step/2.*x+y

    xnew=x+step*yint
    ynew=y+step*(xint)*-1.
    
    xa[i]=x
    ya[i]=y
    ta[i]=t
    x=xnew
    y=ynew
    t=t+step
    i=i+1



#plt.plot(xa,ya,label='mid point')
plt.plot(ta,np.log10(0.5*(xa**2+ya**2)),label='mid point')
#plt.axes().set_aspect('equal')
#plt.axes().set_ylim(-1.2,1.2)
#plt.xlim(-1.2,1.2)
plt.xlabel("x")
plt.ylabel("dx/dt")
plt.title("exercise 3-2")

x=1.
y=0.
t=0.
i=0

xl=np.zeros(1001)
yl=np.zeros(1001)
tl=np.zeros(1001)


while(t < 20*np.pi+step):
    xl[i]=x
    yl[i]=y
    tl[i]=t
    xnew=leapfrog(x,y,step)
    ynew=leapfrog(y,-1*x,step)
    t=t+step
    x=xnew
    y=ynew
    i=i+1
    
#plt.plot(xl,yl,label='leap frog')

plt.plot(tl,np.log10(0.5*(xl**2+yl**2)),label='leap frog')

plt.figure()
plt.plot(tl,(0.5*(xl**2+yl**2)),label='leap frog')
#plt.axes().set_aspect('equal')
plt.ylim(0.4,0.6)

plt.legend()

plt.show()
