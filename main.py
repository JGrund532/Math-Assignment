import math
import matplotlib
import fractions
import matplotlib.pyplot as plt
import numpy as np
import statistics_output
import tools.fraction_to_float
import function_formulas
import sys
import statistics
import sympy
from sympy import *
import probability_formulas


def take_second(elem):
    return elem[1]

def take_third(elem):
    return elem[2]

def take_fourth(elem):
    return elem[3]



#attempt limit used when initiating while loops throughout code

attempt_limit = float("inf")
attempt_count = 0




#operator to run trig options form function opertors module 

class TrigOperator(object): 
    def __init__ (self):
        
        theta = "θ" 

        trig_options = ["1 = sine", "2 = cosine", "3 = tangent", "4 = sin -1", "5 = cos -1", "6 = tan -1"]
        for functions in trig_options:
            print (functions)

        trig_options[0:] = range(6)

        while attempt_count < attempt_limit:
            selection = int(input ("Select trig function "))
            selection = selection -1 
           
           
            if selection == trig_options.index(0):
                θ = input ("Input angle ")
                θ = tools.fraction_to_float.convert_to_float(θ)
                answer = function_formulas.TrigonometricOperators.sine(float(θ))
                print ( "Sine of ",θ, "=", answer)
                break

            if selection == trig_options.index(1):
                θ = input ("Input angle ")
                θ = tools.fraction_to_float.convert_to_float(θ)
                answer = function_formulas.TrigonometricOperators.cosine(float(θ))
                print ( "Sine of ",θ, "=", answer)
                break

            if selection == trig_options.index(2):
                θ = input ("Input angle ")
                θ = tools.fraction_to_float.convert_to_float(θ)
                answer = function_formulas.TrigonometricOperators.tangent(float(θ))
                print ( "Sine of ",θ, "=", answer)
                break

            if selection == trig_options.index(3):
                x = input("Input O/H ")
                x = tools.fraction_to_float.convert_to_float(x)
                answer = function_formulas.TrigonometricOperators.asin(x)
                print (f"{theta} =", math.degrees(answer))
                break

            if selection == trig_options.index(4):
                x = input("Input A/H ")
                x = tools.fraction_to_float.convert_to_float(x)
                answer = function_formulas.TrigonometricOperators.acos(x)
                print (f"{theta} =", math.degrees(answer))
                break

            if selection == trig_options.index(5):
                x = input("Input O/A ")
                x = tools.fraction_to_float.convert_to_float(x)
                answer = function_formulas.TrigonometricOperators.atan(x)
                print (f"{theta} =", math.degrees(answer))
                break










#operator to run hyoerbolic functions 

class HyperbolicOperator:
    def __init__ (self):

        hyperbolic_options = ["1 = sinh", "2 = cosh", "3 = tanh", "4 = sinh -1", "5 = cosh -1", "6 = tanh -1"]
        for functions in hyperbolic_options:
            print (functions)

        hyperbolic_options[0:] = range(6)

        while attempt_count < attempt_limit:
            selection = int(input ("Select hyperbolic function "))
            selection = selection -1 
          
            if selection == hyperbolic_options.index(0):
                answer = function_formulas.HyperbolicOperators.sinh(x)
                print (answer)
                break

            if selection == hyperbolic_options.index(1):
                answer = function_formulas.HyperbolicOperators.cosh(x)
                print (answer)
                break

            if selection == hyperbolic_options.index(2):
                answer = function_formulas.HyperbolicOperators.tanh(x)
                print (answer)
                break

            if selection == hyperbolic_options.index(3):
                answer = function_formulas.HyperbolicOperators.asinh(x)
                print (answer)
                break

            if selection == hyperbolic_options.index(4):
                answer = function_formulas.HyperbolicOperators.cosh(x)
                print (answer)
                break

            if selection == hyperbolic_options.index(5):
                answer = function_formulas.HyperbolicOperators.tanh(x)
                print (answer)
                break










class ProbabilityOperator (object):
    def __init__ (self):

        q, p, n = symbols('q p n')

        print("Pecentage of faulty parts: ")
        p = input ('p: ')
        print (f"{p}","%")        
        p = Float(p)/100

        q = 1 - p
        print ('q = ', q)
        q = Float(q)

        print("sample size: ")
        n = Integer(input('n: '))


    #while loop to allow multiple attempts to re-evaluate w/ different values of r when r < n 
        while attempt_count < attempt_limit:
              
          print('Permutation value:')
          r = Integer(input('r: '))

          expansion = probability_formulas.formulas.binomial_expansion(q, p, n)            
          expansion = str(expansion)
          print (expansion)
          expansion = expansion.split('+')

          expansion = expansion[((int(r)*-1)-1)]
          print (expansion, '=')
          expansion = eval(expansion)
          print(expansion)

       #breaks while loop if user no longer needs       
          print("Revalue r? Type N to cancel, Y to go again")
          go_again = input('')
          if go_again.upper() == 'N':
            break




#        data_set_selection = ["Do you have a data set?", "1 = Yes", "2 = No"]
 #       for x in data_set: 
  #          print (x)

   #     data_set_selection[0:] = range (3)

    #    selection = int(input(""))

     #   selection = selection - 1










#class AnswerLog (self):
#    def __init__ (self, answer_1, answer_2):
#        self.answer_1 = answer_1
#        self.answer_2 = answer_2










#                           _________________________________________________________________________________________________________                        
#initial user input for main_________________________________________________________________________________________________________ 




my_options = ["1 = Function Tool", "2 = Statistic Tool", "3 = Probability Tool", "4 = Arithmetic", "5 = Equation Solver"]

for x in my_options:
    print(x)

option_selection = int(input("what are you trying to do? "))

my_options[:0] = range(5)

option_selection = option_selection - 1

#input function catagory 

if int(option_selection) == my_options.index(0):

 
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











if int(option_selection) == my_options.index(1):
    statistics_output.Data()








#if user selects probabilty tool 

if int(option_selection) == my_options.index(2): 
    
    #options = ['1 = Binomial distribution ']
    ProbabilityOperator()
