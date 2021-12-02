#(a) Go to a real estate Web site such as www.realtor.com or www.zillow.com and enter the particular zip code you are interested in moving to. Randomly select at least 30 homes for sale and record the following information:
 #   •    • Asking price
  #  •    • Square footage
   # •    • Number of days on the market
    #•    • Cost per square foot (asking price divided by square footage)


askingPrice = [365000, 472500, 2499900, 899900, 254900, 619000, 465000, 360000, 219900, 445000, 333000, 580000, 560875, 500000, 349000, 269900, 215000, 175000, 630000, 450000, 349000, 450000, 349000, 450000, 695000, 449000, 349900, 319900, 449000, 339900]
squareFootage = [1440, 1516, 3920, 4250, 1120, 3049, 1716, 784, 2240, 1256, 1443, 2096, 1815, 1912, 1667, 1100, 936, 1248, 2305, 1970, 1667, 2109, 1667, 2109, 2202, 2020, 1378, 1443, 1779, 2082]
numDaysOnMarket = [1, 1, 5, 26, 2, 4, 35, 15, 1, 3, 11, 16, 5, 2, 19, 5, 12, 35, 35, 13, 19, 2, 19, 2, 33, 8, 30, 35, 7, 35]
costPerSquareFood = [253, 312, 638, 212, 228, 203, 258, 210, 280, 354, 212, 227, 309, 262, 209, 425, 229, 140, 273, 228, 209, 213, 209, 213, 316, 222, 254, 222, 252, 192]

print(len(askingPrice), len(squareFootage), len(numDaysOnMarket), len(costPerSquareFood))


#(b) For each of the variables identified, determine a 95% confidence interval. Interpret the interval.

#(c) Now randomly select 30 recently sold homes and determine the percentage discount from the asking price. This is determined by computing asking

#(d) Determine a 95% confidence interval for percentage discount. Interpret the interval.

#(e) For the type of house you are considering (such as a 2400 square foot 3-bedroom/2-bath home), identify at least 20 homes that are for sale in the neighborhood you are considering. Compute a 95% confidence interval for the asking price of this type of home.

#(f) Write a report that details how much you should expect to pay for the type of house you are considering.
