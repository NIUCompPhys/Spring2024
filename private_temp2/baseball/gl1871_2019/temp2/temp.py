import numpy as np
import nfft
from matplotlib.pyplot import plot,show,xlim
f=11
A=12
n=35000
x=13*np.arange(n)
y=np.random.rand(n) + A*np.sin(x*2*3.14159*f)
plot(x,y)
show()
## every 84000 for f=14
### true cycle every 150,000 for f=8

themax = np.max(x)
themin = np.min(x) ### should be zero but doesn't have to be?
span = themax - themin
x = x - themin

### get it again, we need the new max for later
themax = np.max(x)
x = x / span 
x = x -0.5 ### -0.5 to 0.5

f=nfft.nfft_adjoint(x,y,len(x))
f2 = abs(f)**2
plot(f2)
show()


n=len(f2)
xs=[]
print("themax =",themax,"and n = ",n)
##############for i in range(n): xs.append(2*np.pi*themax/(i+1.)) ### convert to frequency with appropriate 2pi factor
for i in range(n): xs.append(2*np.pi*i) ### convert to frequency with appropriate 2pi factor
plot(xs,f2)
#xlim(140000,160000)
show()
