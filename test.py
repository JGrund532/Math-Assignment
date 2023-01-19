import math 
import probability_formulas
import sympy 
from sympy import *

attempt_limit = float("inf")
attempt_count = 0


class ProbabilityOperator (object):
    def __init__ (self):

        q, p, n = symbols('q p n')


        print("Pecentage of faulty parts: ")
        p = input ('p: ')

        print (f"{p}","%")
        
        p = float(p)/100

        q = 1 - p
        print ('q = ', q)

        print("sample size: ")
        n = Integer(input('n: '))

        while attempt_count < attempt_limit:
            
          print('Permutation value:')
          r = Integer(input('r: '))

          expansion = probability_formulas.formulas.binomial_expansion(q, p, n)
          
          expansion = str(expansion)

          print (expansion)

          expansion = expansion.split('+')

          expansion = expansion[((int(r)*-1))-1]

          print (expansion, '=')

          expansion = eval(expansion)

          print(expansion)
            
          print("Reavlue r? Type N to cancel")



ProbabilityOperator()