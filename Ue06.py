import ue05 as Ue05
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import scipy
from scipy import sparse
from scipy.sparse import linalg
from scipy.sparse import csc_array

n = 20
alpha = 10
h_x = 1
h_t = 0.01
shape = (n,n)
t = 1000
# Sadly, the eulers I implemented at ue03 are not very usable here
# Since I wrote them for lambda functions in order to iterate
# over them and call A, B and C as argument
'''
Args: 
u_i: Step before
f: Laplacian -> stencil * heat field * alpha
h: step size
sources: störterm aaaaaaah
'''
def euler_forward(u_i,h, A, sources=1):
    return u_i + 1/(h_x**2)*h*(alpha*A@u_i + sources)
def euler_backward(u_i,f,h):
    pass
'''
Args: 
    l: pattern to reproduce 
    n: dimension of the stencil
returns:
    nxn matrix that is stencil
'''
def CreateSystemMatrixA(l,n):
    A = csc_array((n*n, n*n))
    for i in range(1,n+1):
        for j in range(1,n+1):
            g = csc_array((n+2, n+2))
            #add stance down the tridiagonal
            g[i-1:i+2, j-1:j+2] = l
            #remove outter bound to make flatten possible
            g = g[1:-1,1:-1]
            #put flatten ndarray into A-line
            #every line of A goes like 1 -4 1 ....
            A[:,(j-1)+n*(i-1)] = csc_array.reshape(g, [n*n,1])
    return A

'''
Args: n
    n: dimension
returns:
    Heatfield that is nxn big, has zero everywhere and 1 in the middle
'''
def CreateHeatField(n):
    return csc_array((n*n,1))

'''
Störterm aaaaaah
'''
def GenerateStörterm(n):
    source = csc_array((n*n,1))
    source[n//2+n//2] = 1
    return source

A = CreateSystemMatrixA(np.array(([0,1,0],[1,-4,1], [0,1,0])),n);

u = CreateHeatField(n)
resfields = np.zeros((t+1,n,n))
sources = GenerateStörterm(n)
for time in range(t):
    u = euler_forward(u, h_t, A, sources)
    res = csc_array.reshape(u, [n,n]).toarray()
    resfields[time,:,:] = res

# Ive spent several hours debugging the heat equation
# when the error was all along in the animation
# :(((
# def plotheatmap(u_k,k):
#      # Clear the current plot figure
#     plt.clf()

#     # This is to plot u_k (u at time-step k)
#     plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=0, vmax=100)
#     plt.colorbar()

#     return plt
# def animate(k):
#      plotheatmap(resfields[k], k)

plt.imshow(resfields[t-1,:,:],cmap="jet")
plt.colorbar()
plt.show()

