import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np

plt.figure()
#dt=ts*(1-x)*dy
for j in np.arange(100):
    plt.plot(j,j*2,'b.')
#plt.xlim(0.94,0.9914)    
plt.show()

