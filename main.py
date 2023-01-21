import function_operators
import statistics_output
import probability_operators


def take_second(elem):
    return elem[1]

def take_third(elem):
    return elem[2]

def take_fourth(elem):
    return elem[3]



#attempt limit used when initiating while loops throughout code

attempt_limit = float("inf")
attempt_count = 0


#class AnswerLog (self):
#    def __init__ (self, answer_1, answer_2):
#        self.answer_1 = answer_1
#        self.answer_2 = answer_2


#                           _________________________________________________________________________________________________________                        
#initial user input for main_________________________________________________________________________________________________________ 




my_options = ["1 = Function Tool", "2 = Statistic Tool", "3 = Probability Tool", "4 = Arithmetic", "5 = Equation Solver"]

for x in my_options:
    print(x)

option_selection = int(input("what are you trying to do? "))

my_options[:0] = range(5)

option_selection = option_selection - 1

#input function catagory 

if int(option_selection) == my_options.index(0):

 
    options = ["1 = Trigonometric", "2 = Hyperbolic", "3 = Logarithmic", "4 = Exponential"]

    for x in options: 
        print (x) 

    #converting option list elements to numbers for reference in input and while loop.  
    options[0:] = range(4)

    #user input 
    func_select = int(input("Function type: " ))

    func_select = func_select - 1 

    if func_select == options.index(0):
        function_operators.TrigOperator()


    if func_select == options.index(1):
        
        options = ['1 = Hyperbolic', '2 = Inverse hyperbolic']
        for x in options: 
            print (x)

        options[0:] = range(2)

        selection = input('Function Type: ')
        selection = int(selection)
        selection = selection - 1


        if selection == options.index(0):
            function_operators.HyperbolicOperator()

        if selection == options.index(1):
            function_operators.InverseHyperbolic()

#while loop triggers if user input is invalid 1
        if selection > 1:
            while attempt_count < attempt_limit:
                try_again = int(input ("Error, enter a number 1 to 4 to select. What is your function? "))

                try_again = try_again - 1

                if try_again == options.index(0):
                    function_operators.HyperbolicOperator()
                    break  

                if try_again == options.index(1):
                    function_operators.InverseHyperbolic()
                    break 


#while loop triggers if user input is invalid 
    if func_select > 1:
        while attempt_count < attempt_limit:
            try_again = int(input ("Error, enter a number 1 to 4 to select. What is your function? "))

            try_again = try_again - 1

            if try_again == options.index(0):
                function_operators.TrigOperator()
                break  

            if try_again == options.index(1):
                function_operators.HyperbolicOperator()
                break

            if try_again == options.index(2): 
                break

            if try_again == options.index(3): 
                break
        












if int(option_selection) == my_options.index(1):
    statistics_output.Data()








#if user selects probabilty tool 

if int(option_selection) == my_options.index(2):     
    probability_operators.ProbabilityOperator()
