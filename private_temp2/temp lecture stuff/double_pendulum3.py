# Double pendulum, some interesting plots (not animation)
from math import sin,cos,pi
from numpy import arange,array
from matplotlib.pyplot import plot,show,legend,figure,xlabel,ylabel,savefig

# Function f(r)
def f(r,l):
  g = 9.81
  theta1 = r[0]
  theta2 = r[1]
  omega1 = r[2]
  omega2 = r[3]
  ftheta1 = omega1
  ftheta2 = omega2
  fomega1 = -(omega1*omega1*sin(2*theta1-2*theta2) + 2*omega2*omega2*sin(theta1-theta2) + (3*sin(theta1) + sin(theta1-2*theta2))*g/l)/(3-cos(2*theta1-2*theta2))
  fomega2 = (4*omega1*omega1*sin(theta1-theta2) + omega2*omega2*sin(2*theta1-2*theta2) - 2*(sin(theta2)-sin(2*theta1-theta2))*g/l)/(3-cos(2*theta1-2*theta2))
  return array([ftheta1,ftheta2,fomega1,fomega2],float)


# Main Program from arbitrary starting values
def runDoublePendulum(theta1,theta2,omega1,omega2,tf=5.,nstep=3000000,l = 0.4):
  t = 0
  h = (tf-t)/nstep
  r = array([theta1,theta2,omega1,omega2])
  thetas_1 = []
  thetas_2 = []
  omegas_1 = []
  omegas_2 = []

  # Main loop
  while t < tf:
    ### fix values so we're not sensitive to 2pi wrap
    while (r[0] < pi): r[0] += pi
    while (r[1] < pi): r[1] += pi
    while (r[0] > pi): r[0] -= pi
    while (r[1] > pi): r[1] -= pi
    thetas_1.append(r[0])
    thetas_2.append(r[1])
    omegas_1.append(r[2])
    omegas_2.append(r[3])

    k1 = h*f(r,l)
    k2 = h*f(r+0.5*k1,l)
    k3 = h*f(r+0.5*k2,l)
    k4 = h*f(r+k3,l)
    r += (k1+2*k2+2*k3+k4)/6
  
    # Update
    t += h
  return (thetas_1, thetas_2, omegas_1, omegas_2)

theta1_init = 1.0
theta2_init = -1.1
omega1_init = 0.3

omega2_init_a = -3.0
omega2_init_b = 3.0
nomega2 = 200

step = (omega2_init_b - omega2_init_a)/nomega2
omegas2s_init = arange(omega2_init_a,omega2_init_b,step)
###print(omegas2s_init)
theta1_fs = []
theta2_fs = []

for omega2_init in omegas2s_init:
  print(omega2_init)
  ### do less steps and run for less time to make this more tractable for now
  thetas_1, thetas_2, omegas_1, omegas_2 = runDoublePendulum(theta1_init, theta2_init, omega1_init, omega2_init, 50, 100000)
  theta1_fs.append(thetas_1[-1])
  theta2_fs.append(thetas_2[-1])

plot(omegas2s_init,theta1_fs,label="Theta1")
plot(omegas2s_init,theta2_fs,label="Theta2")
xlabel("Initial Omega2")
ylabel("Final angle")
legend()
savefig("plot.png")
