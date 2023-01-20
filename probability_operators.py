import sympy 
from sympy import *
import math
import probability_formulas

attempt_count = 0
attempt_limit = float('inf')

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

