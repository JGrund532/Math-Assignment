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
import scipy.stats as stats
import math 





class PlotBellZPDF ():
    def __init__ (self, z):
        self.z = z
        self.fig, self.ax = plt.subplots() 


    def plot_a (self, x_value, mean, z_alpha = None):
        inf = str(math.inf)
        total = 1
        mu = 0
        sigma = math.sqrt(total)
        x = np.linspace((0 - (sigma*3.49)),(0 + (sigma*3.49)), 100) 
        y = stats.norm.pdf (x, mu, sigma)
        self.ax.plot(x, y, 'r-', label = f'Z = {self.z}')


     #configuring which side of the bell curve needs to be shaded    
        if x_value > mean:
            self.ax.fill_between(x[x>self.z], 
                                 y[x>self.z], 
                                 0, color='red', alpha = 0.3)
            self.ax.annotate ('z score', xy = (self.z,0), xytext = ((self.z + 1), 0.3), 
                            arrowprops=dict(facecolor='black', shrink=0.05))
        
        elif x_value < mean:
            self.ax.fill_between(x[x<self.z], 
                                 y[x<self.z], 
                                 0, color='red', alpha = 0.3)
            self.ax.annotate ('z score', xy = (self.z,0), xytext = ((self.z - 1), 0.3), 
                    arrowprops=dict(facecolor='black', shrink=0.05))
            

        self.ax.set_title(f"Normal Distribution Chart A (-{inf} - z)")
        self.ax.set_xlabel("Z Score")
        self.ax.set_ylabel("Probability Density")
        self.ax.legend(loc = 'upper left')
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




    def plot_significance(self, x_value, z_alpha):
        inf = str(math.inf)
        total = 1
        mu = 0
        sigma = math.sqrt(total)
        x = np.linspace((0 - (sigma*3.49)),(0 + (sigma*3.49)), 100) 
        y = stats.norm.pdf(x, mu, sigma)
        self.ax.plot(x, y, 'r-', label=f'Z = {self.z}')

        # create boolean masks based on conditionals
        mask_greater = x > z_alpha
        mask_less = x < z_alpha
        
        # configure which side of the bell curve needs to be shaded
        if x_value > z_alpha:
            self.ax.fill_between(x[mask_greater], y[mask_greater], 0, color='red', alpha=0.3)
            self.ax.annotate('z value', xy=(self.z, 0), xytext=((self.z - 1), 0.15), 
                arrowprops=dict(facecolor='grey', shrink=0.05))
            self.ax.annotate('\u03B1', xy=(z_alpha, 0), xytext=((self.z - 2.2), 0.1), 
                arrowprops=dict(facecolor='grey', shrink=0.05))
            self.ax.set_title(f"Critical Region (\u03B1 - z)")
            
        elif x_value < z_alpha:
            self.ax.fill_between(x[mask_less], y[mask_less], 0, color='red', alpha=0.3)
            self.ax.annotate('z score', xy=(self.z, 0), xytext=((self.z + 1), 0.3), 
                arrowprops=dict(facecolor='black', shrink=0.05))
            self.ax.annotate('\u03B1', xy=(z_alpha, 0), xytext=((self.z + 2), 0.3), 
                arrowprops=dict(facecolor='black', shrink=0.05))
            self.ax.set_title(f"Critical Region (z - \u03B1)")
            
        self.ax.set_xlabel("Significance")
        self.ax.set_ylabel("Probability Density")
        self.ax.legend(loc='upper left')
        plt.show()









class BellChart ():
    def __init__ (self, x_bar, sigma):
        self.x_bar = x_bar
        self.sigma = sigma 

        x = np.linspace((self.x_bar - (self.sigma*4)), (self.x_bar + (self.sigma*4)), 100)
        y = (x, self.x_bar, self.sigma)
        plt.plot(x, y, '-r')









class Histogram():
    def __init__ (self, bins, frequency):
        self.bins = bins 
        self.frequency = frequency

        def without_bell (self):
            plt.hist(frequency, bins = bins)
            plt.show()

        







