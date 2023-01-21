import math
from sympy import *


#trigonometric functions

class Trigonometric:
    
        @staticmethod
        def sine (x):
            return sin (x*(pi/180))

        @staticmethod
        def cosine (x):
            return cos (x*(pi/180))

        @staticmethod
        def tangent(x): 
            return tan (x*(pi/180))

        @staticmethod
        def asin (x):
            return asin (x)

        @staticmethod
        def acos (x):
            return acos (x)

        @staticmethod
        def atan (x):
            return atan (x)


#hyperbolic functions 

class Hyperbolic:

        @staticmethod
        def sinh (x):
            return sinh(x)

        @staticmethod
        def cosh (x):
            return cosh(x)

        @staticmethod
        def tanh (x):
            return tanh(x)
        
        @staticmethod
        def asinh (x): 
            return asinh(x)

        @staticmethod
        def acosh (x): 
            return acosh(x)
        
        @staticmethod
        def atanh (x): 
            return atanh(x)



class Logarithmic: 

        @staticmethod
        def base10 (x):
            return log (x, 10)

        @staticmethod
        def natural (x):
            return log(x)

        @staticmethod
        def x_y (x, y):
            return log(x, y)
