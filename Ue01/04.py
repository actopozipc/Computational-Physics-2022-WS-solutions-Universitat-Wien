import numpy as np
import math
def isPrim(n):
    arr = np.arange(2,math.sqrt(n)+1)
    for i in arr:
        if n % i == 0:
            return False;
    return True;
def getPrimes(n):
    primes = np.array([2]);
    numbers = np.arange(3, math.sqrt(n)+1)
    for i in numbers:
        if isPrim(i):
            primes = np.append(i, primes);
    return primes;
def bruteforcePrimes(primes,n):
    arr = np.arange(2, np.max(primes));
    faktoren = np.array([])
    for i in primes:
        if n % i == 0:
            faktoren = np.append(i, faktoren);
    return faktoren;
if __name__ == "__main__":
   n = 600851475143;
   primes = getPrimes(n);
   faktoren = bruteforcePrimes(primes, n)
   print(faktoren)