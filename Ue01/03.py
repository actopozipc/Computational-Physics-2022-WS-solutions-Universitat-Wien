import numpy as np
def fibonaccinumbers():
    fib = [1,2];
    while True:
        sum = fib[-1] + fib[-2];
        if sum < 4e6:
            fib.append(sum);
        else:
            break;
    print(np.sum(list(filter(lambda x: x%2 == 0, fib))));
    return None;

if __name__ == "__main__":
    fibonaccinumbers();