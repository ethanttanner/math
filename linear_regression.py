import numpy as np
import scipy.stats as sc
import pandas as pd
import statistics as stat
import matplotlib.pyplot as plt
import random

x = [35, 50, 75, 95, 120, 130, 145, 155, 180, 175, 185, 190]
y = [5.88, 5.93, 6.74, 6.1, 7.47, 6.93, 6.42, 7.97, 7.92, 7.62, 6.89, 7.9]

plt.scatter(x,y)
r = np.corrcoef(x,y)
print(r[0][1])

b1 = r[0][1]*np.std(y, ddof=1)/np.std(x,ddof=1)
b0 = np.mean(y)-b1*np.mean(x)
print(b1)

yhat = b1*np.array(x)+b0
print(yhat)

err = y - yhat
print(err)

plt.scatter(x,y)
plt.plot(x, yhat)
plt.show()

plt.scatter(x,err)




z = [40,60, 90]
nyhat = b1*np.array(z)+b0
print(nyhat) 






print("\n\n11/11/21:")
print("======================================================")
data = pd.read_csv('advertising.csv')
df = pd.DataFrame(data)

#x = df[['TV','Radio','Newspaper']]
#y = df[['Sales']]


##print(r)
x = df.drop('Sales', axis=1)
y = df['Sales']

from sklearn.model_selection import train_test_split
from sklearn.model_selection import LinearRegression

r = df.corr(method='pearson')
print(r)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.4, random_state=100)

mlr = LinearRegression()
mlr.fit(x_train, y_train)
print(mlr.coef_)
print(mlr.intercept_)


y_pred_mlr = mlr.predict(x_test)
print(y_pred_mlr)
print(y_test)









