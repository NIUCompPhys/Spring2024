### Three-body problem
from numpy import arange,array,empty,concatenate,dot,empty,sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc,rcParams


G = 1.0 ## in these units
m1 = 200
m2 = 225
m3 = 275

### Returns mag squared of a vector
def magsq(v):
  return dot(v,v)

# Function f(vals)
### vals is the r vector (x,y) for each of three objects and then v vector (vx, vy) for each
### everything in z coordinate is zero for this problem
def f(vals):
  r1 = vals[0:2] ### needs two coordinates!
  r2 = vals[2:4]
  r3 = vals[4:6]
  v1 = vals[6:8]
  v2 = vals[8:10]
  v3 = vals[10:12]
  
  dr12 = magsq(r1-r2)**1.5
  dr23 = magsq(r2-r3)**1.5
  dr31 = magsq(r3-r1)**1.5

  fr1 = v1
  fr2 = v2
  fr3 = v3

  fv1 = G*((m2*(r2-r1))/(dr12) + (m3*(r3-r1))/(dr31))
  fv2 = G*((m3*(r3-r2))/(dr23) + (m1*(r1-r2))/(dr12))
  fv3 = G*((m1*(r1-r3))/(dr31) + (m2*(r2-r3))/(dr23))

  return concatenate([fr1,fr2,fr3,fv1,fv2,fv3])

# Main Program
# Set up starting values
stepsperframe = 150
framerate = 1
h = 1e-8
hmax = 1e-5
delta = 1e-5
vals = empty(12,float)
vals[0:2] = [1.0,3.0]
vals[2:4] = [-2.0,-1.0]
vals[4:6] = [1.0,-1.0]
vals[6:12] = [0.3,0.3,-0.3,-0.2,0.1,-0.2]

frame = 0
def animate(i):
  global vals,frame,h
  frame = frame+1
  if (frame % 100 == 0): print(frame)
  for i in range(stepsperframe):
    passedError = False
    while (not passedError):
      # Do one large step
      k1 = 2*h*f(vals)
      k2 = 2*h*f(vals+0.5*k1)
      k3 = 2*h*f(vals+0.5*k2)
      k4 = 2*h*f(vals+k3)
      vals1 = vals + (k1+2*k2+2*k3+k4)/6

      # Do two small steps
      k1 = h*f(vals)
      k2 = h*f(vals+0.5*k1)
      k3 = h*f(vals+0.5*k2)
      k4 = h*f(vals+k3)
      vals2 = vals + (k1+2*k2+2*k3+k4)/6

      k1 = h*f(vals2)
      k2 = h*f(vals2+0.5*k1)
      k3 = h*f(vals2+0.5*k2)
      k4 = h*f(vals2+k3)
      vals2 += (k1+2*k2+2*k3+k4)/6

      # Calculate rho and error and update
      e1 = sqrt(magsq(vals1[0:2]-vals2[0:2]))/30
      e2 = sqrt(magsq(vals1[2:4]-vals2[2:4]))/30
      e3 = sqrt(magsq(vals1[4:6]-vals2[4:6]))/30
      epsilon = max(e1,e2,e3,1e-18)
      rho = delta*h/epsilon

      # Calculate new t, h and r
      if rho >= 1.0: #can increase h, keep this point
        passedError = True
        vals = vals1 ### set new values
        h = min(h*rho**0.25,2.0*h,hmax) ### don't let h get tooo big!
      else: ### nope, make h smaller, redo
        h *= rho**0.25

  planet1.set_data([vals[0]],[vals[1]])
  planet2.set_data([vals[2]],[vals[3]])
  planet3.set_data([vals[4]],[vals[5]])
  return planet1,planet2,planet3,

fig = plt.figure()
maxaxis = 15
ax = plt.axes(xlim=(-maxaxis,maxaxis), ylim=(-maxaxis,maxaxis))
ax.set_aspect("equal")
planet1, = ax.plot(vals[0], vals[1], marker="o")
planet2, = ax.plot(vals[2], vals[3], marker="o")
planet3, = ax.plot(vals[4], vals[5], marker="o")
ani = animation.FuncAnimation(fig, animate, interval=framerate, frames = 5000, blit=True)
ani.save('three-body.mp4', fps=60, extra_args=['-vcodec', 'libx264'])


