from pylab import plot,show,xlabel,ylabel,xlim,yscale,savefig,clf
import datetime
from matplotlib.finance import date2num
import numpy as np
import nfft

firstday=0

filename='attendance_all.txt'
dates=[]
attendances=[]
max=1e8
#max=100

with open(filename) as f:
  for line in f:
    vals = line.strip().split(",")
    if len(vals) < 3: continue
    if (vals[2] == ''): continue
    if ('paid' in vals[2]): continue
    if (vals[2] == '0'): continue ## presumably not valid
    if ('"' in vals[2]): continue		
    if (vals[1] != "\"NYA\""): continue ### only look at NY Yankees for now
    date_string = vals[0].strip("\"")
    year = int(date_string[:4])
    month = int(date_string[4:6])
    day = int(date_string[6:8])
    float_days = date2num(datetime.datetime(year, month, day))
    if (firstday < 1): firstday = float_days
    #print(float_days)
    dates.append(float_days-firstday)
    attendances.append(float(vals[2]))
    if (len(dates) > max): break

if (len(dates) %2 != 0): ### kludge! we need an even number of entries
  dates=dates[1:]
  attendances=attendances[1:]

print("Number of games = ",len(dates))
plot(dates,attendances)
xlabel("Days since start")
ylabel("Attendance for Yankees")
savefig("YankeesAttendance.png")
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

#print(dates)
#print(attendances)

###f=nfft.nfft(dates,attendances,len(dates))
f=nfft.nfft_adjoint(dates,attendances,len(dates))
f2 = abs(f)**2
n=len(f2)
xs=[]
print("themax =",themax,"and n = ",n)
#######for i in range(n): xs.append(2*np.pi*themax/(i+1.)) ### convert to frequency with appropriate 2pi factor
xs=2*np.pi*np.arange(n)
#print(xs)

plot(xs,f2)
yscale("log")
xlabel("frequency (days)")
ylabel("c_k^2")
xlim(325,400)
savefig("c_k2_v_frequency0_yanks.png")
xlim(0,1000)
savefig("c_k2_v_frequency1_yanks.png")
xlim(0,100)
savefig("c_k2_v_frequency2_yanks.png")
xlim(0,20)
savefig("c_k2_v_frequency3_yanks.png")
xlim(60,80)
savefig("c_k2_v_frequency4_yanks.png")