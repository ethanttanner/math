import pandas as pd
import numpy as np





#sc.poisson.pmf(0,1.38)




# probability

#x = 6
#p = 1/6
#a = sc.geom.cdf(x, p)
#a = sc.geom.pdf(x, p)


#print(a)





#ScatterPlot
x = [257,264, 274, 266, 277, 263, 258, 275]
y = [100, 102, 103, 101, 105, 100, 99, 105]
z = [1,2,4,5,5,6,6,7]
df = pd.DataFrame({'x':x, 'x2':y, '3':z})
print(df)
print(pd.plotting.scatter.matrix(df))
print(np.corrcoef([x,y,z]))
