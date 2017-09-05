import numpy as np
import matplotlib.pyplot as plt

plt.figure('figure')

s=np.arange(1000)/100.-5.
tau=1.
pi=np.pi
#y=(tau**2.+(2*pi*(tau**2)*s)**2)/((1+(2*pi*tau*s)**2)**2)
y=(tau**2.)/((1+(2*pi*tau*s)**2))
#y=np.log10(y)
plt.plot(s,y,'k',label='tau='+str(tau))

tau=0.5
pi=np.pi
#y=(tau**2.+(2*pi*(tau**2)*s)**2)/((1+(2*pi*tau*s)**2)**2)
y=(tau**2.)/((1+(2*pi*tau*s)**2))
#y=np.log10(y)
plt.plot(s,y,'b',label='tau='+str(tau))
#
tau=0.2
pi=np.pi
#y=(tau**2.+(2*pi*(tau**2)*s)**2)/((1+(2*pi*tau*s)**2)**2)
y=(tau**2.)/((1+(2*pi*tau*s)**2))
#y=np.log10(y)
plt.plot(s,y,'r',label='tau='+str(tau))

plt.xlabel('Frequency')
plt.ylabel('Intensity')
#
#tau=20.
#pi=np.pi
##y=(tau**2.+(2*pi*(tau**2)*s)**2)/((1+(2*pi*tau*s)**2)**2)
#y=(tau**2.)/((1+(2*pi*tau*s)**2))
#y=np.log10(y)
#plt.plot(s,y,'r',label='tau='+str(tau))

#The peak value scales with tau^2.
plt.legend()
plt.show()

