import numpy as np
import math
def primeFactors(n):
    i = 2;
    factors = [];
    while i*i<=n:
        if n%i == 0:
            factors.append(i);
            n = int(n/i);
        else:
            i = i+1;
    factors.append(n) #offenbar bleibt das immer übrig
    print(max(factors))
    return factors;

if __name__ == "__main__":
    n = 600851475143;

#    isPrimz = lambda x: all(map(lambda i: x%i !=0, np.arange(2.0,math.floor(math.sqrt(x)+1),step=1)));
#    print(max([x for x in range(2,n) if isPrimz(x) and n%x == 0]))
    primeFactors(n)