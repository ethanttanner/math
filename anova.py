import numpy as np
import scipy.stats as sc
import pandas as pd
import statistics as stat
import matplotlib.pyplot as plt
import random
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import f_oneway
import functools as r

alpha = 0.05

father = [8,0,1,4,1,5,6,16,8,9,8,8,6,4,2,4,0,0]
mother = [25,1,6,11,7,21,18,37,35,20,19,19,26,11,4,7,5,1]
other = [5,0,0,0,1,6,4,3,4,2,4,0,1,1,0,1,0,0]
alllist = father + mother + other
print("len of alllist: ", len(alllist))

  
# using reduce() + lambda
# sum of squares 
res = r.reduce(lambda i, j: i + j * j, [alllist[:1][0]**2]+alllist[1:])
  
# printing result
print ("The sum of squares of list is : " + str(res))


fvalue1, pvalue1 = f_oneway(father, mother, other)
print("P value: ", pvalue1, "\nF value: ", fvalue1)

if pvalue1 < alpha:
    print("reject the null hypothesis")
else:
    print("accept the null hypothesis")


df2 = pd.DataFrame({'score': father + mother + other, "groups": np.repeat(["Father", "Mother", "Other"], repeats = 18)})
print(pairwise_tukeyhsd(endog=df2["score"], groups=df2["groups"], alpha=0.05))




data = pd.read_csv("bipolar_disorder.csv", sep=';')
df = pd.DataFrame(data)
#print(df)
#print(df.columns)

x = df[df.Group=='Bipolar']
y = df[df.Group=='Control']
z = df[df.Group=='UD']

#print(x.Right_answers)
print(x.Right_answers.mean())
print(y.Right_answers.mean())
print(z.Right_answers.mean())

bp_right_answers = x.Right_answers
control_right_answers = y.Right_answers
UID_right_answers = z.Right_answers


print("="*53)
fvalue, pvalue = f_oneway(bp_right_answers, control_right_answers, UID_right_answers)
print("P value: ", pvalue, "\nF value: ", fvalue)

if pvalue < alpha:
    print("reject the null hypothesis")
else:
    print("accept the null hypothesis")
    
    

print(pairwise_tukeyhsd(endog=df["Right_answers"], groups=df["Group"], alpha=0.05))

