import numpy as np
from scipy import linalg
import math
import matplotlib.pyplot as plt

if __name__== "__main__":
    n = 100
    stepsize = 1/(n)
    f = 1 # a constant load f = 1
    A = -(2*np.eye(n,n) - np.eye(n, n, -1) - np.eye(n, n, 1))*f/stepsize; #does every fem matrix look like this?
    x = np.full((n),stepsize)*f;
    u = linalg.solve(A,x) #solve the system of equations
    print(u)
    xRange = np.linspace(0,1,n); 
    f = (np.power(xRange,2)-xRange)*0.5;
    plt.plot(xRange,f, "r");
    plt.plot(xRange,u, "g");
    plt.xlabel("x");
    plt.ylabel("f(x), u(x)");
    plt.show()
