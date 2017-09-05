import numpy as np

def sinc(x,u,ss):
    c1=(3.1415*2)**0.5*ss
    c2=(x-u)**2/2./(ss**2)
    g=np.array(np.exp(-1.*c2)/c1)
    return[g]

