import math 
import sympy 
import probability_formulas


class ProbabilityOperator ():
        def __init__ (self):

                
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