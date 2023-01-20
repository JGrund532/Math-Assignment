import math
import sympy 
from sympy import *
import probability_formulas



class ProbabilityOperator (object):
    def __init__ (self):

        q, p, n = symbols('q p n')

        print("Pecentage of faulty parts: ")
        p = input ('p: ')
        print (f"{p}","%")
          
        p = float(p)/100
        Float(p)

        q = 1 - p
        print ('q = ', q)
        Float(q)

        print("sample size: ")
        n = Integer(input('n: '))

        probability_formulas.formulas.binom_expand_calc(q, p, n)

ProbabilityOperator()


