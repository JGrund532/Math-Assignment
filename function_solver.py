import math
import matplotlib
import fractions
import matplotlib.pyplot as plt
import numpy as np
import tools.fraction_to_float

#choose function
MyOptions =["1 = sin","2 = cos", "3 = tan", "4 = sinh", "5 = cosh", "6 = tanh"] #list of functions

#prints the list of function options for the user to select on seperate rows
for x in MyOptions:
    print (x)      

#user inputs function                
funcSelection = input ("What is your mathematical function? ")     

#gives the user options 1 to 6 rather than 0 to 5 [list indexes start at 0]
funcSelection = int(funcSelection) - 1        

#input variables
myvariable = input ("what is your variable? ")

#allows fractions to be inputted by user. (To be saved in a seperate script and imported when needed)
tools.fraction_to_float

myvariable = tools.fraction_to_float.convert_to_float(myvariable)


#do something

#functions selected in the first part of the code
myfunctions = ["sin", "cos", "tan", "sinh", "cosh", "tanh"] 

 # getattr runs the math module to find the functions within it, and matches with the inputted function.
runMath = getattr(math, myfunctions[funcSelection])

# creates an object called answer which can then be called on to print
answer = runMath(myvariable) 

#return result and graph

# prints answer
print (answer) 
