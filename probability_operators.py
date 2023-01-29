import sympy 
from sympy import *
import math
import probability_formulas
import test_2
import statistics_operator


class BinomialExpander (object):
    def __init__ (self):

        q, p, n = symbols('q p n')

        p = input ('Success (p): ')
        print (f"{p}","%")        
        p = Float(p)/100

        q = 1 - p
        print ('Failure (q) = ', q)
        q = Float(q)

        print("sample size: ")
        n = Integer(input('n: '))

    #while loop to allow multiple attempts to re-evaluate w/ different values of r when r < n 
        while True:
              
          print('Permutation value:')
          r = Integer(input('r: '))

          expansion = probability_formulas.formulas.binomial_expansion(q, p, n)            
          expansion = str(expansion)
          print (expansion)
          expansion = expansion.split('+')

          expansion = expansion[((int(r)*-1)-1)]
          print (f'{expansion} = ', eval(expansion))


       #breaks while loop if user no longer needs       
          print("Revalue r? Type N to cancel, Y to go again")
          go_again = input('')
          if go_again.upper() == 'N':
            break



class NormalDistribution (object):
    def __init__ (self):
      data_set = statistics_operator.Data()
      population_value = data_set.population
      x = float(input('x: ')) 
      x = data_set.access_element(x)


      if population_value == True: 
          stdev = statistics_operator.StdevP(data_set.data_set)
          stdev = float(stdev)

      elif population_value == False:
          stdev = statistics_operator.StdevS(data_set.data_set)
          stdev = float(stdev)

      mean = statistics_operator.Mean(data_set.data_set)
      mean = float(mean)

      self.z = (x - mean)/stdev


    def __float__ (self):
      return float(self.z)

answer = NormalDistribution()

print (float(answer))