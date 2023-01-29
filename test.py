import sympy 
from sympy import *
import math
import probability_formulas
import test_2
import statistics

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
    data_set = test_2.Data()
    population_value = data_set.population
    x = input('x: ')
    x = float(x) 
    x = data_set.access_element(x)


    if population_value == True: 
        stdev = test_2.StdevP(data_set.data_set)
        stdev = float(stdev)

    elif population_value == False:
        stdev = test_2.StdevS(data_set.data_set)
        stdev = float(stdev)

    mean = test_2.Mean(data_set.data_set)
    mean = float(mean)

    self.z = (x - mean)/stdev

  def __float__ (self):
    return float(self.z)

answer = NormalDistribution()

answer = float(answer)

print (answer)

#class Mean (object):
 #   def __init__ (self, data_set):
  #      self.mean = statistics.mean(data_set)
    
   # def __float__ (self):
    #    return float(self.mean)
    



