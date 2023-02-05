import statistics
import tools.fraction_to_float
import function_formulas
import math 
from sympy import *
import pandas as pd


class DataDiscrete (list):
    def __init__ (self): 

        #changed to False if user selects 2 from the list below
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