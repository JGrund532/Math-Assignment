"""

Author: Josh Grundy 
Date: 31/01/2023

Description:
To make completing a level 4 maths assignment easier w/ calculations and graph generation 

[Additional Information about the Code and its Use]

"""
import function_operators as fo 
import statistics_operator as so
import probability_operators as po 
import numpy as np 
import matplotlib.pyplot as plt 



class PlotBellCurve ():
    def __init__ (self, z_score, x_bar, sigma):
        self.z_score = z_score
        self.x_bar = x_bar 
        self.sigma = sigma

    def plot_a (self):
        x = np.linspace((self.x_bar - (self.sigma*4)), (self.x_bar + (self.sigma*4)), 100)
        y = (x, self.x_bar, self.sigma)


    def plot_b (self):
        x = np.linspace((self.x_bar - (self.sigma*4)), (self.x_bar + (self.sigma*4)), 100)
        y = (x, self.x_bar, self.sigma)


    def plot_c (self):
        x = np.linspace((self.x_bar - (self.sigma*4)), (self.x_bar + (self.sigma*4)), 100)
        y = (x, self.x_bar, self.sigma)


    def plot_normal (self):
        x = np.linspace((self.x_bar - (self.sigma*4)), (self.x_bar + (self.sigma*4)), 100)
        y = (x, self.x_bar, self.sigma)



#                           _________________________________________________________________________________________________________                        
#initial user input for main_________________________________________________________________________________________________________ 



while True: 

    try:    
        my_options = ["Function Tool", "Statistic Tool", "Probability Tool", 'Quit']

        for index, option in enumerate (my_options, start = 1):
            print(f'{index} = {option}')

        #for x in my_options: 
         #   print(x)

        option_selection = int(input(""))

        #my_options[:0] = range (4)

        #option_selection = option_selection - 1

        if option_selection == len(my_options) :
            break






        #function selection type for index 0

        if option_selection == 1:

            while True:
                try:
                    func_options = ["Trigonometric", "Hyperbolic", "Logarithmic", "Exponential", 'Back']

                    for index, option in enumerate(func_options, start = 1): 
                        print (f'{index} = {option}') 

                    #converting option list elements to numbers for reference in input and while loop.  
                    #func_options[0:] = range(4)

                    #user input 
                    func_select = int(input("Function type: " ))

                    #func_select = func_select - 1 

                    if func_select == 1:
                        fo.TrigOperator()
                        break

                    if func_select == 2:
                        
                        hyperbolic_options = ['Hyperbolic', 'Inverse hyperbolic', 'Back']
                        for index, option in enumerate(hyperbolic_options, start = 1): 
                            print (f'{index} = {option}')

                        while True:
                            try:
                                selection = int(input('Function Type: '))

                                if selection == 1:
                                    fo.HyperbolicOperator()

                                if selection == 2:
                                    fo.InverseHyperbolic()

                                if selection == len(hyperbolic_options):
                                    break
                                
                                if selection < 1 or selection > len(hyperbolic_options):
                                    raise ValueError (f'Enter number 1 - len{hyperbolic_options} to select')
                            except ValueError as e:
                                print (e)
                        break

                    if func_select == 3:
                        fo.LogarithmicOperators()
                        break
                            
                    if func_select == 4:
                        fo.Exponential()
                        break

                    if func_select == len(func_options):
                        break

                        #while loop triggers if user input is invalid 
                    if func_select < 1 or func_select > len(func_options):
                        raise ValueError (f'Error, enter number 1 - {func_options} to select')

                except ValueError as e:
                    print (e)



#statistics tool 

        if option_selection == 2:

            data = so.Data()
            population_value = data.population

            mean = so.Mean(data.data_set)
            range = so.Range(data.data_set)
            median = so.Median(data.data_set)
            mode = so.Mode(data.data_set)

            if population_value == True:
                stdev = so.StdevP (data.data_set)
                variance = so.VarianceP(data.data_set)
                label = '(P)'

            elif population_value == False:
                stdev = so.StdevS (data.data_set)
                variance = so.VarianceS (data.data_set)
                label = '(S)'

            calculations = [f'Mean: {float(mean)}', f'Range: {float(range)}', f'Median: {float(median)}', 
                            f'Mode: {float(mode)}', f'Std deviation{label}: {float(stdev)}',
                            f'Variance{label}: {float(variance)}']

            for answers in calculations:
                print(answers)




#if user selects probabilty tool 

        if option_selection == 3:     

            while True:
                try:
                    prob_options = ['Binomial expander', 'Normal distribution', 'Back']

                    for index, option in enumerate (prob_options, start = 1):
                        print (f'{index} = {option}')
                    
                    answer = 0

                    prob_select = int(input('Tool: '))

                    if prob_select == len(prob_options):
                        break 

                    if prob_select == 1:
                        po.BinomialExpander()
                        print (float(answer))

                    if prob_select == 2:
                        answer = po.NormalDistribution()
                        print (float(answer))
                        Answer(answer)


                    if prob_select > len(prob_options):
                        raise ValueError (f'enter number 1 - {len(prob_options)}')
                except ValueError as e:
                    print (e)
                    

    





        if option_selection < 1 or option_selection > len(my_options):
            raise ValueError (f'Enter number 1 - {len(my_options)}') 
    except ValueError as e:
        print (e)