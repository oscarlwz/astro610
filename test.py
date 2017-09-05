from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb

#read in fits files
d4 = fits.open('dark_4s.fits')
d1 = fits.open('dark_1min.fits')
f4 = fits.open('flat_4s.fits')
s1 = fits.open('source_clear_1min.fits')

d4.info()
d1.info()
s1.info()
f4.info()
#print((hdulist[0].data)[0])
#plt.imshow(f4[0].data)
#plt.axis('off')  # clear x- and y-axes
#plt.show()
plt.figure('sky')
plt.imshow(s1[0].data)
plt.axis('off')  # clear x- and y-axes
#plt.show()
plt.savefig('/Users/weizheliu/astro610/test.eps')

a1=np.subtract(f4[0].data,d4[0].data)
a2=np.subtract(s1[0].data,d1[0].data)

new=np.true_divide(a2,a1)
a20=np.array(a2)
a10=np.array(a1)
print(a20-a10)

#
print(np.min(s1[0].data))

print(np.min(a2))

print(new)

new1=np.arcsinh(new)
new2=np.log(new)

plt.figure('clean')
plt.imshow(new1)
plt.axis('off')  # clear x- and y-axes
#plt.show()
plt.savefig('/Users/weizheliu/astro610/test2.eps')

plt.figure('clean2')
plt.imshow(new2)
plt.axis('off')  # clear x- and y-axes
#plt.show()
plt.savefig('/Users/weizheliu/astro610/test22.eps')




plt.imshow(f4[0].data)
plt.axis('off')  # clear x- and y-axes
#plt.show()
plt.savefig('/Users/weizheliu/astro610/test3.eps')


hdu=fits.PrimaryHDU(new)
hdu.writeto('xin.fits',clobber=1)
print(new.shape)


new=np.array(new)
new2=np.array(new)
new2[new2 < np.exp(-2.75)]=0.
new3=np.array(new)

#print(np.max(new))
#pdb.set_trace()
#print((new3 > 0).shape)
#print((new3 < np.exp(-2.75)).shape)

#print(np.max(new))
#pdb.set_trace()

#pdb.set_trace()
new3[new3 < 0]=0.
new3[(new3 > np.exp(-2.75))]=0.
#new33=np.intersect1d(new3 > 0,new3 < np.exp(-2.75))
new=np.reshape(new,new.size)

#print(np.max(new))
#pdb.set_trace()

new4=new2[new2 < np.exp(-2.75)]
print(new.shape)
#plt.figure('sky')
#plt.imshow(new2)
print(np.min(new3))

print((new3.shape))
print((new2.shape))
print(new4.shape)
#pdb.set_trace()

print(np.max(new))
#pdb.set_trace()


plt.figure('Nebulae')
plt.imshow(new2)
plt.savefig('/Users/weizheliu/astro610/ne.eps')

plt.figure('sky')
plt.imshow(new3)
plt.savefig('/Users/weizheliu/astro610/sky.eps')


num_bins = 500
print(np.max(new),np.min(new))
# the histogram of the data
#new.info()
#print(new)
print(new.shape)



print('aha',np.size(new))


new=new[new > 0]



plt.figure('histogram')
print(np.size(new))


n, bins, patches = plt.hist(np.log(new), num_bins, range=[-3.2,-2.4])
#n, bins, patches = plt.hist(new, num_bins, normed=1, facecolor='green', alpha=0.5)



# add a 'best fit' line
#y = mlab.normpdf(bins, mu, sigma)
#plt.plot(bins, y, 'r--')
#plt.xlabel('flux')
#plt.ylabel('Number')
#plt.title(r'Histogram of pixels')

# Tweak spacing to prevent clipping of ylabel
#plt.subplots_adjust(left=0.15)
#plt.show()
plt.savefig('/Users/weizheliu/astro610/test4.eps')




data=np.loadtxt("charge.txt")
t=np.arange(0,np.size(data),1)
data=np.array(data)

print(data.dtype)

plt.figure("charge")
line,=plt.plot(t,data,'--',linewidth=3)
#plt.show()


ee=data**(1.0/0.7)
histe,be = np.histogram(ee,bins=20)
#plt.hist
#h=6.626e-34
#niu=ee/h*(10.**(-13))*1.60217662 
print(be.size)
print(histe.shape)
#plt.figure("flux")
#line,=plt.plot(be[:20],histe,'--',linewidth=3)
#plt.show()

lbe=np.log(be[:20])
lhiste=np.log(histe)

plt.figure("flux-log")
line,=plt.plot(lbe,lhiste,'--',linewidth=3)
pp=np.polyfit(lbe,lhiste,1)
plt.plot(lbe,lbe*pp[0]+pp[1],'-',color='r')
print('ok',pp)
#plt.show()

print(be.size,histe.size)
plt.figure("flux2")
line,=plt.plot(be[:20],histe,'--',linewidth=3)
#plt.show()


ae=np.random.rand(2000)*2.+1.

ac=ae**0.7
#=ae**0.7
hista,ba = np.histogram(ae,bins=20)
plt.figure("flux3")
line,=plt.plot(ba[:20],hista,'--',linewidth=3)
#plt.xlabel

plt.figure("flux4")
line,=plt.plot(np.log(ba[:20]),np.log(hista),'-',linewidth=3,color='r')

plt.figure("flux5")
line,=plt.plot(np.log(ba[:20]),np.log(hista),'-',linewidth=3,color='r')

plt.show()


