#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 22:16:24 2021

@author: ethantanner
"""

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
print("==================================")

print("Age::")
print(round(sample.fage.mean(), 2))
print(sample.fage.median())
print(sample.fage.min())
print(sample.fage.max())
print(round(sample.fage.std(), 2))
print("==================================")

print("Weeks:")
print(round(sample.weeks.mean(), 2))
print(sample.weeks.median())
print(sample.weeks.min())
print(sample.weeks.max())
print(round(sample.weeks.std(), 2))
print("==================================")

print("Weight:")
print(round(sample.weight.mean(), 2))
print(sample.weight.median())
print(sample.weight.min())
print(sample.weight.max())
print(round(sample.weight.std(), 2))
print("\n\n==================================")
print("ages")

print(sc.ttest_1samp(sample.fage <= 25, 0.05))
meanAge = sample['fage']
print(sc.t.interval(.95, len(meanAge)-1, np.mean(sample.fage), sc.sem(meanAge)))

print("\n\n==================================")

print(sc.ttest_1samp(sample.weeks, 39))
weeks = sample['weeks']
print(sc.t.interval(.95, len(weeks)-1, np.mean(weeks), sc.sem(weeks)))
print("\n\n============")
print(sc.ttest_1samp(sample.weight, 7))
weight = sample['weight']
print("\n\n", sc.t.interval(.95, len(weight)-1, np.mean(weight), sc.sem(weight)))
#H(0)- That the percentage of low birth weight children in North Carolina is above 6%.
#H(a)- That the percentage of low birth weight children in North Carolina is not above 6%.
print("\n\n============")
print("Low birth weight")


low = sample[sample['lowbirthweight'] == "low"]
print(sc.ttest_1samp(sample['lowbirthweight'] == "low", 0.06))

print(len(low)/len(sample))
print(len(low), "/", len(sample))
print(sc.t.interval(.95, len(weight)-1, np.mean(low.weight), sc.sem(low.weight)))

#print(low)

#i. Determine if there is sufficient evidence to conclude the percentage of mothers who smoke in North Carolina is above 10%.
#H(0)- That the percentage of mothers who smoke in North Carolina is above 10%.
#H(a)- That the percentage of mothers who smoke in North Carolina is not above 10%.

print("\n\n============")
print("Mothers who Smoke!")

smokers = sample[sample['habit'] == "smoker"]
print(sc.ttest_1samp(sample['habit'] == "smoker", 0.1))

print(len(smokers)/len(sample))
print(len(smokers), "/", len(sample))
print(sc.t.interval(.95, len(smokers)-1, len(smokers)/len(sample), sc.sem(low.weight)))

















