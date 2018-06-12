#from __future__ import division, print_function
import sys
import numpy as np

def msa(low,high,ksi,dex):
    return ksi*(1./dex)*(high**dex-low**dex)
def mkrs(low,high,ksi,dex):
    return ksi*(1./dex)*(high**dex-low**dex)
def mkrl(low,high,ksi,dex):
    return 0.5*ksi*(1./dex)*(high**dex-low**dex)
def lsa(low,high,ksi):
    dex=2.45
    return ksi*(1./dex)*(high**dex-low**dex)

def lkrs(low,high,ksi):
    dex=3.5
    return ksi*(1./dex)*(high**dex-low**dex)

def lkrl(low,high,ksi):
    dex=2.5
    return 0.5*ksi*(1./dex)*(high**dex-low**dex)




#(2)-b
ksi=1.

#print msa(0.08,100.,1,-2.35)
print msa(0.6,8.,1,-1.35)*0.6/msa(0.08,100,1.,-0.35)

#print (mkrs(0.08,0.5,1,-0.3)+mkrl(0.5,8.,1,-1.3))*0.6/(mkrs(0.1,0.5,1,0.7)+mkrl(0.5,100,1,-0.3))
print mkrl(0.6,8.,1,-1.3)*0.6/(mkrs(0.1,0.5,1,0.7)+mkrl(0.5,100,1,-0.3))
#
#l0=3.828e33/(2e33**(3.8-2.45))
#print lsa(0.08,100.,l0)
#
l02=3.828e33/(2e33**(3.8-3.5))
print lkrs(0.08,0.5,l02)+lkrl(0.5,100,l02)

print 81/0.79*(100**0.79-20**0.79)+1.78/2.15*(20**2.5-2**2.5)+0.75/3.45*(2**3.45-0.8**3.45)

#Lssp, Kroupa, complex L/M
print 0.5*81/0.84*(80**0.84-20**0.84)+0.5*1.78/2.2*(20**2.2-2**2.2)+0.75/4.5*(0.5**4.5-0.08**4.5)+0.5*0.75/3.5*(2**3.5-0.5**3.5)


#salpeter, M/L, simple m/l
lm=0.12
hm=120.
#print msa(0.12,80.,1,-0.35),lsa(0.12,80.,1.),msa(0.12,80.,1,-0.35)/lsa(0.12,80.,1.)
print msa(lm,hm,1,-0.35),lsa(lm,hm,1.),msa(lm,hm,1,-0.35)/lsa(lm,hm,1.)


#Kroupa, M/L, simple m/l
lm=0.08
hm=120.
print (mkrs(lm,0.5,1,0.7)+mkrl(0.5,hm,1,-0.3)),(lkrs(lm,0.5,1)+lkrl(0.5,hm,1)),(mkrs(lm,0.5,1,0.7)+mkrl(0.5,hm,1,-0.3))/(lkrs(lm,0.5,1)+lkrl(0.5,hm,1))

print (0.5**3.5-0.08**3.5)/3.5+(80**2.5-0.5**2.5)/5.
