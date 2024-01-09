from math import sin,cos,pi
from numpy import arange,array
from vpython import rate, vector, sphere,cylinder

g = 9.81
l = 0.4
R = 0.05
W = 0.01
framerate = 200
stepsperframe = 20

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
#theta1 = theta2 = 0.5*pi
#omega1 = omega2 = 0.0
r = array([theta1,theta2,omega1,omega2],float)

# Set up graphics
pivot = sphere(pos=vector(0,0,0),radius=R)
x1 = l*sin(theta1)
y1 = -l*cos(theta1)
x2 = l*(sin(theta1)+sin(theta2))
y2 = -l*(cos(theta1)+cos(theta2))
arm1 = cylinder(pos = vector(0,0,0),axis=vector(x1,y1,0),radius=W)
arm2 = cylinder(pos = vector(x1,y1,0), axis=vector(x2-x1,y2-y1,0), radius=W)
bob1 = sphere(pos = vector(x1,y1,0),radius=R)
bob2 = sphere(pos = vector(x2,y2,0),radius=R)

# Main loop
while True:
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
    rate(framerate)
    arm1.axis = vector(x1,y1,0)
    arm2.pos = vector(x1,y1,0)
    arm2.axis = vector(x2-x1,y2-y1,0)
    bob1.pos = vector(x1,y1,0)
    bob2.pos = vector(x2,y2,0)