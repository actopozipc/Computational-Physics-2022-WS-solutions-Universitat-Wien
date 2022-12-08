import numpy as np
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
                    U[i,j] = A[i,j] - h*A[k,j] #k wird zu 0, von k+1 bis n
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
    x = np.empty(n)
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
    x = np.empty(n)
    comp = 0 
    x[-1] = z[-1]/U[-1,-1]
    for i in range(n - 1, 0, -1):
        # x[i] = z[i]
        # comp = np.dot(U[:i,i], z[:i])
        for j in range(i + 1, n):
            comp -= U[i, j] * x[j] 
        x[i] = 1/U[i, i] * (z[i] + comp)
    return x 

def solve(A,z):
    L2, U2 = LR(A) 
    z = forward_solve(L2, z)
    x = backward_solve(U2,z)
    return x 

if __name__ == "__main__":
    #Apply your method to the following test system
    A = np.array([[1.0,1,1],[4,3,-1],[3,5,3]])
    z = np.array([1,6,4])
    L,U = LR(A)
    y = forward_solve(L, z)
    print(y)
    x = backward_solve(U,y)
    # print(x)
    print(np.matmul(A,x)) #1,6,4 sollte rauskommen
    #Perform benchmarks for some random matrices of different size
    # n = [2,4,8,16]
    # for i in n:
    #     A = np.random.rand(i,i)
    #     b = random.rand(i)

