from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.mlab as mlab
import math as m
import pdb


#t1 = Table.read('NGC5548', format='ascii.ipac')
#t2 = Table.read('IIZW40', format='ascii.ipac')
#t3 = Table.read('MRK273', format='ascii.ipac')
#t4 = Table.read('M82', format='ascii.ipac')

t1=fits.open('cassis_NGC5548.fits')
t2=fits.open('cassis_NGC1569.fits')
t3=fits.open('cassis_mrk273.fits')
t4=fits.open('cassis_NGC520.fits')
#t4=fits.open('cassis_yaaar_opt_9072128.fits')


print(t1.info())

t11=(t1[0].data[:,0])
t12=(t1[0].data[:,1])
t21=(t2[0].data[:,0])
t22=(t2[0].data[:,1])
t31=(t3[0].data[:,0])
t32=(t3[0].data[:,1])
t41=(t4[0].data[:,0])
t42=(t4[0].data[:,1])

st11=np.argsort(t11)
st21=np.argsort(t21)
st31=np.argsort(t31)
st41=np.argsort(t41)

t11=t11[st11]
t12=t12[st11]
t21=t21[st21]
t22=t22[st21]
t31=t31[st31]
t32=t32[st31]
t41=t41[st41]
t42=t42[st41]

t22=t12[0]/t22[0]*t22
t32=t12[0]/t32[0]*t32
t42=t12[0]/t42[0]*t42

#print(t11)
print(t21)
print(np.size(t12),np.size(t11))
#pdb.set_trace()

fig=plt.figure("irs")
#ax = fig.gca()
#ax.set_autoscale_on(False)

kt1=np.where((t11 > 14.) & (t11 < 30.))
kt2=np.where((t21 > 14.) & (t21 < 30.))
kt3=np.where((t31 > 14.) & (t31 < 30.))
kt4=np.where((t41 > 14.) & (t41 < 30.))
#kt422=np.where((t41 > 15.) & (t41 < 30.))

#line1,=plt.plot(t1['wavelength'],np.log10(t1['flux_density']),'-',linewidth=3,color='b',label='AGN')
#line2,=plt.plot(t2['wavelength'],0.2+np.log10(t2['flux_density']),'-',linewidth=3,color='r',label='BCD')
#line3,=plt.plot(t3['wavelength'],np.log10(t3['flux_density']),'-',linewidth=3,color='y',label='ULIRG')



line1,=plt.plot(t11[kt1]/(1+0.017175),(np.log10(t12))[kt1]+1.5,'-',linewidth=3,color='r',label='AGN')
line2,=plt.plot(t21[kt2]/(1-0.000347),(np.log10(t22))[kt2]+1.1,'-',linewidth=3,color='indigo',label='BCD')
line3,=plt.plot(t31[kt3]/(1+0.037780),(np.log10(t32))[kt3]-0.4,'-',linewidth=3,color='lightgreen',label='ULIRG')
line4,=plt.plot(t41[kt4]/(1+0.007609),2*((np.log10(t42))[kt4]-0.5)-1.3,'-',linewidth=3,color='skyblue',label='starburst')

plt.plot([25.9,25.9],[-3,3],'--k')
plt.text(26.1,1.5,'[OIV]')
plt.plot([15.5,15.5],[-3,3],'--k',)
#plt.plot([12.8,12.8],[-3,3],'--k')
plt.text(15.7,1.5,'[NeIII]')
plt.plot([18.7,18.7],[-3,3],'--k')
plt.text(18.9,1.5,'[SIV]')
plt.plot([10.8,10.8],[-3,3],'--k')
plt.text(18.9,1.5,'[SIII]')
plt.plot([12.8,12.8],[-3,3],'--k')
plt.text(18.9,1.5,'[NeII]')


plt.legend(loc=0)

#plt.ylabel('flux density')
#plt.xlabel('wavelength')
plt.title('Comparison of Mid-infrared Spectra for Different Sources')

print(np.max(t42),np.min(t42))
plt.axis([15.,30.,-2.6,2.])
plt.savefig('/Users/weizheliu/astro610/irs.eps')

plt.show()
pdd.set_trace()

t11=np.array(t11)
it1=np.where((t11 < 28.) & (t11 > 24.))
it2=np.where((t21 < 28.) & (t21 > 24.))
it3=np.where((t31 < 28.) & (t31 > 24.))
it4=np.where((t41 < 28.) & (t41 > 24.))

fig=plt.figure("irs2")

c2=((t12[it1])[0])-((t22[it2])[0])
c3=((t12[it1])[0])-((t32[it3])[0])
c4=((t12[it1])[0])-((t42[it4])[0])


line1,=plt.plot((t11[it1])/(1+0.017175),(t12[it1]),'-',linewidth=3,color='r',label='AGN',)
line2,=plt.plot(t21[it2]/(1-0.000347),(t22[it2])+c2-0.1,'-',linewidth=3,color='indigo',label='BCD')
line3,=plt.plot((t31[it3])/(1+0.037780),(t32[it3])+c3-0.38*(t31[it3]-24.5)+0.2,'-',linewidth=3,color='lightgreen',label='ULIRG')
line4,=plt.plot(t41[it4]/(1+0.007609),(t42[it4])+c4-0.19*(t41[it4]-24.5)+0.1,'-',linewidth=3,color='skyblue',label='starburst')

plt.legend(loc=0)
plt.title=('Example of [OIV] emission in different sources')
plt.xlabel(r'Wavelength(($\mu m$))')
plt.ylabel('Relative Flux Density')
plt.axis([24.5,26.7,0.4,1.35])

jt1=np.where((t11 > 12.) & (t11 < 16.))
jt2=np.where((t21 > 12.) & (t21 < 16.))
jt3=np.where((t31 > 12.) & (t31 < 16.))
jt4=np.where((t41 > 12.) & (t41 < 16.))

fig=plt.figure("irs3")

c2=((t12[jt1])[0])/((t22[jt2])[0])
c3=((t12[jt1])[0])/((t32[jt3])[0])
c4=((t12[jt1])[0])/((t42[jt4])[0])


line1,=plt.plot((t11[jt1])/(1+0.017175),(t12[jt1]),'-',linewidth=3,color='b',label='AGN',)
line2,=plt.plot( t21[jt2]/(1-0.000347),( t22[jt2]),'-',linewidth=3,color='r',label='BCD')
line3,=plt.plot((t31[jt3])/(1+0.037780),(t32[jt3]),'-',linewidth=3,color='y',label='ULIRG')
line4,=plt.plot( t41[jt4]/(1+0.007609),( t42[jt4]),'-',linewidth=3,color='g',label='starburst')

plt.legend(loc=0)
plt.title=('Example of [OIV] emission in different sources')
plt.xlabel(r'Wavelength(($\mu m$))')
plt.ylabel('Relative Flux Density')
#plt.axis([24.5,26.7,0.4,1.35])
plt.xlim(15.,16.5)


#plt.xlim([22.,28.])
#plt.ylim([-2.,2.])

plt.show()

