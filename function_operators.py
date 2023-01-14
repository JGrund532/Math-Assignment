import math
import matplotlib
import fractions
import matplotlib.pyplot as plt
import numpy as np
import tools.fraction_to_float

#trigonometric functiona
class TrigonometricOperators:
    
        @staticmethod
        def sine (x):
            return math.sin(math.radians(x))

        @staticmethod
        def cosine (x):
            return math.cos(math.radians(x))

        @staticmethod
        def tangent(x): 
            return math.tan(math.radians(x))

        @staticmethod
        def asine (x):
            return math.asin(x)

        @staticmethod
        def acosine(x):
            return math.acos(x)

        @staticmethod
        def atangent(x):
            return math.atan(x)


#hyperbolic functions 
class HyperbolicOperators:

        @staticmethod
        def sinh (x):
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


x = float(input ("enter known angle "))

x = tools.fraction_to_float.convert_to_float(x)

calc = input ()





