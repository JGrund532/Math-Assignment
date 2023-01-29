import statistics
import tools.fraction_to_float
import function_formulas
import math 



class Data (list):
    def __init__ (self): 

        #changed to False if user selects 2 from the list below
        self.population = True

    #selecting data set type for standard devaition
        selections = ["1 = population", "2 = sample"] 

        for x in selections:
            print (x)

    #changing index elements to 1 and 2 to break the while loop that only allows correct input 
        selections[0] = 1
        selections[1] = 2


        while True: 
            sample_type = int(input ("Population or sample? "))
            sample_type = sample_type - 1

            if sample_type == selections.index(1): 
                break

            if sample_type == selections.index(2):
                self.population = False 
                break
            

    #user input data set, see tools.list_maker for how it works   
        data_set = []
        n = int(input("Enter the population size "))

        print("\n")  
        for i in range(0, n): 
            print("Enter element ", i + 1 , )
            item = float(input()) #user input  
            data_set.append(item) 
        
        print("Data set: ", data_set)

        self.data_set = data_set                  #passes the list generated back to self so it can be accessed from other classes


    def access_element (self, x):                 #creates a method to acess elements in the genrated list above
            return self.data_set.index(x)




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



     


