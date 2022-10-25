import numpy as np
if __name__ == "__main__":
    fib = [1,2];
    list(map(lambda x: fib.append(np.sum(fib[-2:])) if (np.sum(fib[-2:]) < 4e6) else None, range(2,10000)));
    print(np.sum(list(filter(lambda x: x%2 == 0, fib))));
