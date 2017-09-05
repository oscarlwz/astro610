import numpy as np

def rms(a):
    r=(np.sum(a^2)/np.size(a))**0.5
    return[r]
    


