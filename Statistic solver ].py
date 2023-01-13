import math 
import statistics
import tools.fraction_to_float

class Data (object):
    def __init__ (self): 

        selections = ["1 = sample", "2 = population"]

        for x in selections:
            print (x)

    #Is the data set a sample of a larger data set or there whole population? (needed for stadard deviation)
        mySelection = input ("Population or sample? ") 

    #user input data set 
        InputdataSet = input ("Enter your data ")

    #splits user input into indexes for list 
        MyData = InputdataSet.split()

    #prints the user input in the form of a list 
        print ("My data:", MyData)


    #converts each index in list to a float 
        for i in range(len(MyData)):
          MyData[i] = float(MyData[i])


def calculations (data_set):
            return statistics.mean({data_set})


Data()
