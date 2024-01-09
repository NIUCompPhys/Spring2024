from math import log
from random import randrange
import matplotlib.pyplot as plt
from matplotlib import animation, rc
import numpy as np

L = 201
N = 10000
####N = 1000000
framerate = 1

x = y = 0

def animate(i):
  global x,y
  # Main loop
  ###print(pos[i,0],pos[i,1])
  # Main loop
  direction = randrange(4)
  if (direction == 0):
    if x < L/2: x += 1
  elif (direction == 1):
    if x > -L/2: x -= 1
  elif (direction == 2):
    if y < L/2: y += 1
  else:
    if y > -L/2: y -= 1
  point.set_data(x,y)
  return point,

fig = plt.figure()
ax = plt.axes(xlim=(-L/2, L/2), ylim=(-L/2,L/2))
ax.set_aspect("equal")
# create a point in the axes
point, = ax.plot(x,y, marker="o")


ani = animation.FuncAnimation(fig, animate, interval=framerate, frames = N, blit=True)
###plt.show()
ani.save('brownian_motion_2d.mp4', fps=60, extra_args=['-vcodec', 'libx264'])
