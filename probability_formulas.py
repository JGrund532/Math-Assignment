import math
import matplotlib
import fractions
import numpy as np
import function_formulas
import sympy
from sympy import *

attempt_count = 0
attempt_limit = float('inf')


class formulas (object):

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


