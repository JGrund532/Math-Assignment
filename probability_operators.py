from sympy import *
import math
import probability_formulas as pf
import statistics_operator as so  
import scipy.stats as stats

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

          expansion = pf.Formulas.binomial_expansion(q, p, n)            
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

    def discrete (self, frequency, mean, midpoints, stdev):

        stdev = float(stdev)
        mean = float(mean)
        print(mean)
        print(stdev)
        x = float(input('x value: '))
        z = pf.Formulas.z_score(x, mean, stdev)

        self.z = z
        self.x = x
        self.mean = mean 









class Significance:
    def __init__(self):
        self.alpha = None
        self.tail = None

#acquire alpha value 
    def get_significance(self):
        self.alpha = float(input('Enter the significance level (\u03B1): '))
       
        if self.alpha <= 0 or self.alpha >= 1:
            raise ValueError('Invalid value for alpha: must be between 0 and 1')

        print('Select the tail option:')
        print('1 = Single')
        print('2 = Double')
        self.tail = int(input())

        if self.tail not in [1, 2]:
            raise ValueError('Invalid value for tail: must be 1 or 2')

#calculate the z score of alpha ready for comparison 
    def calcz_alpha(self):
        if self.alpha is None or self.tail is None:
            raise ValueError('Call get significance first to set alpha and tail')
        
        if self.tail == 1:
            self.z_alpha = stats.norm.ppf(1 - self.alpha)
        
        elif self.tail == 2:
            self.z_alpha = stats.norm.ppf(1 - self.alpha/2)

#method to run if all required data is known 
    def answer(self, mu, x_bar, pop_size, sample_size, stdev):
        
        if self.alpha is None or self.tail is None:
            raise ValueError('Call get_user_input first to set alpha and tail')
        self.answer = pf.Formulas.significance_level(mu, x_bar, pop_size, sample_size, stdev)



            

