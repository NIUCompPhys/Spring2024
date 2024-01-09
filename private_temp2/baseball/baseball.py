import csv
import numpy as np
import matplotlib.pyplot as plt

babip=[]
angle=[]
velocity=[]
with open('stats.csv', newline='') as csvfile:
   spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
   start = True
   for row in spamreader:
       if (start):
	       start = False
       elif (row[0] != "null"):
           babip.append(float(row[5]))
           angle.append(float(row[11]))
           velocity.append(float(row[10]))
       #print(row)
	   ##print(', '.join(row))

xmin=0
xmax=30
coefficients=np.polyfit(angle,babip,2)
print(coefficients)
poly = np.poly1d(coefficients)
new_x = np.linspace(xmin,xmax)
new_y = poly(new_x)
plt.plot(angle,babip,"o",new_x,new_y)
plt.xlim(xmin,xmax)
plt.xlabel("angle")
plt.ylabel("batting avg")
plt.savefig("avg_v_angle.png")

xmin=70
xmax=100
coefficients=np.polyfit(velocity,babip,2)
print(coefficients)
poly = np.poly1d(coefficients)
new_x = np.linspace(xmin,xmax)
new_y = poly(new_x)
plt.plot(velocity,babip,"o",new_x,new_y)
plt.xlim(xmin,xmax)
plt.xlabel("velocity")
plt.ylabel("batting avg")
plt.savefig("avg_v_velocity.png")