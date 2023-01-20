import math
import sympy
from sympy import *
from sympy import sin, cos, tan, asin, acos, atan
from sympy import sinh, cosh, tanh, asinh, acosh, atanh 


#trigonometric functions

class Trigonometric:
    
        @staticmethod
        def sine (x):
            return sin (x*(pi/180)) #need to updat to rest of functions
            #return math.sin(math.radians(x))

        @staticmethod
        def cosine (x):
            return math.cos(math.radians(x))

        @staticmethod
        def tangent(x): 
            return math.tan(math.radians(x))

        @staticmethod
        def asin (x):
            return math.asin(x)

        @staticmethod
        def acos (x):
            return math.acos(x)

        @staticmethod
        def atan (x):
            return math.atan(x)


#hyperbolic functions 

class Hyperbolic:

        @staticmethod
        def sinh (x):
            #return sin(x)
            return math.sinh(x)

        @staticmethod
        def cosh (x):
            return math.cosh (x)

        @staticmethod
        def tanh (x):
            return math.tanh(x)
        
        @staticmethod
        def asinh (x): 
            return math.asinh(x)

        @staticmethod
        def acosh (x): 
            return math.acosh(x)
        
        @staticmethod
        def atanh (x): 
            return math.atanh(x)



class Logarithmic: 

        @staticmethod
        def base10 (x):
            return 

        @staticmethod
        def natural (x):
            return
