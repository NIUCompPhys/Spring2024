from math import sin,cos,pi
from numpy import arange,array
import matplotlib.pyplot as plt
import matplotlib.animation as animation

g = 9.81
l = 0.4
R = 0.05
W = 0.01
stepsperframe = 20
framerate = 200

# Function f(r)
def f(r):
  theta1 = r[0]
  theta2 = r[1]
  omega1 = r[2]
  omega2 = r[3]
  ftheta1 = omega1
  ftheta2 = omega2
  fomega1 = -(omega1*omega1*sin(2*theta1-2*theta2) + 2*omega2*omega2*sin(theta1-theta2) + (3*sin(theta1) + sin(theta1-2*theta2))*g/l)/(3-cos(2*theta1-2*theta2))
  fomega2 = (4*omega1*omega1*sin(theta1-theta2) + omega2*omega2*sin(2*theta1-2*theta2) - 2*(sin(theta2)-sin(2*theta1-theta2))*g/l)/(3-cos(2*theta1-2*theta2))
  return array([ftheta1,ftheta2,fomega1,fomega2],float)


# Main Program
# Set up starting values
h = 1.0/(framerate*stepsperframe)
theta1 = 0.8*pi
theta2 = 0.9*pi
omega1 = omega2 = 0.0
r = array([theta1,theta2,omega1,omega2],float)

def init():
    x1 = l*sin(theta1)
    y1 = -l*cos(theta1)
    x2 = l*(sin(theta1)+sin(theta2))
    y2 = -l*(cos(theta1)+cos(theta2))
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
    theta1 = r[0]
    theta2 = r[1]
    x1 = l*sin(theta1)
    y1 = -l*cos(theta1)
    x2 = l*(sin(theta1)+sin(theta2))
    y2 = -l*(cos(theta1)+cos(theta2))
    thisx = [0, x1, x2]
    thisy = [0, y1, y2]
    line.set_data(thisx, thisy)
  return line,


fig = plt.figure()
ax = plt.axes(xlim=(-2*l, 2*l), ylim=(-2*l,2*l))
line, = ax.plot([], [], lw=3)
ani = animation.FuncAnimation(fig, animate, interval=framerate, frames = 5000, init_func=init)
###plt.show()
ani.save('double_pendulum.mp4', fps=60, extra_args=['-vcodec', 'libx264'])
