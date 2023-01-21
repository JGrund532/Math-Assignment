from sympy import *
from mpmath import *
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
                d = Integer(input ('Accuracy: '))
                answer = function_formulas.Trigonometric.sine(Float(θ))
                answer = answer.evalf(d)
                print ( "Sine of ",θ, "=", answer)
                break

            if selection == trig_options.index(1):
                θ = input ("Input angle ")
                d = Integer (input ('Accuracy: '))
                answer = function_formulas.Trigonometric.cosine(Float(θ))
                answer = answer.evalf(d)
                print ( "Cosine of ",θ, "=", answer)
                break

            if selection == trig_options.index(2):
                θ = input ("Input angle ")
                d = Integer (input ('Accuracy: '))
                answer = function_formulas.Trigonometric.tangent(Float(θ))
                answer = answer.evalf(d)
                print ( "Tangent of ",θ, "=", answer)
                break

            if selection == trig_options.index(3):
                x = input ("Input O/H ")
                d = Integer (input ('Accuracy: '))
                answer = function_formulas.Trigonometric.asin(x)
                answer = answer.evalf(d)
                mp.dps = d; mp.pretty = True
                answer = degrees(answer)  
                print (f"{theta} =",(answer))
                break

            if selection == trig_options.index(4):
                x = input("Input A/H ")
                d = Integer (input ('Accuracy: '))
                answer = function_formulas.Trigonometric.acos(x)
                answer = answer.evalf(d)
                mp.dps = d; mp.pretty = True
                answer = degrees(answer)  
                print (f"{theta} =",(answer))
                break

            if selection == trig_options.index(5):
                x = input("Input O/A ")
                d = Integer (input ('Accuracy: '))
                answer = function_formulas.Trigonometric.atan(Float(x))
                answer = answer.evalf(d)
                mp.dps = d; mp.pretty = True
                answer = degrees(answer)  
                print (f"{theta} =",(answer))
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
                d = Integer (input ('Accuracy: '))
                answer = function_formulas.Hyperbolic.sinh(Float(x))
                answer =answer.evalf(d)
                print ('y =', answer)
                break

            if selection == hyperbolic_options.index(1):
                print('Input x value ')
                x = input('x = ')
                d = Integer (input ('Accuracy: '))
                answer = function_formulas.Hyperbolic.cosh(Float(x))
                answer = answer.evalf(d)
                print ('y =', answer)
                break

            if selection == hyperbolic_options.index(2):
                print('Input x value ')
                x = input('x = ')
                d = Integer (input ('Accuracy: '))
                answer = function_formulas.Hyperbolic.tanh(x)
                answer = answer.evalf(d)
                print ('y =', answer)
                break




#inverse hyperbolic operators

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
                d = Integer (input ('Accuracy: '))
                answer = function_formulas.Hyperbolic.asinh(Float(x))
                answer = answer.evalf(d)
                print ('x =', answer)
                break

            if selection == hyperbolic_options.index(1):
                print('Input y value ')
                x = input('y = ')
                d = Integer (input ('Accuracy: '))
                answer = function_formulas.Hyperbolic.acosh(Float(x))
                answer = answer.evalf(d)
                print ('x =', answer)
                break

            if selection == hyperbolic_options.index(2):
                print('Input y value ')
                x = input('y = ')
                d = Integer (input ('Accuracy: '))
                answer = function_formulas.Hyperbolic.atanh(Float(x))
                answer = answer.evalf (d)
                print ('x =', answer)
                break



#logarthimic Operators 

class LogarithmicOperators:
    def __init__ (self):

        options = ['1 = base 10', '2 = natural', '3 = x y']
        for x in options:
            print (x)

        options[0:] = range (3)

        while attempt_count < attempt_limit:

            selection = int(input('Log type: '))
            selection = selection - 1

            if selection == options.index(0):
                x = Float(input('x = '))
                d = Integer(input('Accuracy: '))
                answer = function_formulas.Logarithmic.base10(x)
                answer = answer.evalf(d)
                print (answer)
                break

            if selection == options.index(1):
                x = Float(input('x = '))
                d = Integer(input('Accuracy: '))
                answer = function_formulas.Logarithmic.natural(x)
                answer = answer.evalf(d)
                print (answer)
                break

            if selection == options.index(2):
                x = input('b = ')
                y = input('x = ')
                d = Integer(input('Accuracy: '))
                answer = function_formulas.Logarithmic.x_y(y, x)
                answer = answer.evalf(d)
                print(answer)
                break