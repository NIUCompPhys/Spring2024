from math import sin,cos,pi
from numpy import arange,array
import matplotlib.pyplot as plt
import matplotlib.animation as animation

g = 9.81
l = 0.2
framerate = 10
stepsperframe = 20

def f(r):
  theta = r[0]
  omega = r[1]
  ftheta = omega
  fomega = (-g/l)*sin(theta)
  return array([ftheta,fomega],float)

# Initial values
theta = pi*170/180
r = array([theta,0.0],float)
# Main loop
h = 1.0/(framerate*stepsperframe)

def init():
    x = l*sin(theta)
    y = -l*cos(theta)
    line.set_data([], [])
    return line

def animate(i):
  global r
  for i in range(stepsperframe):
    k1 = h*f(r)
    k2 = h*f(r+0.5*k1)
    k3 = h*f(r+0.5*k2)
    k4 = h*f(r+k3)
    r += (k1+2*k2+2*k3+k4)/6
    # Graphics
    theta = r[0]
    x = [0,l*sin(theta),0]
    y = [0,-l*cos(theta),0]
    line.set_data(x,y)
    return line,

fig = plt.figure()
ax = plt.axes(xlim=(-2*l, 2*l), ylim=(-2*l,2*l))
line, = ax.plot([], [], lw=3)
ani = animation.FuncAnimation(fig, animate, interval=framerate, frames = 4000, init_func=init)
###ani.save('non_linear_pendulum.mp4', fps=30)
########, extra_args=['-vcodec', 'libx264'])
#writergif = animation.PillowWriter(fps=30)
#ani.save('non_linear_pendulum.gif',writer=writergif)
writervideo = animation.FFMpegWriter(fps=60) 
ani.save('non_linear_pendulum.mp4', writer=writervideo)


###
