import math
import matplotlib
import fractions
import matplotlib.pyplot as plt
import numpy as np
import tools.fraction_to_float

#trigonometric functions
class TrigonometricOperators:
    
        @staticmethod
        def sine (x):
            return math.sin(math.radians(x))

        @staticmethod
        def cosine (x):
            return math.cos(math.radians(x))

        @staticmethod
        def tangent(x): 
            return math.tan(math.radians(x))

        @staticmethod
        def asin (x):
            return math.asin(x)

        @staticmethod
        def acosin (x):
            return math.acos(x)

        @staticmethod
        def atan (x):
            return math.atan(x)


#hyperbolic functions 
class HyperbolicOperators:

        @staticmethod
        def sinh (x):
            return math.sinh(x)

        @staticmethod
        def cosh (x):
            return math.cosh (x)

        @staticmethod
        def tanh (x):
            return math.tanh(x)
        
        @staticmethod
        def asinh (x): 
            return math.asinh(x)

        @staticmethod
        def acosh (x): 
            return math.acosh(x)
        
        @staticmethod
        def atanh (x): 
            return math.atanh(x)


attempt_limit = float("inf")
attempt_count = 0

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

        if try_again == options.index(0):
            break  

        if try_again == options.index(1): 
            break

        if try_again == options.index(2): 
            break

        if try_again == options.index(3): 
            break



def take_second (element):
    return element [1]

def take_third (element):
    return element[2]

def take_fourth (element):
    return element [3]

def take_fifth (element):
    return element [4]

def take_sixth (element):
    return element [5]


if func_select or try_again == options.index(0):
    operator()

    class operator (object):
        def __init__ (self):
    
        trig_options = ["1 = Sine", "2 = Cosine", "3 = Tangent", "4 = sin -1", "5 = cos -1", "6 = tan -1"]
        for functions in trig_options:
            print (functions)

        trig_options[0:] = range(5)

        while attempt_count < attempt_limit:
            selection = int(input ("Select trig function "))
            if selection == trig_options.index(0):
                TrigonometricOperators.sine(x)
                break
            
            trig_options.sort(key = take_second)
            if selection == trig_options.index(0):
                TrigonometricOperators.cosine(x)
                break

    


    



#def takeSecond(elem): 
 #   return elem[1] 

# random list
#random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
#random.sort(key=takeSecond)

# print list
#print('Sorted list:', random)

