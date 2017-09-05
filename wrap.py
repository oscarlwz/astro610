import numpy as np
from clean3 import clean3
from clean4 import clean4
from clean2 import clean2

#nn=[1,2,5,10]

#nn=[1,2,3,4,5]

nn=[10,15,28,30,40,50,60,70,80,90,100,120,150,200]
#lg=[0.05,0.1,0.2,0.3]
lg=[1.]
#lg=[0.1,0.2,0.5]
#fl=[1,2,3,4,5,6]
fl=[6]

for i in np.arange(np.size(nn)):
    for j in np.arange(np.size(lg)):
        for k in np.arange(np.size(fl)):
            #clean4(nn[i],lg[j])
            clean2(nn[i],lg[j],fl[k])
#for i in np.arange(np.size(nn)):
#    for j in np.arange(np.size(lg)):
#        clean3(nn[i],lg[j])
#        clean4(nn[i],lg[j])
