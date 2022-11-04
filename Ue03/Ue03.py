# A -> B with k1
# B -> C with k2
# therefore: C' = k2*B
# A' = k1*A
# B' = k1*A-k2*B Ansatz
# Matrix: k1 0 0
#         k1 -k2 0
#         0 k2 0
# Vektor: (A,B,C)
# Matrix * Vektor = X'
import numpy as np
import matplotlib.pyplot as plt
h = 0.0001;
k1 = 1.0;
#I think 10 seconds is not a good idea because it depends on the execution time of the PC and the 
# implementation of euler/heun then 
# the results are much more comparable per iterations
#Alternatively, I couldve done something like this:
#t1 = datetime.now();
#while (datetime.now()-t1).seconds<10:
iterations = 100000; 
def euler(func, k2, startingValue, oldValues = range(iterations)):
    values = [];
    values.append(startingValue);
    for n in np.arange(1,iterations):
        f = values[n-1] + h*func(values[n-1],oldValues[n-1], k2);
        values.append(f);
    return values;

def Heun(func,k2, startingValue, oldValues=range(iterations)):
    values = [];
    values.append(startingValue);
    for n in np.arange(1,iterations):
        ystrich = values[n-1] + h*func(values[n-1],oldValues[n-1], k2);
        f = values[n-1] + h/2*(func(values[n-1],oldValues[n-1], k2) + func(ystrich,oldValues[n], k2));
        values.append(f);
    return values;
def AnalyticalSolutions(k1,k2):
    values = [];
    A0 = 1;
    if k1==k2:
        C = lambda t: A0 * (1-np.exp(-k1*t)*(1+k1*t));
        for i in range(10):
            values.append(C(i));
        return values;
    else:
        C = lambda t: A0 * (1-(k2*np.exp(-k1*t)-k1*np.exp(-k2*t))/(k2-k1));
        for i in range(10):
            values.append(C(i));
        return values;


if __name__ == "__main__":

    k2s = [1,10,100,1000];
    Aprime = lambda A, y, z: -k1*A
    Bprime = lambda B,A,k2: k1*A-k2*B;
    Cprime = lambda C,B, k2: k2*B;
    #List of values for functions A, B and C
    aValuesEuler = [];
    bValuesEuler = [];
    cValuesEuler = [];
    aValuesHeun = [];
    bValuesHeun = [];
    cValuesHeun = [];
    ValuesAnalytical = [];

    #Counter to use values of A, B since B uses values of A and C values of B
    count = 0;
    for k2 in k2s:
        aValuesEuler.append(euler(Aprime,10, 1));
        aValuesHeun.append(Heun(Aprime,10, 1));
        ValuesAnalytical.append(AnalyticalSolutions(k1, k2));
        bValuesEuler.append(euler(Bprime, k2, 0, oldValues=aValuesEuler[count]));
        bValuesHeun.append(Heun(Bprime, k2, 0, oldValues=aValuesEuler[count]));
        cValuesEuler.append(euler(Cprime, k2, 0, oldValues=bValuesEuler[count]));
        cValuesHeun.append(Heun(Cprime, k2, 0, oldValues=bValuesEuler[count]));
        count = count+1;
    range = np.arange(1,iterations+1);
    fig, axs = plt.subplots(3, 3);

    for x in aValuesEuler:
        axs[0,0].plot(range,x);
    for x in bValuesEuler:
        axs[1,0].plot(range,x);
    for x in cValuesEuler:
        axs[2,0].plot(range,x);
    for x in aValuesHeun:
        axs[0,1].plot(range,x);
    for x in bValuesHeun:
        axs[1,1].plot(range,x);
    for x in cValuesHeun:
        axs[2,1].plot(range,x);
    for x in ValuesAnalytical:
        axs[2,2].plot(np.arange(10),x);
    plt.show();