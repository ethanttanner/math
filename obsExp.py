import numpy as np
import scipy.stats as sc
import pandas as pd
import matplotlib.pyplot as plt
import random

observed = [252, 255, 162, 331]
expected = [228, 239, 176, 357]

print(sc.chisquare(f_obs=observed,f_exp=expected))




national = pd.DataFrame(['white']*100000 + ['hispanic']*60000 + ['black']*50000 + ['asian']*15000 + ['other']*35000)
minnesota = pd.DataFrame(['white']*600 + ['hispanic']*300 + ['black']*250 + ['asian']*75 + ['other']*150)

national_table = pd.crosstab(national[0], columns='count')
minnesota_table = pd.crosstab(minnesota[0], columns='count')

national_ratios = national_table/sum(national_table['count'])
print(national_ratios)

exp = len(minnesota)*national_ratios
obs = minnesota_table
print(obs)
print(exp)
print(sc.chisquare(f_obs=obs,f_exp=exp))

