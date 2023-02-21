from sympy import *
import math
import probability_formulas as pf
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

          expansion = pf.formulas.binomial_expansion(q, p, n)            
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



class NormalDistribution ():
    def __init__ (self, population_value):
      self.population_value = population_value

    def discrete (self, frequency, mean, midpoints):


    #calculating STDEV via variance dependant on population value of sample or population
        if self.population_value == True:
            variance = sum(frequency[i] * (midpoints[i] - mean) ** 2 for i in range(len(midpoints))) / sum(frequency)
            stdev = math.sqrt(variance)

        if self.population_value == False: 
            variance = sum(frequency[i] * (midpoints[i] - mean) ** 2 for i in range(len(midpoints))) / sum(frequency) - 1
            stdev = math.sqrt(variance)

        stdev = float(stdev)
        mean = float(mean)
        print(mean)
        print(stdev)
        x = float(input('x value: '))
        z = pf.formulas.z_score(x, mean, stdev)

        self.z = z
        self.x = x
        self.mean = mean 

    