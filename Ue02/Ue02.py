import numpy as np
#read time t and ~mfreelayer from data file oscillator.dat
t, mfree_x, mfree_y, mfree_z, mfixed_x, mfixed_y, mifxed_z = np.loadtxt("oscillator.dat", unpack=True)

avgs = list(map(lambda x: np.average(x), [t,mfree_x, mfree_y, mfree_z]))
interp = np.interp([1,2,3,4,5], t, mfree_x)
