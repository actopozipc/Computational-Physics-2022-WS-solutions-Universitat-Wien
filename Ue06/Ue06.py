import ue05 as Ue05
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import scipy
from scipy import sparse

n = 9
alpha = 0.01
h_x = 1/4
h_t = h_x**2/(4*alpha)
shape = (n,n)
t = 20
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
def euler_forward(u_i,f,h, sources=1):
    f = np.array(f).reshape(shape)
    sources = np.array(sources).reshape(shape)
    u_i = np.array(u_i).reshape(shape)
    return np.array(u_i + h*f +sources) #source f=1
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
Args: n
    n: dimension
returns:
    Heatfield that is nxn big, has zero everywhere and 1 in the middle
'''
def CreateHeatField(n):
    u = np.zeros((n*n))
    i = int(np.floor(n*n/2))
    u[i] = 1 #boundary condition
    return u

'''
Störterm aaaaaah
'''
def Howcangodberealiflaplaceexists(n, s, coors):
    source = scipy.sparse.csr_matrix(shape).toarray().flatten()
    source[coors[1]+n*(coors[0]-1)-1] = s
    return source

A = CreateSystemMatrixA( np.array(([0,1,0],[1,-4,1], [0,1,0])),n);
u = CreateHeatField(n)
fields = [u]
sources = Howcangodberealiflaplaceexists(n, n**2, [n,n])
for time in range(t):
    f = (A@u)
    fields.append(np.reshape(np.array(euler_forward(fields[-1], f, h_t, sources)),(n,n)))

def plotheatmap(u_k, k):
    plt.clf()
    plt.pcolormesh(np.array(u_k).reshape((n,n)), cmap=plt.cm.jet, vmin=0, vmax=100)
    plt.colorbar()
    return plt
def animate(k):
    plotheatmap(fields[k], k)


anim = animation.FuncAnimation(plt.figure(), animate, interval=n, frames=time, repeat=True)

# saves the animation in our desktop
anim.save('heat.mp4', writer = 'ffmpeg', fps = 2)