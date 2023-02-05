from sympy import *
import math
import probability_formulas
import statistics_operator as so 
import scipy as stats 

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
          answer = f'{expansion} = {eval(expansion)}'
          print (answer)
          self.answer = answer

       #breaks while loop if user no longer needs       
          print("Re-evaluate r? Y/N")
          go_again = input('')
          if go_again.upper() == 'N':
            break



class NormalDistribution (object):
    def __init__ (self):
      data_set = so.DataContinuous()
      population_value = data_set.population
      x = float(input('x: ')) 


      if population_value == True: 
          stdev = so.StdevP(data_set.data_set)
          stdev = float(stdev)

      elif population_value == False:
          stdev = so.StdevS(data_set.data_set)
          stdev = float(stdev)

      mean = so.Mean(data_set.data_set)
      mean = float(mean)

      self.stdev = stdev 
      self.mean = mean
      self.z = (x - mean)/stdev
      self.x = x


    def __float__ (self):
      return float(self.z)