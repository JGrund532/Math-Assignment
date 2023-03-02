import statistics
import math 
from sympy import *
import pandas as pd


class CFormulas():

    @staticmethod
    def mean(data):
        return statistics.mean(data)
    
    @staticmethod
    def range(data):
        return max(data) - min(data)

    @staticmethod
    def median(data):
        return statistics.median(data) 

    @staticmethod 
    def mode (data):
        return statistics.mode(data)

    @staticmethod
    def stdevP (data):
        return statistics.pstdev(data)
    
    @staticmethod
    def stdevS (data):
        return statistics.stdev(data)

    @staticmethod
    def varianceP (data):
        return statistics.pvariance(data)
    
    @staticmethod
    def varianceS (data):
        return statistics.variance(data)
    








class DFormulas():
        
        @staticmethod
        def stdev (variance):
            stdev = math.sqrt(variance)
            return stdev
        
        @staticmethod
        def varianceP (frequency, midpoints, mean):
            variance = sum(frequency[i] * (midpoints[i] - mean)** 2 for i in range(len(midpoints))) / (sum(frequency))
            return variance 
        
        @staticmethod
        def varianceS (frequency, midpoints, mean):
            variance = sum(frequency[i] * (midpoints[i] - mean)** 2 for i in range(len(midpoints))) / (sum(frequency) - 1)
            return variance 
        
        @staticmethod
        def mean (sum_fx, f):
            mean = sum(sum_fx)/sum(f)
            return mean
        
        @staticmethod
        def calc_range (bins):
            upper = (bins[-1]).split('-')
            upper = float(upper[-1])
            lower = (bins[0]).split('-')
            lower = float(lower[0])
            range = upper - lower 
            return range 
        
        @staticmethod
        def median (frequency_list, bins_list):
            cf = DFormulas.culmitive_f(frequency_list)
            n = sum(frequency_list)       #n = sum culumitive freq
            median_index = None
            for i in range(len(cf)):     #for loop finds the median class of the data set (closest class to n/2) 
                if cf[i] >= n/2:
                    median_index = i
                    break 
                print (median_index)
            if median_index is not None:
                median_class = str(bins_list[median_index])
                median_class_l = median_class.split('-')
                l = float(median_class_l[0])                #calculating values for formula 
                freq = frequency_list[median_index]
                median_class_range = float(median_class_l[1]) - l
                cff = cf[median_index]
                median_value = float(l + (((n/2) - cff)/freq) * median_class_range)   #median in discrete return median class  
                return median_class, median_value                                     #and the calculated value
            if median_index is None:
                return 'No median class found'

        @staticmethod
        def culmitive_f (frequency_list):
            total = 0
            cf = []
            for f in frequency_list:
                cf.append(total + f)
            return cf
        
        @staticmethod
        def sumfx (frequency_list, midpoints):
            sum_fx = []
            for i in range(len(frequency_list)):
                sum_fx.append(midpoints[i] * frequency_list[i])
            return sum_fx




#discrete data that uses words is called catagorical data, discrete data that uses number ranges is called quantitative data
#this is needed to be imported into the discrete data function with the user being able to select which type of data they have 


class DataDiscreteQ(list):
    def __init__ (self): 

        #changed to False if user selects 2 from the list below for sample/population stdev
        self.population = True

    #selecting data set type for standard devaition
        selections = ["population", "sample"] 

        for index, data_type in enumerate(selections, start = 1):
            print (f'{index} = {data_type}')

        while True: 
            sample_type = int(input ("Population or sample? "))

            if sample_type == 1: 
                break

            if sample_type == 2:
                self.population = False 
                break
            
        frequency = []
        n = int(input("Number of classes: "))
        class_valuelower = float (input ('Class 1 bottom value: '))
        class_valueupper = float (input ('class 1 upper value: '))
        class2_valuelower = float (input ('Class 2 bottom value: '))
        class_jump = float(class2_valuelower - class_valuelower)
        class_range = class_valueupper - class_valuelower

        bins = []
        print("\n")  
        for i in range(0, n): 
            print(f"{class_valuelower} - {class_valueupper} frequency: ", )
            item = (input())
            item = int(eval(item))
            frequency.append(item) 
            bins.append (f'{class_valuelower} - {class_valueupper}')
            class_valuelower = class_valuelower + class_jump 
            class_valueupper = class_valueupper + class_jump #Calculating the size of each class     
     
        data = {'BIN': bins, 'Frequency': frequency}
        df = pd.DataFrame(data).transpose()
        import string 
        df.columns = list(string.ascii_lowercase[:len(df.columns)]) #switches column naming to letters not numbers 

        self.df = df 
        self.bins = bins  
        self.frequency = frequency
        self.class_range = class_range
       

        #generating a list of the class midpoints for use in calculations 
    def get_midpoints(self):
        midpoints = []
        for class_interval in self.bins:
            lower, upper = map(float, class_interval.split('-'))
            midpoint = (lower + upper)/2
            midpoints.append(midpoint) 
        return midpoints 









class DataContinuous (list):
    def __init__ (self): 

        #changed to False if user selects 2 from the list below
        self.population = True

    #selecting data set type for standard devaition
        selections = ["population", "sample"] 

        for index, option in enumerate(selections, start = 1):
            print (f'{index} = {option}')

        while True: 
            sample_type = int(input ("Population or sample? "))

            if sample_type == 1: 
                type = 'population'
                break

            if sample_type == 2:
                self.population = False
                type = 'sample' 
                break    

    #user input data set, see tools.list_maker for how it works   
        data_set = []
        n = int(input(f"Enter the {type} size "))

        print("\n")  
        for i in range(0, n): 
            print("Enter element ", i + 1 , )
            item = (input())
            item = float(eval(item))
            data_set.append(item) 
        
        print("Data set: ", data_set)

        self.data_set = data_set   


    def index (self, x):                 #creates a method to acess elements in the genrated list above
            return self.data_set.index(x)