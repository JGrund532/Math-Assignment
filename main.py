import math
import matplotlib
import fractions
import matplotlib.pyplot as plt
import numpy as np
import statistics
import tools.fraction_to_float
import tools.list_maker



class FunctionOperators(object): 
    def __init__ (self):

    #choose function
        myOptions =["1 = sin","2 = cos", "3 = tan", "4 = sinh", "5 = cosh", "6 = tanh"] 

        for x in myOptions:
            print (x)     

        funcSelection = input ("What is your mathematical function? ")     

    #gives the user options 1 to 6 rather than 0 to 5 [list indexes start at 0]
        funcSelection = int(funcSelection) - 1


        myvariable = input ("what is your variable? ")

    #allows fractions to be inputted by user. (To be saved in a seperate script and imported when needed)
        tools.fraction_to_float

        myvariable = tools.fraction_to_float.convert_to_float(myvariable)



    #functions selected in the first part of the code
        myfunctions = ["sin", "cos", "tan", "sinh", "cosh", "tanh"] 

    #getattr runs the math module to find the functions within it, and matches with the inputted function and func selection
        runMath = getattr(math, myfunctions [funcSelection])

        print(runMath((myvariable))) 

 



#data class for running statistical functions 
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



#class AnswerLog (self):
#    def __init__ (self, answer_1, answer_2):
#        self.answer_1 = answer_1
#        self.answer_2 = answer_2




#initial user input 
my_options = ["1 = Calculate a function value", "2 = Statistical"]

for x in my_options:
    print(x)

option_selection = input("what are you trying to do? ")

if int(option_selection) == 1: 
    FunctionOperators()
   


if int(option_selection) == 2:
    Data()


