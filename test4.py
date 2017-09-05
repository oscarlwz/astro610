from astropy.io import fits
from scipy.optimize import curve_fit
from astropy.table import Table
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb

def gaussian(x, mu, sig, h):
    return h*np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

#read in fits files
d4 = fits.open('dark_4s.fits')
d1 = fits.open('dark_1min.fits')
f4 = fits.open('flat_4s.fits')
s1 = fits.open('source_clear_1min.fits')
ramp=fits.open('ramp.fits')

#plot the image in ramp.fits
plt.figure('ramp')
plt.imshow(ramp[0].data)
plt.axis('off')  # clear x- and y-axes
plt.title('ramp.fits')

#print value at pixel(63,17) in ramp.fits
print((ramp[0].data)[63,17])



#plot the image in source_clear_1min.fits
plt.figure('sky')
plt.imshow(s1[0].data)
plt.axis('off')  # clear x- and y-axes
plt.title('source_clear_1min.fits')
plt.savefig('/Users/weizheliu/astro610/sky.eps')

#plot the image in dark_4s.fits
plt.figure('dark_4s')
plt.imshow(d4[0].data)
plt.axis('off')  # clear x- and y-axes
plt.title('dark_4s.fits')
plt.savefig('/Users/weizheliu/astro610/dark4.eps')

#plot the image in dark_1min.fits
plt.figure('dark_1min')
plt.imshow(d1[0].data)
plt.axis('off')  # clear x- and y-axes
plt.title('dark_1min.fits')
plt.savefig('/Users/weizheliu/astro610/dark1.eps')

#plot the image in flat_4s.fits
plt.figure('flat')
plt.imshow(f4[0].data)
plt.axis('off')  # clear x- and y-axes
plt.title('flat_4s.fits')
plt.savefig('/Users/weizheliu/astro610/flat.eps')


#subtract correspoding dark frames from the images in flat_4s.fits and source_clear_1min.fits 
a1=np.subtract(f4[0].data,d4[0].data)
a2=np.subtract(s1[0].data,d1[0].data)

#after subtract dark: source/flat
new=np.true_divide(a2,a1)
a20=np.array(a2)
a10=np.array(a1)

#rescale the image using arsinh
new1=np.arcsinh(new)
#rescale the image using log
new2=np.log(new)

#plot dark-corrected flat 
plt.figure('flat_corrected')
plt.imshow(a1)
plt.axis('off')  # clear x- and y-axes
plt.title('flat_corrected')
plt.savefig('/Users/weizheliu/astro610/flatc.eps')
print(np.max(1./a1),np.min(1./a1),np.mean(1./a1)/np.min(1./a1))

#plot sky image after dark and flat
#image in arsinh scale
plt.figure('clean')
plt.imshow(new1)
plt.axis('off')  # clear x- and y-axes
plt.title('image after dark and flat: arcsinh scale')
#plt.savefig('/Users/weizheliu/astro610/test2.eps')

#image in log scale
plt.figure('clean2')
plt.imshow(new2)
plt.axis('off')  # clear x- and y-axes
plt.title('image after dark and flat: log scale')
plt.savefig('/Users/weizheliu/astro610/test22.eps')
plt.show()
newnew=np.array(new)
print(new.shape)
print(newnew.shape)

num_bins = 500
print(np.max(new),np.min(new))

# plot the histogram of the data
new=new[new > 0]
plt.figure('histogram')
n, bins, patches = plt.hist(np.log(new), num_bins, label='data',color='k')
plt.title('histogram of pixels')
# use gaussian fit to the data to help distinguish sky, nebulae, junk
popt, pcov = curve_fit(gaussian, bins[:500]+0.0008, n)
plt.plot(bins[:500]+0.0008, gaussian(bins[:500]+0.0008, popt[0], popt[1], popt[2]),color='r',label='gaussian fit')
plt.legend()


#use the gaussian fit to decide the range of sky, nebula: let u and sigma are the mean and sigma of the gaussian profile, pixels with value less than u-2.5*sigma are junk, pixels with value between u-2.5*sigma and u+2.5*sigma are sky, pixels with value larger than u+2.5*sigma are nebula 
cut1=popt[0]+3.*popt[1]
cut2=popt[0]-3.*popt[1]

new2=np.array(newnew)
new2[new2 > np.exp(cut1)]=0.
new2[new2 < np.exp(cut2)]=0.

new3=np.array(newnew)
new3[new3 < np.exp(cut1)]=0.

new4=np.array(newnew)
new4[new4 < np.exp(cut2)]=0.



#plot sky
plt.figure('skynew')
plt.imshow(np.log(new2))
plt.title('sky_pure')
plt.savefig('/Users/weizheliu/astro610/sky.eps')

#plot Nebula
plt.figure('Nebula')
plt.imshow(np.log(new3))
plt.title('Nebula')
plt.savefig('/Users/weizheliu/astro610/ne.eps')

#plot Nebula + sky
plt.figure('Nebula+sky')
plt.imshow(np.log(new4))
plt.title('Nebula+sky')
plt.savefig('/Users/weizheliu/astro610/ne+sky.eps')

plt.show()

