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
t4 = Table.read('M82', format='ascii.ipac')
#t4=fits.open('cassis_NGC1569.fits')
#t4.info()

z1=0.017175
z2=0.002632
z3=0.03778
z4=0.000677
#pdb.set_trace

fig=plt.figure("irs")
#ax = fig.gca()
#ax.set_autoscale_on(False)
mf=np.min(np.log10(t1['flux_density']))

line1,=plt.plot(t1['wavelength']/(1+z1),np.log10(t1['flux_density'])-mf,'-',linewidth=3,color='r',label='AGN')
line2,=plt.plot(t2['wavelength']/(1+z2),0.2+np.log10(t2['flux_density'])-mf,'-',linewidth=3,color='indigo',label='BCD')
line3,=plt.plot(t3['wavelength']/(1+z3),np.log10(t3['flux_density'])-mf,'-',linewidth=3,color='lightgreen',label='ULIRG')
line4,=plt.plot(t4['wavelength']/(1+z4),np.log10(t4['flux_density'])-mf,'-',linewidth=3,color='skyblue',label='starburst')

plt.ylabel('Flux Density (relative)')
plt.xlabel(r'$\lambda /\mu m$')
plt.title('Comparison of Mid-infrared Spectra for Different Sources')

plt.plot([25.9,25.9],[-3,30],'--k')
plt.text(26.1,1.5-mf,'[OIV]')
plt.plot([15.5,15.5],[-3,30],'--k',)
plt.text(15.7,1.5-mf,'[NeIII]')
plt.plot([18.7,18.7],[-3,30],'--k')
plt.text(18.9,1.5-mf,'[SIII]')

plt.plot([12.8,12.8],[-3,30],'--k',)
plt.text(13.0,1.5-mf,'[NeII]')
plt.plot([10.5,10.5],[-3,30],'--k')
plt.text(10.7,1.5-mf,'[SIV]')
plt.plot([33.5,33.5],[-3,30],'--k')
plt.text(33.7,1.5-mf,'[SIII]')

plt.legend(loc=0)



plt.ylim(-0.5,3.5)
plt.xlim(0,40)
plt.show()

plt.figure("irs2")


line1,=plt.plot(t1[r'$ambda/mum m'],np.log10(t1['flux_density']),'-',linewidth=3,color='b',label='AGN')
line2,=plt.plot(t2[r'$ambda/mum m'],0.2+np.log10(t2['flux_density']),'-',linewidth=3,color='r',label='BCD')
line3,=plt.plot(t3[r'$ambda/mum m'],np.log10(t3['flux_density']),'-',linewidth=3,color='y',label='ULIRG')
line4,=plt.plot(t4[r'$ambda/mum m'],np.log10(t4['flux_density']),'-',linewidth=3,color='g',label='starburst')
plt.legend(loc=0)
plt.ylabel('flux density')
plt.xlabel(r'$ambda/mum m')
plt.title('Comparison of Mid-infrared Spectra for Different Sources')

plt.axis([22.,28.,-1.,1.])
#plt.xlim([22.,28.])
#plt.ylim([-2.,2.])

#plt.show()

