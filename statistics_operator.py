import statistics
import math 
from sympy import *
import pandas as pd


class Formulas():

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
    








class DiscreteFormulas():
        
        @staticmethod
        def stdevP (frequency, midpoints, mean):
            variance = sum(frequency[i] * (midpoints[i] - mean)**2 for i in range(len(midpoints))) / sum(frequency)
            stdev = math.sqrt(variance)
            return stdev

        @staticmethod
        def stdevS (frequency, midpoints, mean):
            variance = sum(frequency[i] * (midpoints[i] - mean)** 2 for i in range(len(midpoints))) / (sum(frequency) - 1)
            stdev = math.sqrt(variance)
            return stdev
        
        @staticmethod
        def mean (sum_fx, f):
            mean = sum(sum_fx)/sum(f)
            return mean




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

        classes = []
        print("\n")  
        for i in range(0, n): 
            print(f"{class_valuelower} - {class_valueupper} frequency: ", )
            item = (input())
            item = int(eval(item))
            frequency.append(item) 
            classes.append (f'{class_valuelower} - {class_valueupper}')
            class_valuelower = class_valuelower + class_jump 
            class_valueupper = class_valueupper + class_jump #Calculating the size of each class

        print ('Data classes: ', classes)
        print("Frequency: ", frequency)        
     
        data = {'BIN': classes, 'frequency': frequency }
        df = pd.DataFrame(data)

        self.df = df 
        self.classes = classes  
        self.frequency = frequency
       

        #generating a list of the class midpoints for use in calculations 
    def get_midpoints(self):
        midpoints = []
        for class_interval in self.classes:
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