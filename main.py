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
import probability_formulas as pf 
import numpy as np 
import matplotlib.pyplot as plt 
import scipy.stats as stats
import math 





class PlotBellZPDF ():
    def __init__ (self, z):
        self.z = z


    def plot_a (self, x_value, mean):
        inf = str(math.inf)
        total = 1
        mu = 0
        sigma = math.sqrt(total)
        x = np.linspace((0 - (sigma*3.49)),(0 + (sigma*3.49)), 100) 
        y = stats.norm.pdf (x, mu, sigma)
        plt.plot(x, y, 'r-', label = f'Z = {self.z}')
        if x_value > mean:
            plt.fill_between(x[x>self.z], y[x>self.z], 0, color='red', alpha = 0.3)
        
        elif x_value < mean:
            plt.fill_between(x[x<self.z], y[x<self.z], 0, color='red', alpha = 0.3)
        
            
        plt.title(f"Normal Distribution Chart A (-{inf} - z)")
        plt.xlabel("Z Score")
        plt.ylabel("Probability Density")
        plt.legend(loc = 'upper left')
        plt.show()


    def plot_b (self):
        inf = str(math.inf)
        total = 1
        x_bar = 0
        sigma = math.sqrt(total)
        x = np.linspace((0 - (sigma*3.49)),(0 + (sigma*3.49)), 100) 
        y = stats.norm.pdf (x, x_bar, sigma)
        plt.plot(x, y, 'r-', label = f'Z = {self.z}')
        plt.fill_between(x[x<self.z], y[x<self.z], 0, color='red', alpha = 0.3)
        plt.title(f"Normal Distribution Chart B (-{inf} - z)")
        plt.xlabel("Z Score")
        plt.ylabel("Probability Density")
        plt.legend(loc = 'upper left')
        plt.show()


    def plot_c (self):
        total = 1
        x_bar = 0
        sigma = math.sqrt(total)
        x = np.linspace((0 - (sigma*3.49)),(0 + (sigma*3.49)), 100) 
        y = stats.norm.pdf (x, x_bar, sigma)
        plt.plot(x, y, 'r-', label = f'Z = {self.z}')
        plt.fill_between(x[x>self.z], y[x>self.z], 0, color='red', alpha = 0.3)
        plt.title(f"Normal Distribution Chart C (mean - z)")
        plt.xlabel("Z Score")
        plt.ylabel("Probability Density")
        plt.legend(loc = 'upper left')
        plt.show()





class BellChart ():
    def __init__ (self, x_bar, sigma):
        self.x_bar = x_bar
        self.sigma = sigma 

        x = np.linspace((self.x_bar - (self.sigma*4)), (self.x_bar + (self.sigma*4)), 100)
        y = (x, self.x_bar, self.sigma)
        plt.plot(x, y, '-r')


#                           _________________________________________________________________________________________________________                        
#initial user input for main_________________________________________________________________________________________________________ 



while True: 

    try:    
        my_options = ["Function Tool", "Statistic Tool", "Probability Tool", 'Quit']

        for index, option in enumerate (my_options, start = 1):
            print(f'{index} = {option}')

        option_selection = int(input(""))


        if option_selection == len(my_options) :
            break









#running function slelection

        if option_selection == 1:

            while True:
                try:
                    func_options = ["Trigonometric", "Hyperbolic", "Logarithmic", "Exponential", 'Back']

                    for index, option in enumerate(func_options, start = 1): 
                        print (f'{index} = {option}') 

                    func_select = int(input("Function type: " ))

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

            stat_options = ['Continuous', 'Discrete']
            
            for index, option in enumerate(stat_options, start = 1):
                print (f'{index} = {option}')

            stat_select = int(input('Data type: '))

            if stat_select == 1: 
                    
                data = so.DataContinuous()
                population_value = data.population

                mean = so.Mean(data.data_set)
                _range = so.Range(data.data_set)
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


                if stat_select == 2:

                    data = so.DataDiscrete()
                    population_value = data.population



            calculations = [f'Mean: {float(mean)}', f'Range: {float(_range)}', f'Median: {float(median)}', 
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

                #selecting whether data is continuous or discrete
                    if prob_select == 2:
                        while True: 
                            try:
                                set_type = ['Discrete', 'Continuous', 'Back' ]

                                for index, option in enumerate(set_type, start = 1):
                                    print (f'{index} = {option}')

                                type_select = int(input('Data type: ')) 
                                
                                population_value = None
                                mean = None


                        #if discrete data is selected 
                                if type_select == 1:

                                    data = so.DataDiscrete()
                                    population_value = data.population
                                    frequency = data.frequency 
                                    midpoints = data.get_midpoints()

                            #generating a list to alculate the mean 
                                    sum_fx = []
                                    for i in range(len(frequency)):
                                        sum_fx.append(midpoints[i] * frequency[i])
                                    mean = so.MeanDiscrete(sum(sum_fx), sum(frequency))
                                    mean = float(mean)


                            #plot graph after generating z score via PO module 
                                while True:
                                    try:                                        
                                        run = po.NormalDistribution(population_value)
                                        run.discrete(frequency, mean, midpoints)
                                        z = run.z
                                        x = run.x
                                        graph = PlotBellZPDF(z)
                                        graph.plot_a(x, mean)
                                        print ('Revaluate x? Y/N')
                                        go_again = input ('')
                                        if go_again.upper() == 'N': 
                                            break

                                        if go_again.upper() != 'Y':
                                            raise TypeError(f'Enter Y/N')
                                        
                                    except TypeError as e:
                                        print (e)


                        #if continuous data is selected 
                                if type_select == 2: 
                                    data = so.DataContinuous()
                                    print ()
                                    break

                                if type_select == 3:
                                    break
                                    

                        #type error if invalid input 
                                if type_select < 1 or type_select > len(set_type):
                                    raise ValueError (f'Select 1 - {len(set_type)}')

                            except ValueError as e: 
                                print (e)


                    if prob_select > len(prob_options):
                        raise ValueError (f'enter number 1 - {len(prob_options)}')
                except ValueError as e:
                    print (e)
                    

    






        if option_selection < 1 or option_selection > len(my_options):
            raise ValueError (f'Enter number 1 - {len(my_options)}') 
    except ValueError as e:
        print (e)