import numpy as np
if __name__ == "__main__":
    n=1000;
    print(np.sum(list(filter(lambda x:x<n, np.arange(n)*3))) + np.sum(list(filter(lambda x:x<n, np.arange(n)*5))));