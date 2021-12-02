import pandas as pd
from matplotlib import pyplot as plt

print("Justice Ages: ")
df = pd.read_csv('3_r_3.csv')
mean1 = df['Age'].mean()
median1 = df['Age'].median() 
mode = df['Age'].mode()
minAge = df['Age'].min()
maxAge = df['Age'].max()
std = df['Age'].std()

# 1A
print ('Mean: ' + str(round(mean1, 2)))
print ('Median: ' + str(round(median1)))
print('Mode: ' + str(mode[0]) + ", " + str(mode[1]))

# 1B
print('Range: ' + str(minAge) + ' - ' + str(maxAge))
print( 'Standard Deviation: ' + str(round(std, 2)))

# 1C
sample = df.sample(4)
print("\nSample1:")
print("Mean: " + str(round(df['Age'].mean())))
print("Deviation: " + str(round(sample['Age'].std(), 2)))

sample2 = df.sample(4)
print("\nSample2: ")
print("Mean: " + str(round(df['Age'].mean())))
print("Deviation: " + str(round(sample2['Age'].std(), 2)))


speedingTickets = [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 2, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0 ,0 ,0, 0, 1, 0 ]


# 2A
plt.hist(speedingTickets, color='black') 
plt.xlabel("# of tickets")
plt.ylabel("# of Students")
plt.title('Parking tickets in the last month: ')
plt.show()

# 2B
# the mean will probalby be less than the median becasuse the median will probably be a 1, and there are far more 0's than 1's & 2's.


#print(round(sum(speedingTickets)/len(speedingTickets), 2))
print("\nParking Tickets: ")
st = pd.read_csv('3_r_4.csv')
ticMean = st['Tickets Issued'].mean()
ticMedian = st['Tickets Issued'].median() 
ticMode = st['Tickets Issued'].mode()


# 2C
print ('Mean: ' + str(round(ticMean, 2)))
print ('Median: ' + str(round(ticMedian)))

# 2D
print("Mode: " + str(ticMode[0]))
#print('Mode: ' + str(ticMode[0]) + ", " + str(ticMode[1]))





ps = pd.read_csv('3_r_10.csv')
presMean = ps['Presidential Inaugural Addresses'].mean()
presMedian = ps['Presidential Inaugural Addresses'].median() 
presMin = ps['Presidential Inaugural Addresses'].min() 
presMax = ps['Presidential Inaugural Addresses'].max() 
presidentialSTDS = ps['Presidential Inaugural Addresses'].std()

# 3A
print('\nPresidential Inaugural Addresses:')
print ('Mean: ' + str(round(presMean, 2)))
print ('Median: ' + str(round(presMedian)))

# 3B
q1 = ps['Presidential Inaugural Addresses'].quantile(0.25)
q3 = ps['Presidential Inaugural Addresses'].quantile(0.75)
print("Q1: " + str(round(q1)))
print("Q2: " + str(round(presMedian)))
print("Q3: " + str(round(q3)))

# 3C
print("\nFive Number Summary: ")
print( str(presMin) + ", " + str(round(q1)) + ", " + str(round(presMedian)) + ", " + str(round(q3)) + ", " + str(presMax))

# 3D
print( 'Standard Deviation: ' + str(round(presidentialSTDS)))

# 3E
# yes- just the 8445


# 3F
plt.boxplot(ps['Presidential Inaugural Addresses']) 
plt.xlabel("Presidents")
plt.ylabel("# of words")
plt.title('Inaugural word count: ')
plt.show()


# 3G
# Most of the presidents hover around 2134 words and in the range of 1427-2885 words this is the range of the quartiles, then there are a couple of outliers.

 
# 3H
#The mean, there are more values that are large than there are small.

# 3I
#I think the range because it shows the high and low, it just depends on waht president is speaking, and however long he wants to talk for, this best shows the range of possibilities. 

