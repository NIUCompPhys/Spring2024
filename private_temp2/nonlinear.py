### Exercise 8.4 Non-linear pendulum

from math import sin,cos,pi
from numpy import array
import matplotlib.pyplot as plt
import matplotlib.animation as animation

g = 9.81
l = 0.1
W = 0.002
R = 0.01
framerate = 200
stepsperframe = 20

def f(r):
  theta = r[0]
  omega = r[1]
  ftheta = omega
  fomega = (-g/l)*sin(theta)
  return array([ftheta,fomega],float)

# Initial values
theta = pi*179/180
r = array([theta,0.0],float)
# Main loop
h = 1.0/(framerate*stepsperframe)

def init():
    x = l*sin(theta1)
    y = -l*cos(theta1)
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
    x = l*sin(theta)
    y = -l*cos(theta)
    line.set_data(x,y)
  return line,
