import numpy as np

x=np.array([1,0])
t=np.array([[0.9,0.1],[0.5,0.5]])
i=0
while(i < 200):
    xnew=x.dot(t)
    x=xnew
    print xnew*6.
    i=i+1


