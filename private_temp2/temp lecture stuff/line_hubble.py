import numpy as np

# distances in Mpc, x
x = np.array([ 0.032, 0.034, 0.214, 0.263, 0.275, 0.275, 0.45, 0.5,
      0.5,   0.63,  0.8,   0.9,   0.9,   0.9,   0.9,  1.0,
      1.1,   1.1,   1.4,   1.7,   2.0,   2.0,   2.0,  2.0 ])

# velocities in km/s, y
y = np.array([ +170, +290, -130, -70,  -185, -220, +200, +290,
      +270, +200, +300, -30,  +650, +150, +500, +920,
      +450, +500, +500, +960, +500, +850, +800, +1090 ])

n = float(len(y))
sum_x2 = np.sum(x*x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x*y)

a = (1./n*sum_xy*sum_x-1./n*sum_y*sum_x2)/(1./n*sum_x*sum_x - sum_x2)
b = (1./n*sum_y*sum_x - sum_xy)/(1./n*sum_x*sum_x - sum_x2)

print(a,b)