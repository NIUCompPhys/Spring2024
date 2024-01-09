from numpy import empty, linspace, exp, zeros
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#constants
L = 1.0
d = 0.1
v = 100.0
C = 1.0
N = 100
a = L/N
sigma = 0.3

h = 4e-6

# create the initial array of y and z values
x = linspace(0.0,L,N+1)
global psi,dpsi
psi = zeros(N+1,float)
dpsi = C*x*(L-x)*exp(-(x-d)**2 / (2*sigma*sigma))/(L*L)

def f(y):
  res = empty(N+1,float)
  res[1:N] = (y[0:N-1] + y[2:N+1] - 2*y[1:N]) * (v*v)/(a*a)
  res[0] = res[N] = 0.0
  return res

def init():
  line.set_data([], [])
  return line,

def animate(i):
  global psi,dpsi
  line.set_data(x,psi)
  psi,dpsi = psi+h*dpsi,dpsi+h*f(psi)
  return line,


fig = plt.figure()
ax = plt.axes(xlim=(0, L), ylim=(-0.0005,0.0005))
line, = ax.plot([], [], lw=3)

ani = animation.FuncAnimation(fig, animate, interval=0, frames = 7500, init_func=init,blit=True)
ani.save('ftcs_wave.mp4', fps=60, extra_args=['-vcodec', 'libx264'])


