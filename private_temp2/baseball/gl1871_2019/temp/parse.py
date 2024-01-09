from pylab import plot,show,xlabel,ylabel,xlim,yscale,savefig,clf
import datetime
from matplotlib.finance import date2num
import numpy as np
import nfft

firstday=0

filename='attendance_all.txt'
dates=[]
attendances=[]
max=1e15
###max = 100 ## for testing

with open(filename) as f:
  for line in f:
    vals = line.strip().split(",")
    if len(vals) < 2: continue
    if (vals[1] == ''): continue
    if ('paid' in vals[1]): continue
    if (vals[1] == '0'): continue ## presumably not valid
    if ('"' in vals[1]): continue		
    date_string = vals[0].strip("\"")
    year = int(date_string[:4])
    month = int(date_string[4:6])
    day = int(date_string[6:8])
    float_days = date2num(datetime.datetime(year, month, day))
    if (firstday < 1): firstday = float_days
    #print(float_days)
    dates.append(float_days-firstday)
    attendances.append(float(vals[1]))
    if (len(dates) > max): break

print("Number of games =",len(dates))
plot(dates,attendances)
xlabel("Days since start (Opening Day 1900)")
ylabel("Attendance")
savefig("attendance.png")
clf()

### transform the dates
themax = np.max(dates)
themin = np.min(dates) ### should be zero but doesn't have to be?
span = themax - themin
dates = dates - themin

### get it again, we need the new max for later
themax = np.max(dates)

dates = dates / span 
dates = dates -0.5 ### -0.5 to 0.5

###f=nfft.nfft(dates,attendances,len(dates))

max = 100000  ### max k to evaluate at

f=nfft.nfft_adjoint(dates,attendances,max)
f2_temp = abs(f)**2

### cut these off, we don't need to double them!
n_temp=len(f2_temp)
f2 = f2_temp[int(n_temp/2):]
n=len(f2)
print("n=",n,"and themax = ",themax)

plot(f2)
yscale("log")
savefig("f2.png")

clf()

xs=[]
###############for i in range(n): xs.append(2*np.pi*themax/(i+1)) ### convert to frequency with appropriate 2pi factor
####xs=(np.arange(n)+1)*themax/n
### f2 is the wave number, so we want 1/i, but then it goes from 0 = 1/0 = infinite to max = 1/max, but then multiply each by themax range for dates)
xs = []
for i in range(n): xs.append(themax/(i+1)) ### missing a factor of 2pi???? or not?

plot(xs,f2)
yscale("log")
xlabel("frequency (days)")
ylabel("c_k^2")
savefig("c_k2_all.png")

xlim(325,400)
savefig("c_k2_v_frequency_year.png")
xlim(0,1000)
savefig("c_k2_v_frequency_3years.png")
xlim(0,100)
savefig("c_k2_v_frequency_months.png")
xlim(0,20)
savefig("c_k2_v_frequency_onemonth.png")
xlim(0,10)
savefig("c_k2_v_frequency_oneweek.png")
