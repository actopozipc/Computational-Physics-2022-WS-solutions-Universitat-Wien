import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.gridspec as gridspec
from scipy import integrate
#read time t and ~mfreelayer from data file oscillator.dat
t, mfree_x, mfree_y, mfree_z, mfixed_x, mfixed_y, mifxed_z = np.loadtxt("oscillator.dat", unpack=True)
#averages
avgs = list(map(lambda x: integrate.simpson(x,t)/(t[-1]-t[0]), [mfree_x, mfree_y, mfree_z]))
avgs.append(np.sum(t)/len(t))
betrag = list(map(lambda x,y,z: math.sqrt(x**2+y**2+z**2), mfree_x, mfree_y, mfree_z))
avgs.append(np.average(betrag))
print(avgs)
#range for interpolation
ran = np.arange(0,t[-1], t[1])
#interpolation
interp = np.interp(ran, t, mfree_x)
#differentation
dfdt = np.diff(interp)
#fft for y and x
f = np.fft.fft(interp)
xf = np.fft.fftfreq(len(interp), t[1])
#plotting stuff
gs = gridspec.GridSpec(3, 1) #rows
plt.figure()
ax = plt.subplot(gs[0, 0]) # row 0, col 0
plt.plot(ran,interp)
ax = plt.subplot(gs[1, 0])
plt.plot(ran[1:], dfdt)
ax = plt.subplot(gs[2, 0])
plt.xlim(0,0.5e10)
plt.plot(np.abs(xf),np.abs(f))
plt.show()