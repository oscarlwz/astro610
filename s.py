import matplotlib.pyplot as plt
import numpy as np
gg=6.67e-8
c=3.e10
pc=3.086e18



v=10*1e5
n=1000./(pc**3)
ms=2*1.4*2e33
nn=1e5

#v=100*1e5
#n=1000./(pc**3)
#ms=2*1.4*2e33
#nn=1e4


kk=(2*1.37e10/1.e6)**3*0.003

r=1e6
sigma=np.pi*r*(2.*gg*ms/v/v)
rr=nn*n*v*sigma/2.
rr2=rr*3600.*24.*kk
#wiki pedia: 1e-4 to 1e-6
print(r,kk,rr,rr2)



x=20
y=2**0.5*(x-1-np.log(x))**0.5

print(y)
