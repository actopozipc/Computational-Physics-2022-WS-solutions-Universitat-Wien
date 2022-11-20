
"""
lARA FARKAS
COMPUTATIONAL PHYSICS, PUE%
PDE
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as LA

n = 50
'''
    Creates a Matrix with the stencil along the tridiagonal and n-1 zeros after the -4 for the nth line of the matrix (please just look at the sheet)
    Args:
        stencil
    Returns:
        Matrix A
    '''
def CreateSystemMatrixA(l):
    A = np.zeros((n*n,n*n))
    for i in range(1,n+1):
        for j in range(1,n+1):
            g = np.zeros((n,n))
            #add zeros around everything
            gp = np.pad(g,1)
            #add stance down the tridiagonal
            gp[i-1:i+2, j-1:j+2] = l
            #remove outter bound to make flatten possible
            gp = gp[1:-1,1:-1]
            #put flatten ndarray into A-line
            #every line of A goes like 1 -4 1 ....
            A[:,(j-1)+n*(i-1)] = gp.flatten()
    return A
    '''
    Creates a vector that has n entries of -1 and n*n-n entries of 0
    Args:
        None
    Returns:
        Vector
    '''
def CreateSolutionVectorB():
    B = np.zeros(n**2)
    B[:n] = -1
    return B
    '''
    Solves Au = b
    Args:
        None
    Returns:
        u reshaped to nxn matrix
    '''
def Setup2DLaplacian(): #Au=b
    A = CreateSystemMatrixA( np.array(([0,1,0],[1,-4,1], [0,1,0])))
    b = CreateSolutionVectorB()
    u = LA.solve(A,b)[::-1] #revert u for some reason
    return np.reshape(u, (n, n))


if __name__ == "__main__":
    u = Setup2DLaplacian()
    x = np.linspace(0, 1, n)
    y = np.linspace(1, 0, n)
    X, Y = np.meshgrid(x, y)
    plt.contourf(X, Y, u, 10)
    plt.colorbar()
    plt.show()
