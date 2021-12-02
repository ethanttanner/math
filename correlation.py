import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import random
import statistics as stats
import scipy.stats as sc



x = 5, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12
y = 4.2, 5, 5.2, 5.9, 6, 6.2, 6.1, 6.9, 7.2, 8, 8.3, 7.4, 8.4, 7.8, 8.5, 9.5

ax = plt.gca()
ax.set_xlim([0, 30])
ax.set_ylim([0, 20])

print(np.corrcoef(x,y))
plt.xlabel("X")
plt.ylabel("Y")
plt.scatter(x, y)
plt.show()

x2 = []
y2 = []
for i in range(len(x)):
    x2.append( x[i] * 2 )
    y2.append( y[i] * 2 )
    
ax = plt.gca()
ax.set_xlim([0, 30])
ax.set_ylim([0, 20])

print(np.corrcoef(x2,y2))
plt.xlabel("X")
plt.ylabel("Y")
plt.scatter(x2, y2)
plt.show()

x10 = []
y10 = []
for i in range(len(x)):
    x10.append( x[i] * 10 )
    y10.append( y[i] * 10 )
    
ax = plt.gca()
ax.set_xlim([0, 200])
ax.set_ylim([0, 150])

print(np.corrcoef(x10,y10))

plt.scatter(x10, y10)
plt.show()



casesOfLymeDisease = [3,2,2,4,5,15,22,13,6,5,4,1]
drowningDeaths = [0,1,2,1,2,9,16,5,3,3,1,0]


print(np.corrcoef(drowningDeaths,casesOfLymeDisease))

plt.scatter(drowningDeaths, casesOfLymeDisease)
plt.show()


genders = ["Female", "Female", "Female", "Female", "Female",  "Female", "Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male"]

MRICounts = [ 816932, 951545, 991305, 833868, 856472, 852244, 790619, 866662, 857785, 948066, 949395, 1001121, 1038437, 965353, 955466, 1079549, 924059, 955003, 935494, 949589]
IQs = [ 133, 137, 138, 132, 140, 132, 135, 130, 133, 133, 140, 140, 139, 133, 133, 141, 135, 139, 141, 144]

plt.xlabel("IQs")
plt.ylabel("MRI Counts")
print(np.corrcoef(IQs[10:20],MRICounts[10:20]))
#plt.scatter(IQs, MRICounts)
plt.scatter(IQs[0:9], MRICounts[0:9])
plt.scatter(IQs[10:20], MRICounts[10:20], marker='v')
plt.show()

maleDrivers = [12, 6424, 6941, 18068, 20406, 19898, 14340, 8194, 4803]
maleCrashes = [227, 5180, 5016, 8595, 7990, 7118, 4527, 2274, 2022]
femaleDrivers = [12, 6139, 6816, 17664, 20063, 19984, 14441, 8400, 5375]
femaleCrashes = [77, 2113, 1531, 2780, 2742, 2285, 1514, 938, 980]
#print(len(maleDrivers), len(maleCrashes))
#print(len(femaleDrivers), len(femaleCrashes))
plt.xlabel("Number of Licensed Drivers (000s)")
plt.ylabel("Number of Fatal Crashes")
print(np.corrcoef(maleDrivers,maleCrashes))
print(np.corrcoef(femaleDrivers,femaleCrashes))

plt.scatter(maleDrivers, maleCrashes, marker='s')
plt.scatter(femaleDrivers, femaleCrashes, marker='+')
plt.show()



