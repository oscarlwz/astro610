import numpy as np
import matplotlib.pyplot as plt

def recen(x,y):
    x=np.array(x)
    y=np.array(y)
    n=np.size(x)
    kk=np.arange(n)-n/2
    xx=x/np.abs(x[1]-x[0])
    x2=xx-n/2
    xnew=x2*(x[1]-x[0])
    ynew=y[kk]
    return xnew,ynew
