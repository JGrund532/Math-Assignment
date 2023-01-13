import math 


class function_operators:
    
        @staticmethod
        def sine (x):
            return math.sin(x)

        @staticmethod
        def cosine (x):
            return math.cos(x)

        @staticmethod
        def tangent(x): 
            return math.tan(x)

        @staticmethod
        def sinh (x):
            return math.sinh(x)

        @staticmethod
        def cosh (x):
            return math.cosh (x)

        @staticmethod
        def tanh (x):
            return math.tanh(x)

runmath = getattr (function_operators, cosh)

answer = runmath(5)