class get_data():
    def __init__ (self):
        self.data = None

    def get_continuous (self):
        variance = None
        stdev = None
        data = so.DataContinuous()
        population_value = data.population

        mean = so.Formulas.mean(data.data_set)
        _range = so.Formulas.range(data.data_set)
        median = so.Formulas.median(data.data_set)
        mode = so.Formulas.mode(data.data_set)

        if population_value == True:
            stdev = so.Formulas.stdevP (data.data_set)
            variance = so.Formulas.varianceP(data.data_set)
            label = '(P)'

        elif population_value == False:
            stdev = so.Formulas.stdevS (data.data_set)
            variance = so.Formulas.varianceS (data.data_set)
            label = '(S)'

        return mean, _range, median, mode, stdev, variance 



    def get_discrete(self):
        discrete_options = ['Quantitative', 'Catagorical']

        for index, option in enumerate (discrete_options, start = 1):
            print (f'{index} = {option}') 

        discrete_select = int(input('Discrete data type: '))

        if discrete_select == 1:
            data = so.DataDiscreteQ()
            population_value = data.population
            df = data.df
            print (df)
            population_value = data.population
            frequency = data.frequency 
            midpoints = data.get_midpoints()

        #generating a list to calculate the mean 
            sum_fx = []
            for i in range(len(frequency)):
                sum_fx.append(midpoints[i] * frequency[i])
            mean = so.DiscreteFormulas.mean(sum_fx,frequency)
            mean = float(mean)
        
        #calculating stdev using the correct formula based on whether a population or sample is being used
            if population_value == True: 
                stdev = so.DiscreteFormulas.stdevP(frequency, midpoints, mean)

            if population_value == False:
                stdev = so.DiscreteFormulas.stdevS(frequency, midpoints, mean)




        def get_stats (self):
            calculations_c = [f'Mean: {float(mean)}', f'Range: {float(_range)}', f'Median: {float(median)}', 
                            f'Mode: {float(mode)}', f'Std deviation{label}: {float(stdev)}',
                            f'Variance{label}: {float(variance)}']

            for answers in calculations_c:
                print(answers)




#                           _________________________________________________________________________________________________________                        
#initial user input for main_________________________________________________________________________________________________________ 



while True: 

    try:    
        my_options = ["Function Tool", "Statistic Tool", "Probability Tool", 'Quit']

        for index, option in enumerate (my_options, start = 1):
            print(f'{index} = {option}')

        option_selection = int(input(""))


    #allows the user to quit program
        if option_selection == len(my_options) :
            break








#_______________________________________________________________________________________________________________________________________
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








#_______________________________________________________________________________________________________________________________________
#statistics tool 

        if option_selection == 2:

            stat_options = ['Continuous', 'Discrete']
            
            for index, option in enumerate(stat_options, start = 1):
                print (f'{index} = {option}')

            stat_select = int(input('Data type: '))

            if stat_select == 1: 
                    
                data = so.DataContinuous()
                population_value = data.population

                mean = so.Formulas.mean(data.data_set)
                _range = so.Formulas.range(data.data_set)
                median = so.Formulas.median(data.data_set)
                mode = so.Formulas.mode(data.data_set)

                if population_value == True:
                    stdev = so.Formulas.stdevP (data.data_set)
                    variance = so.Formulas.varianceP(data.data_set)
                    label = '(P)'

                elif population_value == False:
                    stdev = so.Formulas.stdevS (data.data_set)
                    variance = so.Formulas.varianceS (data.data_set)
                    label = '(S)'

                calculations_c = [f'Mean: {float(mean)}', f'Range: {float(_range)}', f'Median: {float(median)}', 
                                f'Mode: {float(mode)}', f'Std deviation{label}: {float(stdev)}',
                                f'Variance{label}: {float(variance)}']

                for answers in calculations_c:
                    print(answers)




            if stat_select == 2:

                discrete_options = ['Quantitative', 'Catagorical']

                for index, option in enumerate (discrete_options, start = 1):
                    print (f'{index} = {option}') 

                discrete_select = int(input('Discrete data type: '))

                if discrete_select == 1:
                    data = so.DataDiscreteQ()
                    population_value = data.population
                    df = data.df
                    print (df)
                    population_value = data.population
                    frequency = data.frequency 
                    midpoints = data.get_midpoints()

                #generating a list to calculate the mean 
                    sum_fx = []
                    for i in range(len(frequency)):
                        sum_fx.append(midpoints[i] * frequency[i])
                    mean = so.DiscreteFormulas.mean(sum_fx,frequency)
                    mean = float(mean)
                
                #calculating stdev using the correct formula based on whether a population or sample is being used
                    if population_value == True: 
                        stdev = so.DiscreteFormulas.stdevP(frequency, midpoints, mean)

                    if population_value == False:
                        stdev = so.DiscreteFormulas.stdevS(frequency, midpoints, mean)


            #probabilty tool activated if needed
                print('Calculate statistcal probabilty? Y/N')

                sprob_calc = input('')

                if sprob_calc.upper() == 'Y':

                    sprob_options = ['Z Score Calc', 'Significance Testing', 'Back']

                    for index, option in enumerate (sprob_options, start = 1):
                        print (f'{index} = {option}')   

                    sprob_select = int(input (''))

                #calculating z score and plotting bell graph 
                    if sprob_select == 1:
                        while True:
                            try:                                        
                                run = po.NormalDistribution(population_value)
                                run.discrete(frequency, mean, midpoints, stdev)
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



                #claculating significance level and plotting a bell chart to graphically represent 
                    if sprob_select == 2:
                        pass

                        

                        
                        
                        
                        


