import pandas as pd
import statistics as stats
import scipy.stats as sc

df = pd.read_csv('soccer_results.csv')
data = pd.DataFrame(df)
df['total'] = df['home_score'] + df['away_score']
#print(df['goals'])

df[['year', 'month', 'day']] = df['date'].str.split('-', expand = True)
#df1 = df.groupby['year'].sum()
#print(df1)
print(df.head())

print("By year: ")
df1 = df.groupby(['year']).sum()
#print(df1.tail(20))
freq = df1.value_counts(['total'])
print(freq.head(10))

print("By month: ")
df2 = df.groupby(['month']).sum()
#print(df1.tail(20))
freq = df2.value_counts(['total'])
print(freq.head(10))

print("By day: ")
df3 = df.groupby(['day']).sum()
#print(df1.tail(20))
freq = df3.value_counts(['total'])
print(freq.head(10))




#sc.poisson.pmf(0,1.38)
#               x - 

#going to use group by to split the data up by 
#for year in data.date:
 #   print(year.split("-"))
    
    #df[['year', 'month', 'day']] = df['date'].str.split('-', expand = True)
    #df1 = df.groupby['year'].sum()
    #print(df1)