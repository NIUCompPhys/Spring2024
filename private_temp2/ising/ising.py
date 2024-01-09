from math import exp
from numpy import empty,sum,arange
from random import random, randrange
from pylab import plot,show,imshow

#### JAAA TEMP

# Function to calculate the energy
def energy(s):
  return -J*(sum(s[0:L-1,:]*s[1:L,:]) + sum(s[:,0:L-1]*s[:,1:L]))

def calculate(J, T, N, L):

  # Initial state
  s = empty([L,L],int)
  for i in range(L):
    for j in range(L):
      if random() < 0.5:
        s[i,j] = +1
      else:
        s[i,j] = -1
  E = energy(s)
  M = sum(s)
  # Main loop
  xpoints = arange(N)
  Naccept = 1
  Etot = E
  E2tot = E*E
  Mtot = M
  M2tot = M*M

  for k in range(N):

    # Save current energy
    oldE = E

    # Choose a random spin, flip it, and calculate dE
    i = randrange(L)
    j = randrange(L)
    # We could probably be move clever since "most" of the calculation doesn't change, only nearest neighbors
    # So let's try that here. We will flip the spin AFTER after calculating dE, too
    #E = energy(s)
    #deltaE = E - oldE
    #be more careful now about the boundary conditions, too
    iup = i+1
    idown = i-1
    jup = j+1
    jdown = j-1
    if (iup == L): iup = 0
    if (idown == 0): idown = L-1
    if (jup == L): jup = 0
    if (jdown == 0): jdown = L-1
    ### Factor of two comes from (1 - (-1) = 2)
    deltaE = 2*J*s[i,j]*(s[iup,j]+s[idown,j]+s[i,jup]+s[i,jdown])
    E = deltaE + oldE
    ### Flip!
    s[i,j] = -s[i,j]
    # Decide whether to accept the move or not
    if deltaE > 0.0: ### If dE < 0 we always keep things
      if random() > exp(-deltaE/T): 
        # Move rejected, revert to old state, don't need to recalculate M, we haven't changed it
        s[i,j] = -s[i,j]
        E = oldE
        continue
    # Accepted! Calculate new values
    Naccept = Naccept + 1
    M = sum(s)
    Etot = Etot + E
    E2tot = E2tot + E*E
    Mtot = Mtot + M
    M2tot = M2tot + M*M

  chi = (M2tot-Mtot)/Naccept
  c = (E2tot - Etot)/Naccept
  ## return results
  return(chi,c,Naccept,s)

J=0.5
T=3.0
N=20000000
L=50
chi,c,Naccept,s = calculate(J,T,N,L)
imshow(s)
show()
