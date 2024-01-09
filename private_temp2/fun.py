import numpy as np
import matplotlib.pyplot as plt

def func(xs, c):
    return -c*c*c/(2)*xs*xs*np.exp(c*xs)

def func_fixed(xs):
    return -c*c*c/(2)*xs*xs*np.exp(c*xs)

##print(integral)

c=-0.02

# f = k*x^2 * exp(cx)
# L = product k*x_i^2 * exp(cx_i)
# ln L = ln(product k*x_i^2 * exp(cx_i))
# ln L = sum ln(k x_i^2) + ln(exp (cx_i)) = 
# ln L = sum [ln(k) + ln(x_i^2) + cx_i] = Nln(k) + sum(ln(x_i^2) + csum(x_i)
# (ln L)/N = ln(k) + 2*avg ln(x) + c<avg x>

#partial ln L partial c = partial ln k / partial c + <avg x> = 0

### let c be negative, integral(0) = e^0(2/c^3) = 2/c^3, integral(infinity) = 0
### so integral 0->infty = -2/c^3, so k = -c^3/2

#Then partial ln k / partial c = d/dc (ln -3c^3/2) = d/dc (ln (-3/2) + 3*ln(c)) = 3/c
# So 3/c = -<avg x> -> c = -3/<avg x>

## check, second derivative = -3/c^2, which is negative, yay!


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
max=1000
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
           y = func(xtest,c)/maxval
           if y > 1:
               print(f"Problem: function ({y*maxval}) has exceeded maxval {maxval} for x {xtest}")
           ytest = uniform(0,1)
           if ytest < y:
               return xtest
   
   # some points:
   for x in range(N):
     points = np.append(points,accept_reject(func, (min,max), 0.02))

   # compare histogram of generated points to PDF
   #plt.hist(points, bins=50, density=True)
   #plt.plot(np.linspace(min,max,1000), np.frompyfunc(func_fixed, 1, 1)(np.linspace(min,max,1000)))
   #plt.show()
   
   np.savetxt('data.txt',points)
else:
   points = np.genfromtxt('data.txt')

N = points.size
average = np.sum(points)/N
#print(average)
c_estimated = -3/average
print("c estimated = ",c_estimated)


plt.hist(points,bins = 50, density = True)
plt.plot(np.linspace(min,max,1000), np.frompyfunc(func_fixed, 1, 1)(np.linspace(min,max,1000)))
plt.show()
