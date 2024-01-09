from numpy import empty, arange, linspace, exp, real, full, append, array, zeros
from matplotlib.pyplot import plot,show
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
x = linspace(0,L,N+1)

psi = array([])
# Create the initial arrays of x and psi values
for height in linspace(0,L/2,N/2):
  psi = append(psi,height/L)

temp = append(psi,psi[-1])
#  now flip them on the other side
psi = append(temp,psi[::-1])
psi = psi*exp(1j*kappa*x)
psi[0] = psi[N] = 0

psi2 = exp(-(x-x0)**2/(2*sigma**2))*exp(1j*kappa*x)
psi2[0] = psi2[N] = 0

psi3 = zeros(N+1)
for i in range(N+1):
  q = (1-((x[i]-x0)/(2*L)**2))
  if (q > 0): psi3[i] = q
  else: psi3[i] = 0

psi3 = psi3*exp(1j*kappa*x)*2*L

print(len(psi))
plot(psi)
plot(psi2)
plot(psi3)
show()