#_______________________________________________________________________________________________________________________________________
    #probabilty options 
        if option_selection == 3:     

            while True:
                try:
                    prob_options = ['Binomial expander', 'Normal distribution', 'Significance testing', 'Back']

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

                                if type_select == len(set_type):
                                    break
                                
                                population_value = None
                                mean = None


                        #if discrete data is selected 
                                if type_select == 1:

                                    data = so.DataDiscreteQ()
                                    print (data.df)
                                    population_value = data.population
                                    frequency = data.frequency 
                                    midpoints = data.get_midpoints()

                            #generating a list to calculate the mean 
                                    sum_fx = []
                                    for i in range(len(frequency)):
                                        sum_fx.append(midpoints[i] * frequency[i])
                                    mean = so.DiscreteFormulas.mean(sum_fx,frequency)
                                    mean = float(mean)

                                    if population_value == True: 
                                        stdev = so.DiscreteFormulas.stdevP(frequency, midpoints, mean)

                                    if population_value == False:
                                        stdev = so.DiscreteFormulas.stdevS(frequency, midpoints, mean)

                            #plot graph after generating z score via PO module 
                                while True:
                                    try:                                        
                                        run = po.NormalDistribution(population_value)
                                        run.discrete(frequency, mean, midpoints, stdev)
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

                        
                    if prob_select == 3:
                        known_data = input ('Are key data variable known? (mean, standard deviation etc.): Y/N')
                        if known_data.upper() == 'Y':
                            sample_def = input('Testing a sample from a batch? Y/N')
                            if sample_def.upper() == 'Y':

                                mu = float(input('Population mean: '))
                                x_bar = float(input('Sample mean: '))
                                pop_size = float(input('Population size: '))
                                sample_size = float(input('Sample size: '))
                                stdevs = float(input('Sample standard deviation: '))    
                        
                                run = po.Significance()
                                z = run.get_significance()
                                z_alpha = run.calcz_alpha()
                                answer = run.answer(mu, x_bar, pop_size, sample_size, stdevs)

                                print (run.alpha)
                                print (run.z_alpha)
                                print (run.answer)

                                z_alpha = float(run.z_alpha)
                                answer = float(run.answer)
                                graph = PlotBellZPDF(answer)
                                graph.plot_significance(answer, z_alpha)



                                
                                        




                      


                    if prob_select > len(prob_options):
                        raise ValueError (f'enter number 1 - {len(prob_options)}')
                except ValueError as e:
                    print (e)
                    

    






        if option_selection < 1 or option_selection > len(my_options):
            raise ValueError (f'Enter number 1 - {len(my_options)}') 
    except ValueError as e:
        print (e)