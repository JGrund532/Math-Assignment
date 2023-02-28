import math
import numpy as np
import sympy
from sympy import *

class Formulas (object):

        @staticmethod 
        def permutation_rep(x, r):
            return math.perm(x, r)

        @staticmethod
        def permutation_no_rep(x, r):
            return math.pow (x, r)

        @staticmethod
        def combination(n, r):
            return math.comb(n, r)

        @staticmethod
        def binomial_expansion(q, p, n):
            q, p = sympy.symbols ("q p")
            formula = (q + p)**n
            return formula.expand()
        

#statistics probability formulas 
        @staticmethod
        def z_score (x, mean, stdev):
             formula = (x - mean)/stdev 
             return formula 

        @staticmethod 
        def significance_level (mu, x_bar, np, n, s):
             numerator = x_bar - mu 
             denominator_l = s/(math.sqrt(n))
             denominator_r = math.sqrt((np-n)/(np-1))
             formula = numerator/(denominator_l * denominator_r)
             return formula
        
