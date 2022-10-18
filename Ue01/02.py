import numpy as np
def multiplesOf3And5(n):
    a = np.array(range(1,n));
    triples = a*3;
    five = a*5;
    print(np.sum(list(filter(lambda x:x<n, triples))) + np.sum(list(filter(lambda x:x<n, five))));
    return None;

if __name__ == "__main__":
    multiplesOf3And5(1000);