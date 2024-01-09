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

def calcEnergies(vals):
  u_val = -G*m1*m2/sqrt(magsq(vals[0:3] - vals[3:6])) + -G*m1*m3/sqrt(magsq(vals[0:3] - vals[6:9])) + -G*m3*m2/sqrt(magsq(vals[3:6] - vals[6:9]))
  k_val = 0.5*m1*magsq(vals[9:12]) + 0.5*m2*magsq(vals[12:15]) + 0.5*m3*magsq(vals[15:18])
  e_val = u_val + k_val
  return u_val, k_val, e_val

# Function f(vals)
### vals is the r vector (x,y) for each of three objects and then v vector (vx, vy) for each
### everything in z coordinate is zero for this problem
def f(vals):
  r1 = vals[0:3] ### needs two coordinates!
  r2 = vals[3:6]
  r3 = vals[6:9]
  v1 = vals[9:12]
  v2 = vals[12:15]
  v3 = vals[15:18]
  
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
doAdaptive = True
stepsperframe = 300
framerate = 1
h = hstart = 1e-8
hmax = 1e-5
delta = 1e-5
vals = empty(18,float)
vals[0:3] = [1.0,3.0,1.0]
vals[3:6] = [-2.0,-1.0,-1.0]
vals[6:9] = [1.0,-1.0,2.0]
vals[9:12] = [0.6,1.3,-0.7]
vals[12:15] = [-1.2,0.9,-2.4]
vals[15:18] = [0.1,0.4,1.0]
uvals=[0]
kvals=[0]
evals=[0]

xs=[]
ys_e=[]
ys_u=[]
ys_k=[]

frame = 0
def animate(i):
  global vals,frame,h
  frame = frame+1
  if (frame % 100 == 0): print(frame)
  for i in range(stepsperframe):
    if (doAdaptive):
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
         e1 = sqrt(magsq(vals1[0:3]-vals2[0:3]))/30
         e2 = sqrt(magsq(vals1[3:6]-vals2[3:6]))/30
         e3 = sqrt(magsq(vals1[6:9]-vals2[6:9]))/30
         epsilon = max(e1,e2,e3,1e-18)
         rho = delta*h/epsilon
         
         # Calculate new t, h and r
         if rho >= 1.0: #can increase h, keep this point
           passedError = True
           vals = vals1 ### set new values
           h = min(h*rho**0.25,2.0*h,hmax) ### don't let h get tooo big!
         else: ### nope, make h smaller, redo
           h *= rho**0.25
    else:
      h = hstart
      k1 = h*f(vals)
      k2 = h*f(vals+0.5*k1)
      k3 = h*f(vals+0.5*k2)
      k4 = h*f(vals+k3)
      vals += (k1+2*k2+2*k3+k4)/6

  planet1.set_data([vals[0]],[vals[1]])
  planet1.set_3d_properties([vals[2]])
  planet2.set_data([vals[3]],[vals[4]])
  planet2.set_3d_properties([vals[5]])
  planet3.set_data([vals[6]],[vals[7]])
  planet3.set_3d_properties([vals[8]])
  u_val, k_val, e_val = calcEnergies(vals)
  xs.append(frame)
  ys_u.append(u_val)
  ys_k.append(k_val)
  ys_e.append(e_val)
  u.set_data(xs,ys_u)
  k.set_data(xs,ys_k)
  e.set_data(xs,ys_e)
  return planet1,planet2,planet3,u,k,e,

maxaxis = 8
nframe=5000
# Setting the axes properties
fig = plt.figure()
ax = fig.add_subplot(2,1,1,projection="3d") 

ax.set(xlim3d=(-maxaxis,maxaxis), xlabel='X')
ax.set(ylim3d=(-maxaxis,maxaxis), ylabel='Y')
ax.set(zlim3d=(-maxaxis,maxaxis), zlabel='Z')
planet1, = ax.plot(vals[0], vals[1], vals[2], marker="o")
planet2, = ax.plot(vals[3], vals[4], vals[5], marker="o")
planet3, = ax.plot(vals[6], vals[7], vals[8], marker="o")
ax2 = fig.add_subplot(2,1,2)
ax2.set(xlim=(0,nframe),ylim=(-100000,100000))
u, = ax2.plot([], [], lw = 3, label='U')
k, = ax2.plot([], [], lw = 3, label='K')
e, = ax2.plot([], [], lw = 3, label='E=K+U')
plt.legend()
plt.xlabel('epoch')
plt.ylabel('funny units')

frame = 0
doAdaptive = True
ani = animation.FuncAnimation(fig, animate, interval=framerate, frames = nframe, blit=True)
outputname = 'three-body3d_adaptive'+str(doAdaptive)+'.mp4'
ani.save(outputname, fps=60, extra_args=['-vcodec', 'libx264'])
