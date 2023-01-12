import math
import matplotlib
import fractions
import matplotlib.pyplot as plt
import numpy as np
import Solver


#list of options presented to the user
my_options = ["1 = solve a function", "2 = statistical"]

#prints the options to the user to select using a number 
for x in my_options:
    print(x)

#user input
option_selection = input("what are you trying to do? ")

if int(option_selection) == 1: 
    Solver.funcSolver()



