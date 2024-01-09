import numpy as np
import matplotlib.pyplot as plt

def func(xs,a,b,c):
    k = np.sqrt(np.pi/a)*np.exp(b*b/(4*a))
    return (1./k)*np.exp(-(a*xs*xs + b*xs + c))

def func_fixed(xs):
    k = np.sqrt(np.pi/a)*np.exp(b*b/(4*a))
    return (1./k)*np.exp(-(a*xs*xs + b*xs + c))

a=0.0011
b=1.08
c=-12

##f = k*e^{-(ax*2 + bx+c)}
#L = product k*e^{-(ax*2 + bx+c)}
#ln L = ln product k*e^{-(ax*2 + bx+c)}
#ln L = sum ln(k) + sum ln(e^{-(ax*2 + bx+c)})
#ln L = sum ln(k) + sum{-(ax_i*2 + bx_i+c)}
#ln L = sum ln(k) + -aN<x^2> - bN<x> - cN
#ln L = N ln(k) + -aN<x^2> - bN<x> - cN
#K = (pi/a)^{-1/2}*e^{-b*b/(4a)}
#ln(K) = -0.5 ln(pi/a) -b*b/4a = 0.5*ln(a) - 0.5*ln(pi) - b*b/4a
#ln L = 0.5*N*ln(a) - 0.5*N*ln(pi) - N*b*b/4a -aN<x^2> - bN<x> - cN

#partial L / partial a = 0.5*N/a + N*b*b/(4*a*a) - N<x^2> = 0
#partial L / partial b = -N*b/(2a) - N<x> = 0
#partial L / partial c = -N = 0 ????

# rewrite first: 0.5*a + b*b/4 - a*a<x^2> = 0
# rewrite second: -b/2a = <x>, b = -2a<x>
# Then first again: 0.5*a + a*a*<x><x> - a*a<x^2> = 0, a = 0, NO
# 0.5a = a*a<x^2> - a*a<x><x>, 0.5 = a*(<x^2> - <x><x>), a = 1./(2*(<x^2> - <x><x>))
# and then b = -<x>/(<x^2> - <x><x>)


min=-650
max=-350
N = 50000
regen = True
points = np.array([])
if (regen):
   # Implementation of accept/reject sampling for a continuous variable.
   # Pass the Python function, the range of potential x values as a tuple (xmin, xmax), and the maximum value for f(x) to assume
   def accept_reject(func, rng, maxval):
       from random import uniform
       while True:
           xtest = uniform(*rng)
           y = func(xtest,a,b,c)/maxval
           if y > 1:
               print(f"Problem: function ({y*maxval}) has exceeded maxval {maxval} for x {xtest}")
           ytest = uniform(0,1)
           if ytest < y:
               return xtest
   
   # some points:
   for x in range(N):
     points = np.append(points,accept_reject(func, (min,max), 3500))

   # compare histogram of generated points to PDF
   plt.hist(points, bins=50, density=True)
   plt.plot(np.linspace(min,max,1000), np.frompyfunc(func_fixed, 1, 1)(np.linspace(min,max,1000)))
   plt.show()
   
   np.savetxt('fitdata3.txt',points)
else:
   points = np.genfromtxt('fitdata3.txt')
   print("nope")


N = points.size
avgx = np.sum(points)/N
avgx2 = np.sum(points*points)/N
thisa = 1./(2*(avgx2 - avgx*avgx))
thisb = -avgx/(avgx2 - avgx*avgx)
thisc = 0
print("True = ",a,b,c)
print("Estimated = ",thisa,thisb,thisc)
print("avg x = ",avgx,"and avg x^2 = ",avgx2)

#a = 1./(2*(<x^2> - <x><x>))
# and then b = -<x>/(<x^2> - <x><x>)
