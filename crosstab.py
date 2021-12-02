import pandas as pd

x = {'Company':['Ford', 'Chevy', 'Ford', 'Ford', 'Ford', 'Toyota'], 
'Model':['Mustang', 'Camaro', 'Fiesta', 'Focus', 'Taurus', 'Camry'],
'Rating': ['A', 'B', 'C', 'A', 'B', 'B'],
'Type': ['Coupe', 'Coupe', 'Sedan', 'Sedan', 'Sedan', 'Sedan']}

cars = pd.DataFrame(x)
con_table = pd.crosstab(cars.Company, cars.Rating, margins=True, normalize='index')
print(con_table)

con_table7 = pd.crosstab(cars.Rating, cars.Type, margins=True, normalize='index')
print(con_table7)

print("\nFind the marginal probabilities of the different ratings:")
print("A: 0.333333  B: 0.50  C: 0.166667\n")
print("\nAlso find out the conditional probabilities of different type of cars given different ratings of the car:")
print("Coupe: 0.333333  Sedan: 0.666667\n\n\n")






data = pd.read_csv('heart.csv')
df = pd.DataFrame(data)
#con_table1 = pd.crosstab(df.sex, df.fbs, margins=True, normalize='index')
#print(con_table1)

con_table2 = pd.crosstab(df.sex, df.fbs, margins=True, normalize='index')
print(con_table2)

#4
con_table3 = pd.crosstab(df.sex, df.chol.between(200,239), margins=True, normalize='index')
print(con_table3)
#v
con_table4 = pd.crosstab(df.age > 60, df.trestbps > 140, margins = True, normalize='index')
print(con_table4)

#1
#0.159420
#2
#0.125
#3
#0.3575
#4
#0.25
#5
#0.3544

print("\ni.    Find the probability of a patient having fasting sugar level > 120 mg/l given that the patient is a male.")
print("    0.159420\n")

print("ii.    Find the probability of a patient having fasting sugar level > 120 mg/l given that the patient is a female.")
print("    0.125\n")

print("iii.    Find the probability of a patient having serum level 200 – 239 (moderately elevated) given that the patient is male?")
print("    0.357488\n")

print("iv.    Find the probability of a patient having serum level 200 – 239 (moderately elevated) given that the patient is female?")
print("    0.250000\n")

print("v.    P (hypertension | older than 60) = ")
print("    0.354430")







