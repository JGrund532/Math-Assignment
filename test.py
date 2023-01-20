import sympy
from sympy import *
from sympy import sin
import math 

x = 22
answer = sin(x*(pi/180))
#answer = str(x)
#answer = sympify(answer)
answer = answer.evalf(100)

print (answer)


answer_2 = math.sin(x*(pi/180))
print(answer_2)

