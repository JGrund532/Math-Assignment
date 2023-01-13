import math
import matplotlib
import fractions
import matplotlib.pyplot as plt
import numpy as np
import statistics
import tools.fraction_to_float



class function_operators(object): 
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

        print(runMath(myvariable)) 

 



#data class for running statistical functions 
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
    function_operators()
   


if int(option_selection) == 2:
    Data()


