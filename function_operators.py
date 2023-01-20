import math 
import sympy 
from sympy import *
import tools.fraction_to_float
import function_formulas

attempt_count = 0
attempt_limit = float('inf')



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
                d = Integer(input ('Accuracy(dcml places): '))#need to updst to other functions
                θ = tools.fraction_to_float.convert_to_float(θ)
                answer = function_formulas.Trigonometric.sine(Float(θ))
                answer = answer.evalf(d)
                print ( "Sine of ",θ, "=", answer)
                break

            if selection == trig_options.index(1):
                θ = input ("Input angle ")
                θ = tools.fraction_to_float.convert_to_float(θ)
                answer = function_formulas.Trigonometric.cosine(float(θ))
                print ( "Sine of ",θ, "=", answer)
                break

            if selection == trig_options.index(2):
                θ = input ("Input angle ")
                θ = tools.fraction_to_float.convert_to_float(θ)
                answer = function_formulas.Trigonometric.tangent(float(θ))
                print ( "Sine of ",θ, "=", answer)
                break

            if selection == trig_options.index(3):
                x = input("Input O/H ")
                x = tools.fraction_to_float.convert_to_float(x)
                answer = function_formulas.Trigonometric.asin(x)
                print (f"{theta} =", math.degrees(answer))
                break

            if selection == trig_options.index(4):
                x = input("Input A/H ")
                x = tools.fraction_to_float.convert_to_float(x)
                answer = function_formulas.Trigonometric.acos(x)
                print (f"{theta} =", math.degrees(answer))
                break

            if selection == trig_options.index(5):
                x = input("Input O/A ")
                x = tools.fraction_to_float.convert_to_float(x)
                answer = function_formulas.Trigonometric.atan(x)
                print (f"{theta} =", math.degrees(answer))
                break


#operator to run hyoerbolic functions 

class HyperbolicOperator:
    def __init__ (self):

        hyperbolic_options = ["1 = sinh", "2 = cosh", "3 = tanh"]
        for functions in hyperbolic_options:
            print (functions)

        hyperbolic_options[0:] = range(6)

        while attempt_count < attempt_limit:
            selection = int(input ("Select hyperbolic function "))
            selection = selection -1 
          
            if selection == hyperbolic_options.index(0):
                print('Input x value ')
                x = input('x = ')
                x = tools.fraction_to_float.convert_to_float(x)
                answer = function_formulas.Hyperbolic.sinh(x)
                print ('y =', answer)
                break

            if selection == hyperbolic_options.index(1):
                print('Input x value ')
                x = input('x = ')
                x = tools.fraction_to_float.convert_to_float(x)
                answer = function_formulas.Hyperbolic.cosh(x)
                print ('y =', answer)
                break

            if selection == hyperbolic_options.index(2):
                print('Input x value ')
                x = input('x = ')
                x = tools.fraction_to_float.convert_to_float(x)
                answer = function_formulas.Hyperbolic.tanh(x)
                print ('y =', answer)
                break





class InverseHyperbolic:
    def __init__ (self):

        hyperbolic_options =  ["1 = sinh -1", "2 = cosh -1", '3 = tanh -1']
        for x in hyperbolic_options:
            print (x)

        hyperbolic_options = range(3)

        while attempt_count < attempt_limit:
            selection = int(input ('Select inverse hyperbolic function: '))
            selection = selection - 1

            if selection == hyperbolic_options.index(0):
                print('Input y value ')
                x = input('y = ')
                x = tools.fraction_to_float.convert_to_float(x)
                answer = function_formulas.Hyperbolic.asinh(x)
                print ('x =', answer)
                break

            if selection == hyperbolic_options.index(1):
                print('Input y value ')
                x = input('y = ')
                x = tools.fraction_to_float.convert_to_float(x)
                answer = function_formulas.Hyperbolic.cosh(x)
                print ('x =', answer)
                break

            if selection == hyperbolic_options.index(2):
                print('Input y value ')
                x = input('y = ')
                x = tools.fraction_to_float.convert_to_float(x)
                answer = function_formulas.Hyperbolic.tanh(x)
                print ('x =', answer)
                break




#class LogarithmicOperators (self):
 #   def __init__ (self):
