import math 
import probability_formulas
import sympy 
from sympy import *

attempt_limit = float("inf")
attempt_count = 0
init_printing(use_unicode=True)


class ProbabilityOperator (object):
    def __init__ (self):

        q, p, n = symbols('q p n')

        p = input ("Pecentage of faulty parts: " )

        print (f"{p}","%")
        
        p = float(p)/100

        q = 1 - p

        n = Integer(input("sample size: "))

        r = Integer(input("Amount of defect parts you're looking for: "))

#calculating binomial termcoefficients
        binom_coef = probability_formulas.formulas.combination(n, r)

        expansion = probability_formulas.formulas.binomial_expansion(q, p, n)
      
        expansion = str(expansion)

        expansion = expansion.split("+")

        expansion = expansion[((int(r)*-1))-1]

        print(expansion)

        expansion = str(expansion)

        expansion = eval(expansion)

        print(expansion)

        print("Reavlue r? Type N to cancel")

        go_again = input ("r: ") 
        if go_again == "N":
          break

ProbabilityOperator()