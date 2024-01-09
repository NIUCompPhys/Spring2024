import csv
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt,log

hr_perab=[]
log_hr_perab=[]
angle=[]
velocity=[]
babip=[]
weights=[]
with open('stats3.csv', newline='') as csvfile:
   spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
   start = True
   for row in spamreader:
       if (start):
	       start = False
       elif (row[0] != "null"):
           ab=float(row[3])	
           hr=float(row[4])
           if (hr > 0.0):
             ba = float(row[5])
             babip.append(ba)
             log_hr_perab.append(log(hr/ab))
             hr_perab.append(hr/ab)
             #print(hr/ab)
             angle.append(float(row[12]))
             velocity.append(float(row[11]))
             ### sigma = bavg / sqrt(n), weight = sqrt(n) / bavg
             #print(row[5],row[12])
             weights.append(sqrt(ab)/ba)
        #print(row)
	   ##print(', '.join(row))

#xmin=0
#xmax=30	
#coefficients=np.polyfit(angle,hr_perab,2,w=weights)
#print(coefficients)
#poly = np.poly1d(coefficients)
#new_x = np.linspace(xmin,xmax)
#new_y = poly(new_x)
#plt.plot(angle,hr_perab,"o",new_x,new_y)
#plt.xlim(xmin,xmax)
#plt.xlabel("angle")
#plt.ylabel("ln (HR / AB)")
#plt.savefig("HRrate_v_angle.png")
#
#xmin=70
#xmax=100
#coefficients, residuals, _, _, _ = np.polyfit(velocity,log_hr_perab,1,w=weights,full=True)
#print(coefficients)
#print("chi2 ndf =",residuals / (len (velocity) - 1))
#poly = np.poly1d(coefficients)
#new_x = np.linspace(xmin,xmax)
#new_y = poly(new_x)
#plt.plot(velocity,log_hr_perab,"o",new_x,new_y)
#plt.xlim(xmin,xmax)
#plt.xlabel("velocity")
#plt.ylabel("ln (HR / AB)")
#plt.savefig("log_HRrate_v_velocity.png")
##

xmin=70
xmax=100
coefficients, residuals, _, _, _ = np.polyfit(velocity,log_hr_perab,2,w=weights,full=True)
print(coefficients)
print("chi2 ndf =",residuals / (len (velocity) - 1))
poly = np.poly1d(coefficients)
new_x = np.linspace(xmin,xmax)
new_y = poly(new_x)
plt.plot(velocity,log_hr_perab,"o",new_x,new_y)
plt.xlim(xmin,xmax)
plt.xlabel("velocity")
plt.ylabel("ln (HR / AB)")
plt.savefig("log_pol2_HRrate_v_velocity.png")
#
#
#
#xmin=70
#xmax=100
#coefficients, residuals, _, _, _ = np.polyfit(velocity,hr_perab,1,w=weights,full=True)
#print(coefficients)
#print("chi2 ndf =",residuals / (len (velocity) - 1))
#poly = np.poly1d(coefficients)
#new_x = np.linspace(xmin,xmax)
#new_y = poly(new_x)
#plt.plot(velocity,hr_perab,"o",new_x,new_y)
#plt.xlim(xmin,xmax)
#plt.xlabel("velocity")
#plt.ylabel("(HR / AB)")
#plt.savefig("HRrate_v_velocity.png")
##
#


xmin=0
xmax=30
coefficients=np.polyfit(angle,babip,2,w=weights)
print(coefficients)
poly = np.poly1d(coefficients)
new_x = np.linspace(xmin,xmax)
new_y = poly(new_x)
plt.plot(angle,babip,"o",new_x,new_y)
plt.xlim(xmin,xmax)
plt.xlabel("angle")
plt.ylabel("batting avg")
plt.savefig("avg_v_angle.png")

#xmin=70
#xmax=100
#coefficients=np.polyfit(velocity,babip,2,w=weights)
#print(coefficients)
#poly = np.poly1d(coefficients)
#new_x = np.linspace(xmin,xmax)
#new_y = poly(new_x)
#plt.plot(velocity,babip,"o",new_x,new_y)
#plt.xlim(xmin,xmax)
#plt.xlabel("velocity")
#plt.ylabel("batting avg")
#plt.savefig("avg_v_velocity.png")