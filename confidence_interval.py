import numpy as np
import scipy.stats as sc
import pandas as pd
#import statsmodels.api as sm
#from statsmodels.stats.proportion import proportion_confint


("""
data = [12,12,13,15,14,15,17]
confidence_interval = sc.t.interval(.95, len(data)-1, np.mean(data), sc.sem(data))
print(confidence_interval)
""")

x = pd.read_csv('Heart.csv')
df= pd.DataFrame(x)
print(x.head(5))


data = x['chol']
confidence_interval = sc.t.interval(.95, len(data)-1, np.mean(data), sc.sem(data))
print(confidence_interval)


male = df[df['sex'] == 1]
male_chol = male['chol']
print(male.head(5))
confidence_interval = sc.t.interval(.95, len(male_chol)-1, np.mean(male_chol), sc.sem(male_chol))
print(confidence_interval)


female = df[df['sex'] == 0]
print(female.head(5))
female_chol = female['chol']
confidence_interval = sc.t.interval(.95, len(female_chol)-1, np.mean(female_chol), sc.sem(female_chol))
print(confidence_interval)

newData = df['fbs']
x = sum(df['fbs'])
n = len(df['fbs'])
#proportion_confint(count = x, # Number of "successes"
                   #nobs=n, # Number of trials
                   #alpha=(1 - 0.95))




# tstat
#tstat,pval = sc.ttest_lsamp(data1, 160)

men = []
women = []
tstat,pval = sc.ttest_ind(men, women)
#tstat,pval = sc.ttest_lsamp(data1, 160)

men = []
women = []
tstat,pval = sc.ttest_ind(men, women)



