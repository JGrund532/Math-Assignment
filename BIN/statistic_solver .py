import math 
import statistics
import tools.fraction_to_float

class Data (object):
    def __init__ (self): 
    
        selections = ["1 = population", "2 = sample"] 

        for x in selections:
            print (x)

    #Is the data set a sample of a larger data set or there whole population? (needed for stadard deviation)
        mySelection = input ("Population or sample? ") 
    
    #user input data set 
        data_set = []
        n = int(input("Enter the population size "))

        print("\n") #Uses n variable to accept data n amount of times 
        for i in range(0, n): #starts a for loop with n amount of rows 
            print("Enter Sample ", i + 1 , )
            item = float(input()) #user input 
            data_set.append(item) #appends the list after each input 
        
        print("Data set: ", data_set)

        print("mean: " + str(statistics.mean (data_set)))

        print ("Range: " + str(max(data_set) - min(data_set)))

        print("Median: " + str(statistics.median(data_set)))
        
        print("Mode: " + str(statistics.mode(data_set)))






Data()

