import statistics
import tools.fraction_to_float
import function_formulas
import math 
from sympy import *
import pandas as pd



class Mean (object):
    def __init__ (self, data_set):
        self.mean = statistics.mean(data_set)
    
    def __float__ (self):
        return float(self.mean)


class Range (object):
    def __init__ (self, data_set):                     #function that is always called to initilaise the class when it is called 
        self.range = max(data_set) - min(data_set)     #the self. makes this class '=' this function 

    def __float__ (self):                              #automatically converts self.range to a float whenever 'float(range)' is called 
        return float (self.range)


class Median (object):
    def __init__ (self, data_set):
        self.median = statistics.median (data_set)

    def __float__ (self):
        return float(self.median)


class Mode (object):
    def __init__ (self, data_set):
        self.mode = statistics.mode (data_set)

    def __float__ (self):
        return float(self.mode)


class StdevP (object):
    def __init__ (self, data_set):
        self.stdev_p = statistics.pstdev (data_set)

    def __float__ (self):
        return float(self.stdev_p)


class StdevS (object):
    def __init__ (self, data_set):
        self.stdev_s = statistics.stdev (data_set)

    def __float__ (self):
        return float(self.stdev_s)


class VarianceP (object):
    def __init__ (self, data_set):
        self.variance_p = statistics.pvariance (data_set)

    def __float__ (self):
        return float(self.variance_p)


class VarianceS (object):
    def __init__ (self, data_set):
        self.variance_s = statistics.variance (data_set)

    def __float__ (self):
        return float(self.variance_s)








class DataDiscrete (list):
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
        class_mid = (class_range)/2
        classes = []

        print("\n")  
        for i in range(0, n): 
            print(f"{class_valuelower} - {class_valueupper} frequency: ", i + 1 , )
            item = (input())
            item = int(eval(item))
            frequency.append(item) 
            classes.append (f'{class_valuelower} - {class_valueupper}')
            class_valuelower = class_valuelower + class_jump
            class_valueupper = class_valueupper + class_jump

        print ('Data classes: ', classes)
        print("Frequency: ", frequency)        
        self.classes = classes  
        self.frequency = frequency  
        
        while True:
            try: 
                print ('Create data frame? Y/N')
                input_df = input('')
                if input_df.upper() == 'Y':    
                    data = {'class': classes, 'frequency': frequency }
                    df = pd.DataFrame(data)
                    self.df = df 
                    break

                if input_df.upper() == 'N':
                    break
                
                if input_df.upper() != 'Y' or input_df.upper != 'N':
                    raise TypeError('Enter Y or N')

            except TypeError as e: 
                print (e) 

     




class DataContinuous (list):
    def __init__ (self): 

        #changed to False if user selects 2 from the list below
        self.population = True

    #selecting data set type for standard devaition
        selections = ["1 = population", "2 = sample"] 

        for index, option in enumerate(selections, start = 1):
            print (f'{index} = {option}')

        while True: 
            sample_type = int(input ("Population or sample? "))
            sample_type = sample_type - 1

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
