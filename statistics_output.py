import statistics
import tools.fraction_to_float
import function_operators
import math 


class Data (object):
    def __init__ (self): 
    
        attempt_limit = float("inf")
        attempt_count = 0

    #selecting data set type for standard devaition
        selections = ["1 = population", "2 = sample"] 

        for x in selections:
            print (x)

    #changing index elements to 1 and 2 to break the while loop that only allows correct input 
        selections[0] = 1
        selections[1] = 2

        while attempt_count < attempt_limit: 
            sample_type = int(input ("Population or sample? "))
            sample_type = sample_type - 1
            attempt_count += 1

            if sample_type == selections.index(1):
                break

            if sample_type == selections.index(2):
                break
            

    #user input data set, see tools.list_maker for how it works   
        data_set = []
        n = int(input("Enter the population size "))

        print("\n")  
        for i in range(0, n): 
            print("Enter element ", i + 1 , )
            item = float(input()) #user input  
            data_set.append(item) 
        
        print("Data set: ", data_set)

        print("mean: " + str(statistics.mean (data_set)))

        print ("Range: " + str(max(data_set) - min(data_set)))

        print("Median: " + str(statistics.median(data_set)))
        
        print("Mode: " + str(statistics.mode(data_set)))

    #standard deviation functions for both data set types 
        if sample_type == 0: 
            
            print ("Standard deviation(P):" + str(statistics.pstdev(data_set)))

            print ("Variance (P):" + str(statistics.pvariance(data_set)))

        elif sample_type == 1:

            print ("standard deviation (S):" + str(statistics.stdev(data_set)))

            print ("Variance(S): " + str(statistics.variance(data_set)))