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
    n,n = A.shape;
    L = np.identity(n);
    U = np.zeros((n,n));
    for k in range(n):
        if abs(A[k,k]) != 0: #durch 0 dividieren bissi doof
            U[0,k] = A[0,k]
            for i in range(k+1,n):
                h = A[i,k]/A[k,k]; #h = Zeile / Zeile darüber
                for j in range(k,n):
                    A[i,j] = A[i,j] - h*A[k,j]; #k wird zu 0, von k+1 bis n
                    U[i,j] = A[i,j];
                L[i,k] = h;
        else:
            print("doof");
    return L,U;
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
    x[0] = b[0]/L[0,0];
    comp = 0;
    for i in range(1,n):
        
        # for k in range(0,i):
        #     index = L[i,k]
        #     preSolution = x[k]
        comp = np.dot(L[i,:i], x[:i])
        x[i] = 1/L[i,i] * (b[i] - comp)
    return x;
def backward_solve(U, z):
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = z[i]
        for j in range(i + 1, n):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]
    return x;
if __name__ == "__main__":
    A = np.array([[1.0,1,1],[4,3,-1], [3,5,3]])
    z = np.array([1,6,4])
    L2,U2 = LR(A)
    z = forward_solve(L2,z)
    print(z);
    x = backward_solve(U2,z)
    print(x)


    
