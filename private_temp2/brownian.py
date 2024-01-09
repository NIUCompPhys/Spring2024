from math import log
from vpython import sphere,box,color,rate,vector
from random import randrange

L = 1001
N = 1000000
framerate = 1000

box(pos=vector(-L/2,0,0),length=1,height=L,width=1,color=color.green)
box(pos=vector(L/2,0,0),length=1,height=L,width=1,color=color.green)
box(pos=vector(0,-L/2,0),length=L,height=1,width=1,color=color.green)
box(pos=vector(0,L/2,0),length=L,height=1,width=1,color=color.green)
s = sphere(pos=vector(0,0,0), radius=5, color = color.white)

# Main loop
i = j = 0
for k in range(N):
  direction = randrange(4)
  if (direction == 0):
    if i < L/2: i += 1
  elif (direction == 1):
    if i > -L/2: i -= 1
  elif (direction == 2):
    if j < L/2: j += 1
  else:
    if j > -L/2: j -= 1
  rate(framerate)
  s.pos = vector(i,j,0)
