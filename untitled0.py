#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('loan_status.csv')
df = pd.DataFrame(data)
print(df.head(4))

con_table = pd.crosstab(df.grade, df.loan_status, margins=True)
print(con_table)

print(df['grade'].value_counts())

x = ['B', 'A', 'C', 'D', 'E', 'F']
y = df['grade'].value_counts()
plt.bar(x,y)
plt.show()

x = ['B', 'A', 'C', 'D', 'E', 'F']
y = df['grade'].value_counts()/sum(df['grade'].value_counts())
plt.bar(x,y)
plt.show()

con_table = pd.crosstab(df.grade,df.loan_status, margins=True).plot.bar(stacked=True)