from numpy import empty, arange, linspace, exp, real, full, array, append, zeros
from vpython import curve,rate,canvas,color,vector
from banded import banded

#constants
L = 1.0e-8
N = 500
a = L/N
m = 9.109e-31
hbar = 1.055e-34
x0 = L/2
sigma = 1.0e-10
kappa = 5.0e10

tmax = 1.0e-13
yscale = 1e-9
framerate=1000
h = 1e-18
###h = 1e-16

C = 1j*hbar/(4*m*a*a)
a1 = 1 + 2*h*C
a2 = -h*C
b1 = 1 - 2*h*C
b2 = h*C

# Create the initial arrays of x and psi values
x = linspace(0,L,N+1)
psi = zeros(N+1)
for i in range(N+1):
  q = (1-((x[i]-x0)/(2*L)**2))
  if (q > 0): psi[i] = q
  else: psi[i] = 0

psi = psi*exp(1j*kappa*x)*5*L

# Create the tridiagonal array A
A = empty([3,N-1],complex)
A[0,:] = a2
A[1,:] = a1
A[2,:] = a2

print(len(psi))

pos = []
for xval in x:
  pos.append(vector(xval,yscale,0))
c = curve(pos = pos,color=color.red)  
## main loop for the Crank-Nicolson method
nstep = tmax/h
i = 0

for t in arange(0,tmax,h):
    i = i+1
    v = b2*psi[0:N-1] + b1*psi[1:N] + b2*psi[2:N+1]
    psi[1:N] = banded(A,v,1,1)
    rate(framerate)
    for entry in range(N+1):
      c.modify(entry, y = yscale*real(psi[entry]))

