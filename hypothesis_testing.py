import numpy as np
import scipy.stats as sc
import pandas as pd
import statistics as stat
import matplotlib.pyplot as plt
import random


x = pd.read_csv('ncbirths.csv')
df1= pd.DataFrame(x)
df = df1.dropna()
sample = df.sample(150)

frequency_table = pd.crosstab(df.lowbirthweight == "low", df.habit == "smoker", margins = True, normalize='index')
print(frequency_table)







print("Age summary statistics: ")
print(sample.fage.mean())
print(sample.fage.median())
print(sample.fage.min())
print(sample.fage.max())
print(sample.fage.std())

#print(df.fage)
#print(df.fage.mean())
#print(df.fage.median())
#print(df.fage.min())
#print(df.fage.max())
#print(df.fage.std())





#data = x['chol']
#confidence_interval = sc.t.interval(.95, len(data)-1, np.mean(data), sc.sem(data))
#print(confidence_interval)