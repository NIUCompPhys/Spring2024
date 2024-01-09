from numpy import empty, arange, linspace, zeros
from math import pi,cos,sin,exp
from dcst import dst,idst
from vpython import curve,rate,canvas,color,vector

#constants
L = 1.0e-8
#N = 100
N = 1000
a = L/N
m = 9.109e-31
hbar = 1.055e-34

x0 = L/2
sigma = 1.0e-10
kappa = 5.0e10

tmax = 1.0e-13
yscale = 1e-9
framerate=1000
tstep = 1.0e-18

C = pi*pi*hbar/(8*m*L*L)

# Create the arrays for the Re and Im parts of psi
repsi = zeros(N,float)
impsi = zeros(N,float)

for n in range(1,N):
  xn = n*a
  gauss = exp(-(xn-x0)**2/(2*sigma**2))
  repsi[n] = -1*gauss*cos(kappa*xn)
  impsi[n] = -1*gauss*sin(kappa*xn)


# Perform forward transforms to calculate alpha_k, eta_k
alpha = yscale*dst(repsi)
eta = yscale*dst(impsi)

# Graphics
###display(center = [0.5*L,0.0])
###c = curve(x=linspace(a,L-a,N-1))
x = linspace(0,L,N+1)
pos = []
for xval in x:
  pos.append(vector(xval,yscale,0))
c = curve(pos = pos,color=color.red)



# Main loop
b = empty(N,float)
i=0
for t in arange(0.0,tmax,tstep):
  for k in range(1,N):
    angle = C*k*k*t
    b[k] = alpha[k]*cos(angle) - eta[k]*sin(angle)
  repsi = idst(b)
  rate(framerate)
  #c.y = repsi
  for k in range(1,N): c.modify(k, y = repsi[k])
  #if (i%100 == 0): print(repsi)
  #i = i+1
