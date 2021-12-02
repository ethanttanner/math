# Ethan Tanner 

from matplotlib import pyplot as plt
#import numpy as np
#import pandas as pd




def main():
#Data
    f0 = [ 1, 1, 5, 1, 1, 6, 4, 10, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 30, 1, 9 ]
    f1 = [ 16, 13, 9, 8, 13, 10, 15, 1, 17, 23, 10, 8, 12, 5, 20, 31, 12, 5, 30, 13, 7, 1, 5, 13, 1, 2, 5, 10, 1, 20, 5 ]
    f2 = [ 7, 15, 2, 10, 23, 10, 7, 12, 8, 1, 8, 19, 5, 10, 15, 20, 10, 13, 20, 15, 13, 14, 1, 4, 2, 15, 30, 91, 11, 5 ]
    f3 = [ 9, 20, 8, 16, 26, 36, 10, 20, 50, 17, 26, 31, 21, 30, 23, 28, 23, 18, 35, 35, 15, 25, 30, 15, 22, 18, 58, 19, 23, 31, 13, 26, 40, 14, 11 ]
    f4 = [ 120, 23, 23, 42, 47, 25, 22, 22, 34, 50, 38, 28, 39, 29, 28, 25, 34, 16, 40, 55, 124, 30, 30, 31 ]
    f5 = [ 37, 69, 23, 52, 61, 122 ]
        
#1
    fscaleLabels = ['F-0', 'F-1', 'F-2',
        'F-3', 'F-4', 'F-5']  
    # Creating plot
    #fig = plt.figure(figsize =(10, 6))
    plt.pie([len(f0), len(f1), len(f2), len(f3), len(f4), len(f5)], labels = fscaleLabels)
    plt.title('Number of tornados per f-scale')
    plt.show()
    
    # Most of the tornados were pretty quick, and the ones with the bigger f-scale cause more deaths.
    
#2??
    plt.hist(f0+f1+f2+f3+f4+f5) 
    plt.xlabel("Time(minutes)")
    plt.ylabel("# of Tornados")
    plt.title('Distribution of Tornado duration')
    plt.show()
#3?
    plt.hist(f0, color ="orange") 
    plt.xlabel("Time(minutes)")
    plt.ylabel("# of Tornados")
    plt.title('Distribution of Tornado duration')
    plt.show()
    
    plt.hist(f1, color="maroon") 
    plt.xlabel("Time(minutes)")
    plt.ylabel("# of Tornados")
    plt.title('Distribution of Tornado duration')
    plt.show()
    
    plt.hist(f2, color='black') 
    plt.xlabel("Time(minutes)")
    plt.ylabel("# of Tornados")
    plt.title('Distribution of Tornado duration')
    plt.show()
    
    plt.hist(f3, color='purple') 
    plt.xlabel("Time(minutes)")
    plt.ylabel("# of Tornados")
    plt.title('Distribution of Tornado duration')
    plt.show()
    
    plt.hist(f4, color='navy') 
    plt.xlabel("Time(minutes)")
    plt.ylabel("# of Tornados")
    plt.title('Distribution of Tornado duration')
    plt.show()
    
    plt.hist(f5, color='red') 
    plt.xlabel("Time(minutes)")
    plt.ylabel("# of Tornados")
    plt.title('Distribution of Tornado duration')
    plt.show()
  # Most of the distributions show most of them being shorter with just a few outliers.
  # But the higher intensity tornados had a higher distributions than the the lower fscale group.
#4      
    #fig = plt.figure(figsize = (10, 5))   
    # creating the bar plot
    plt.bar(fscaleLabels, [0, 0, 14, 32, 129, 130], color ='green',
            width = 0.4)
    plt.xlabel("Tornado Intensity")
    plt.ylabel("Number of Deaths")
    plt.title("Relationship between deaths and tornado intensity")
    plt.show()
    #Yes the f4 and f5 group account for 84% of the deaths.
    
#5
    #fig = plt.figure(figsize = (10, 5))   
    # creating the bar plot
    plt.bar(['Rural areas', 'Small communities', 'Small cities', 'Medium cities', 'Large cities'], [99, 77, 63, 56, 10], color ='maroon',
            width = 0.4)
    plt.xlabel("Community size")
    plt.ylabel("Number of Deaths")
    plt.title("Relationship between number of deaths and community size")
    plt.show()
    # The smaller and more rural areas from the data had more deaths where the bigger and medium cities had less.
    
#6
    #Most of the tornados that happened in oz were medium sized tornados and had shorter durations and caused less damage. The f4 and f3 scale tornados only make up for over 1% of the tornados but caused more than 70% of the deaths accross the communities.
    
    
    
    
    
    
    
    
    
    
    
    
    #ages = {}
    #df = pd.DataFrame(ages)
    #print(df)
    #file = "temp.py"
    #file.read_csv()
    
    
#    age = [44, 56, 51, 46, 59, 56, 58, 55, 65, 64, 68, 69, 56, 62, 62, 62, 50]
#
#   mean = 0
#   x = sorted(age)
#    for i in range( len(age)):
#        mean += age[i]
#        if (age[i] == age[i+1]):
#            mode = age[i]
#    
#    x = sorted(age)
#    mean = mean / len(age)
#    median = x[int(len(x)/2)]
#    
#    print("Mean: " , round(mean, 0))
#    print("Median: ", median)
#    print("Mode: ", median)
          
if __name__ == "__main__":
    main()