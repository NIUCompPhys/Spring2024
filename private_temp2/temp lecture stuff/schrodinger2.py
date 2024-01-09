from numpy import empty, arange, linspace, exp, real, full
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from banded import banded

#constants
L = 1.0e-8
N = 1000
a = L/N
m = 9.109e-31
hbar = 1.055e-34
x0 = L/2
sigma = 1.0e-10
kappa = 5.0e10

tmax = 1.0e-12
yscale = 1e-9
h = 5e-19
###h = 1e-16

C = 1j*hbar/(4*m*a*a)
a1 = 1 + 2*h*C
a2 = -h*C
b1 = 1 - 2*h*C
b2 = h*C

# Create the initial arrays of x and psi values
x = linspace(0,L,N+1)
psi = exp(-(x-x0)**2/(2*sigma**2))*exp(1j*kappa*x)
psi[0] = psi[N] = 0
# Create the tridiagonal array A
A = empty([3,N-1],complex)
A[0,:] = a2
A[1,:] = a1
A[2,:] = a2

def init():
    line.set_data([], [])
    return line,


def animate(i):
    ## main loop for the Crank-Nicolson method
    v = b2*psi[0:N-1] + b1*psi[1:N] + b2*psi[2:N+1]
    psi[1:N] = banded(A,v,1,1)
    ys = yscale*real(psi)
    line.set_data(x,ys)
    return line,


fig = plt.figure()
ax = plt.axes(xlim=(0, L), ylim=(-yscale,yscale))
line, = ax.plot([], [], lw=3)

ani = animation.FuncAnimation(fig, animate, interval=15, frames = 5000, init_func=init)
###ani = animation.FuncAnimation(fig, animate, interval=20, init_func=init,blit=True)
ani.save('schrodinger.mp4', fps=60, extra_args=['-vcodec', 'libx264'])

###plt.show()

