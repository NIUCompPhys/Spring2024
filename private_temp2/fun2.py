import numpy as np
import matplotlib.pyplot as plt

def func(xs, p):
    return p*p*xs*np.exp(p*xs)

def func_fixed(xs):
    return p*p*xs*np.exp(p*xs)

p=-0.05

#### if we instead do f = q*x*exp(px), p is negative, integral(0) = -1/c^2, integral(infty) = 0
# so integral 0->infty = -1/p^2, so q = -p^2
# f = q*x * exp(px)
# L = product q*x_i * exp(px_i)
# ln L = ln(product q*x_i * exp(px_i))
# ln L = sum ln(q x_i) + ln(exp (px_i)) = 
# ln L = sum [ln(q) + ln(x_i) + px_i] = Nln(q) + sum(ln(x_i) + psum(x_i)
# (ln L)/N = ln(q) + avg ln(x) + p<avg x>
# partial ln L partial p = partial (ln (q) + <avg x>) partial p = d/dp (ln -p^2) =
# = d/dp(ln -1 + ln p^2) = d/dp (2 ln p) = 2/p, so 2/p = -<avg x>, p = -2/<avg x>


min=0
max=300
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
           y = func(xtest,p)/maxval
           if y > 1:
               print(f"Problem: function ({y*maxval}) has exceeded maxval {maxval} for x {xtest}")
           ytest = uniform(0,1)
           if ytest < y:
               return xtest
   
   # some points:
   for x in range(N):
     points = np.append(points,accept_reject(func, (min,max), 0.02))

   # compare histogram of generated points to PDF
   plt.hist(points, bins=50, density=True)
   #plt.plot(np.linspace(min,max,1000), np.frompyfunc(func_fixed, 1, 1)(np.linspace(min,max,1000)))
   plt.show()
   
   np.savetxt('data2.txt',points)
else:
   points = np.genfromtxt('data2.txt')

N = points.size
average = np.sum(points)/N
print("average =",average)
p_estimated = -2/average
print("p estimated = ",p_estimated)
print(p)

plt.hist(points,bins = 50, density = True, label="data")
plt.plot(np.linspace(min,max,1000), np.frompyfunc(func_fixed, 1, 1)(np.linspace(min,max,1000)),label="function")
plt.legend()
plt.show()
