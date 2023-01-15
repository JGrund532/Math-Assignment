import math
import matplotlib
import fractions
import matplotlib.pyplot as plt
import numpy as np
import statistics
import tools.fraction_to_float
import function_operators
import sys





def take_second(elem):
    return elem[1]

def take_third(elem):
    return elem[2]

def take_fourth(elem):
    return elem[3]





attempt_limit = float("inf")
attempt_count = 0




#operator to run trig options form function opertors module 

class TrigOperator(object): 
    def __init__ (self):
        
        theta = "θ"

        trig_options = ["1 = Sine", "2 = Cosine", "3 = Tangent", "4 = sin -1", "5 = cos -1", "6 = tan -1"]
        for functions in trig_options:
            print (functions)

        trig_options[0:] = range(6)

        while attempt_count < attempt_limit:
            selection = int(input ("Select trig function "))
            selection = selection -1 
           
           
            if selection == trig_options.index(0):
                θ = input ("Input angle ")
                answer = function_operators.TrigonometricOperators.sine(float(θ))
                print ( "Sine of ",θ, "=", answer)
                break

            if selection == trig_options.index(1):
                θ = input ("Input angle ")
                answer = function_operators.TrigonometricOperators.cosine(float(θ))
                print ( "Sine of ",θ, "=", answer)
                break

            if selection == trig_options.index(2):
                θ = input ("Input angle ")
                answer = function_operators.TrigonometricOperators.tangent(float(θ))
                print ( "Sine of ",θ, "=", answer)
                break

            if selection == trig_options.index(3):
                x = float(input("Input O/H "))
                answer = function_operators.TrigonometricOperators.asin(x)
                print (f"{theta} =", answer)
                break

            if selection == trig_options.index(4):
                x = float(input("Input A/H "))
                answer = function_operators.TrigonometricOperators.acos(x)
                print (f"{theta} =", answer)
                break

            if selection == trig_options.index(5):
                x = float(input("Input O/A "))
                answer = function_operators.TrigonometricOperators.atan(x)
                print (f"{theta} =", answer)
                break










#operator to run hyoerbolic functions 

class HyperbolicOperator:
    def __init__ (self):

        hyperbolic_options = ["1 = Sinh", "2 = Cosh", "3 = Tanh", "4 = sinh -1", "5 = cosh -1", "6 = tanh -1"]
        for functions in hyperbolic_options:
            print (functions)

        hyperbolic_options[0:] = range(6)

        while attempt_count < attempt_limit:
            selection = int(input ("Select hyperbolic function "))
            selection = selection -1 
          
            if selection == hyperbolic_options.index(0):
                answer = function_operators.HyperbolicOperators.sinh(x)
                print (answer)
                break

            if selection == hyperbolic_options.index(0):
                answer = function_operators.HyperbolicOperators.cosh(x)
                print (answer)
                break

            if selection == hyperbolic_options.index(0):
                answer = function_operators.HyperbolicOperators.tanh(x)
                print (answer)
                break

            if selection == hyperbolic_options.index(0):
                answer = function_operators.HyperbolicOperators.asinh(x)
                print (answer)
                break

            if selection == hyperbolic_options.index(0):
                answer = function_operators.HyperbolicOperators.cosh(x)
                print (answer)
                break

            if selection == hyperbolic_options.index(0):
                answer = function_operators.HyperbolicOperators.tanh(x)
                print (answer)
                break




 





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



#input function catagory 
 
    options = ["1 = Trigonometric", "2 = Hyperbolic", "3 = Logarithmic", "4 = Exponential"]

    for x in options: 
        print (x) 

    #converting option list elements to numbers for reference in input and while loop.  
    options[0:] = range(4)

    #user input 
    func_select = int(input("what is your function type?" ))

    func_select = func_select - 1 

    #while loop triggers if user input is invalid 
    if func_select > 3:
        while attempt_count < attempt_limit:
            try_again = int(input ("error, enter a number 1 to 4 to select. What is your function? "))

            try_again = try_again - 1

            if try_again == options.index(0):
                TrigOperator()
                break  

            if try_again == options.index(1):
                HyperbolicOperator()
                break

            if try_again == options.index(2): 
                break

            if try_again == options.index(3): 
                break
        

#user inputs correctly first time operator triggers
    if func_select == options.index(0):
        TrigOperator()

    if func_select == options.index(1):
        HyperbolicOperator()



if int(option_selection) == 2:
    Data()


