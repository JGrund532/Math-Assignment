import math
from sympy import *
from sympy import sin, cos, tan, asin, acos, atan
from sympy import sinh, cosh, tanh, asinh, acosh, atanh 


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
            return 

        @staticmethod
        def natural (x):
            return
