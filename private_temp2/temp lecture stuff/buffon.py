import random
import numpy
from math import sqrt,atan,cos,pi
import matplotlib.pyplot as plt
n = 100000
npass = 0
L = 1.
d = 2.
piover2 = pi/2.
thetas = []

for i in range(n):
    x1 = random.uniform(0,d) ## starting point

    ### now pick random direction, want it to be forward, thankfully arctan returns values between -pi/2 and pi/2
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    theta = numpy.arctan(y/x)
    thetas.append(theta)
    #theta = random.uniform(-piover2,piover2)

    x2 = x1 + L*cos(theta)
    if (x2 > d): npass = npass+1

    
pi = 2*L*n/(d*npass)
print("Pi = ",pi)
plt.plot(thetas)
plt.show()
