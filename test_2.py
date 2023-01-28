import function_formulas
import sympy as sp
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from sympy.plotting import plot 


attempt_count = 0 
attempt_limit = float('inf')

class Exponential:
    def __init__ (self):

        print ('f(x) = a^x')
        print ('Type e for eulers')    
        a = str(4)
        x = 2
        d = 3

        while attempt_count < attempt_limit:

            if a.lower() == 'e':
                answer = function_formulas.exponential.natural_exponential(Float(x))
                answer = answer.evalf(d)
                print(answer)
                break

            if a.lower() != 'e':        
                answer = function_formulas.exponential.exponential(Float(a), Float(x))
                answer = answer.evalf(d)
                print (answer)
                break
Exponential()

