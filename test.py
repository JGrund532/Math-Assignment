import math 
import probability_formulas
import sympy 
from sympy import *

attempt_limit = float("inf")
attempt_count = 0


class ProbabilityOperator (object):
    def __init__ (self):

        #@classmethod
        #def binom_calc(bpc):
        q, p, n = symbols('q p n')

        print("Pecentage of faulty parts: ")
        p = input ('p: ')

        print (f"{p}","%")
          
        p = float(p)/100

        q = 1 - p
        print ('q = ', q)

        print("sample size: ")
        n = Integer(input('n: '))

    #while loop to allow multiple attempts changing the value of r 
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
          if go_again == 'N':
            break


ProbabilityOperator()