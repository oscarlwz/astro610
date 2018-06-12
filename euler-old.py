import numpy as np
from matplotlib import pyplot as plt


def leapfrog(x,xdot,h,t=t)
    xmid=x+0.5*h*xdot
    xdotnew=xdot+h*(-1.*xmid)
    xnew=xmid+0.5*h*xdotnew
    
    #ymid=y+0.5*h*-x
    #ydotnew=-x+h*(-1.*ymid)
    #ynew=ymid+0.5*ydotnew

x=1.
y=0.
t=0.
step=2.*np.pi/100.
i=0
xa=np.zeros(101)
ya=np.zeros(101)
ta=np.zeros(101)
while(t < 2*np.pi):
    xnew=x+y*step
    ynew=-1*(x+y)*step+y
    xa[i]=x
    ya[i]=y
    ta[i]=t
    x=xnew
    y=ynew
    t=t+step
    i=i+1
plt.figure()
plt.plot(xa,ya,label='Euler')
#plt.figure()
#plt.plot(ta,ya,label='dx/dt vs t')


xa=np.zeros(101)
ya=np.zeros(101)
ta=np.zeros(101)
x=1.
y=0.
t=0.
i=0
while(t < 2*np.pi):
    #xint=step/2.*y+x   
    #yint=-1.*step/2.*x+y
    #
    #xnew=x+step*yint
    #ynew=y+step*xint*-1.

    #k1=step*y
    #k2=step*(y+k1/2.)
    #xnew=x+k2
    #
    #yk1=step*-1*x
    #yk2=step*-1*(x+step*0.5)
    #ynew=y+yk2


    xint=step/2.*y+x 
    yint=-1.*step/2.*(x+y)+y

    xnew=x+step*yint
    ynew=y+step*(xint+yint)*-1.


    
    xa[i]=x
    ya[i]=y
    ta[i]=t
    x=xnew
    y=ynew
    t=t+step
    i=i+1



plt.plot(xa,ya,label='mid point')
plt.axes().set_aspect('equal')
plt.axes().set_ylim(-1.2,1.2)
plt.xlim(-1.2,1.2)
plt.xlabel("x")
plt.ylabel("dx/dt")
plt.title("exercise 3-2")
plt.legend()
plt.show()
