from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb


t1 = Table.read('NGC5548', format='ascii.ipac')
t2 = Table.read('IIZW40', format='ascii.ipac')
t3 = Table.read('MRK273', format='ascii.ipac')
t4 = Table.read('cassis_NGC520.tbl', format='ascii.ipac')
#t4=fits.open('cassis_NGC1569.fits')
t4.info()


#pdb.set_trace

fig=plt.figure("irs")
#ax = fig.gca()
#ax.set_autoscale_on(False)

#line1,=plt.plot(t1['wavelength'],np.log10(t1['flux_density']),'-',linewidth=3,color='b',label='AGN')
#line2,=plt.plot(t2['wavelength'],0.2+np.log10(t2['flux_density']),'-',linewidth=3,color='r',label='BCD')
#line3,=plt.plot(t3['wavelength'],np.log10(t3['flux_density']),'-',linewidth=3,color='y',label='ULIRG')
line4,=plt.plot(t4['wavelength'],np.log10(t4['flux']),'-',linewidth=3,color='g',label='starburst')
plt.legend(loc=0)

plt.ylabel('flux density')
plt.xlabel('wavelength')
plt.title('Comparison of Mid-infrared Spectra for Different Sources')



plt.figure("irs2")


#line1,=plt.plot(t1['wavelength'],np.log10(t1['flux_density']),'-',linewidth=3,color='b',label='AGN')
#line2,=plt.plot(t2['wavelength'],0.2+np.log10(t2['flux_density']),'-',linewidth=3,color='r',label='BCD')
#line3,=plt.plot(t3['wavelength'],np.log10(t3['flux_density']),'-',linewidth=3,color='y',label='ULIRG')
#line4,=plt.plot(t4['wavelength'],np.log10(t4['flux_density']),'-',linewidth=3,color='g',label='starburst')
#plt.legend(loc=0)
#plt.ylabel('flux density')
#plt.xlabel('wavelength')
#plt.title('Comparison of Mid-infrared Spectra for Different Sources')

#plt.axis([22.,28.,-1.,1.])
#plt.xlim([22.,28.])
#plt.ylim([-2.,2.])

plt.show()

