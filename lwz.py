import numpy as np
from rec import recen as rec
def cha(ra1,dec1,ra2,dec2):
    c=((ra1-ra2)**2+(dec1-dec2)**2)**0.5*3600
    print((ra1-ra2)*3600)
    print((dec1-dec2)*3600)
    return c
def plank(x,t):
    h=6.626E-34
    c=3E8
    k=1.38E-23
    f0=2*h*c**2/(x**5)/(np.exp(h*c/x/k/t)-1)
    return f0
def plankcgs(x,t):
    h=6.626E-27
    c=3E10
    k=1.38E-16
    f0=2*h*c**2/(x**5)/(np.exp(h*c/x/k/t)-1)
    return f0


#the generalized function I use to shift and subtract and the DB from DM. 
def yi(a,b):
    a=np.array(a)
    b=np.array(b)
    kk=np.arange(np.size(a))
    ina=np.where(a == np.max(a))
    inb=np.where(b == np.max(b))
    d=(ina[0])[0]-(inb[0])[0]
    print('ddd',d)
    if d == 0:
        an=a
    if d > 0:
        kk=kk+d
        tt=np.where(kk < np.size(a))
        kn=kk[tt]
        an=np.append(a[kn],np.zeros(d))
    if d < 0:
        kk=kk-(kk-d)/np.size(kk)*np.size(kk)
        tt=np.where(kk >= 0)
        kn=np.array(kk[tt])
        an=np.append(np.zeros(-1*d),a[kn])
    return b-an

def convolve(a,b):
    #a=np.array(a)
    #b=np.array(b)
    fa=np.fft.fft(a)
    fb=np.fft.fft(b)
    ab=np.fft.ifft(fa*fb)
    ii=np.arange(np.size(ab))
    jj,abnew=rec(ii,ab)
    return abnew
def gauss(x,u,ss):
    x=np.array(x)
    c1=(3.1415*2)**0.5*ss
    c2=(x-u)**2/2./(ss**2)
    g=np.array(np.exp(-1.*c2)/c1)
    print(g.shape)
    return g
def rms(a):
    a=np.array(a)
    r=(np.sum(a**2)/np.size(a))**0.5
    return r

