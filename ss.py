import matplotlib.pyplot as plt
import numpy as np

a=np.arange(10)
plt.hist(a,label='MPL-4',color='k',histtype='step')
plt.hist(a,histtype='bar',label='outflow',color='r')
plt.ylim(0,100)
plt.legend()
plt.show()

