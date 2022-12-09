import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
'''
Example:
(2 4 1
-1 1 3
3 2 5)
-> damit R2 = -1 -> 0 wird, muss man R2 + 2 * R2 + R1 = 2*-1 + 2 = -1 +  2*1/2 rechnen
-> A[1,0] - A[0,0] * A[1,0]/A[0,0] 
h = A[1,0]/A[0,0]
A[1,0] = A[1,0] - h*A[0,0] 
Dann Rest auf die anderen Zeilen anwenden
Mach dort wo die Nuller von L sind R hin, weil R eh nur 
I + Rechenschritte von L ist
'''
def LR(A):
    n,n = A.shape 
    L = np.identity(n) 
    U = np.zeros((n,n)) 
    for k in range(n):
        if abs(A[k,k]) != 0: #durch 0 dividieren bissi doof
            U[0,k] = A[0,k]
            for i in range(k+1,n):
                h = A[i,k]/A[k,k]  #h = Zeile / Zeile darüber
                for j in range(k,n):
                    A[i,j] = A[i,j] - h*A[k,j]
                    U[i,j] = A[i,j] #k wird zu 0, von k+1 bis n
                L[i,k] = h 
        else:
            print("doof") 
    return L,U 
'''
1.a
Lx = b
forward substitution method
params: 
    L: np.array
    b: np.array
returns:
    x: np.array
'''
def forward_solve(L,b):
    #x1 = b1
    #x_i = b_i - sum(L_iy * y_j)
    n = len(b)
    x = np.zeros(n)
    x[0] = b[0]/L[0,0] 
    comp = 0 
    for i in range(1,n):
        # for k in range(0,i):
        #     index = L[i,k]
        #     preSolution = x[k]
        #     comp = comp + index * preSolution
        comp = np.dot(L[i,:i], x[:i])
        x[i] = 1/L[i,i] * (b[i] - comp)
    return x 
def backward_solve(U, z):
    n = len(z)
    x = np.zeros(n)
    comp = 0 
    x[n-1] = z[n-1]/U[n-1,n-1]
    for i in range(n - 2, -1, -1):
        comp = z[i]
        # comp = np.dot(U[:i,i], z[:i])
        for j in range(i + 1, n):
            comp -= U[i, j] * x[j] 
        x[i] = 1/U[i, i] * ( comp)
    return x 

def solve(A,z):
    L2, U2 = LR(A) 
    z = forward_solve(L2, z)
    x = backward_solve(U2,z)
    return x 

if __name__ == "__main__":
    #Apply your method to the following test system
    A = np.array([[7.0,3,-1,2],[3,8,1,-4],[-1,1,4,-1],[2,-4,-1,6]])
    z = np.array([1,2,3,4])
    x = solve(A,z)
    A = np.array([[7.0,3,-1,2],[3,8,1,-4],[-1,1,4,-1],[2,-4,-1,6]])
    print("Result:" , np.matmul(A,x)) #1,6,4 sollte rauskommen
    #Perform benchmarks for some random matrices of different size. How does the algorithm
    #scale with the system size? Visualize the results using a log-log plot
    n = np.arange(2,80,10)
    timesavg = []
    for i in n:
        A = np.random.rand(i,i)
        b = np.random.rand(i)
        times = []
        for j in np.arange(10):
            t1 = datetime.now()
            solve(A,b);
            times.append((datetime.now()-t1).total_seconds());
        timesavg.append(np.mean(times));
    
            
    plt.plot(np.log(timesavg),np.log(n))
    plt.show()

    #Are there any linear systems which cannot be solved using your algorithm? Why? Try e.g.:
    '''
    0 0 0 1
    0 0 1 0
    0 1 0 0
    1 0 0 0

    '''
    wontWork = np.array([[0,0,0,1], [0,0,1,0], [0,1,0,0], [1,0,0,0]])
    solve(wontWork, z) #oh no, a division through zero, who wouldve thought! I wonder what this so called "pivoting" is