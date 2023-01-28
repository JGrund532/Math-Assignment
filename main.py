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


#class Answer (self):
#    def __init__ (self, answer_1):
#        self.answer = answer


#                           _________________________________________________________________________________________________________                        
#initial user input for main_________________________________________________________________________________________________________ 



while attempt_count < attempt_limit: 
        
    my_options = ["1 = Function Tool", "2 = Statistic Tool", "3 = Probability Tool", '4 = Quit']

    for x in my_options:
        print(x)

    option_selection = int(input(""))

    my_options[:0] = range(4)

    option_selection = option_selection - 1

    if option_selection == my_options.index(3):
        break






    #function selection type for index 0

    if int(option_selection) == my_options.index(0):

    
        func_options = ["1 = Trigonometric", "2 = Hyperbolic", "3 = Logarithmic", "4 = Exponential"]

        for x in func_options: 
            print (x) 

        #converting option list elements to numbers for reference in input and while loop.  
        func_options[0:] = range(4)

        #user input 
        func_select = int(input("Function type: " ))

        func_select = func_select - 1 

        if func_select == func_options.index(0):
            function_operators.TrigOperator()


        if func_select == func_options.index(1):
            
            hyperbolic_options = ['1 = Hyperbolic', '2 = Inverse hyperbolic']
            for x in hyperbolic_options: 
                print (x)

            hyperbolic_options[0:] = range(2)

            selection = input('Function Type: ')
            selection = int(selection)
            selection = selection - 1


            if selection == hyperbolic_options.index(0):
                function_operators.HyperbolicOperator()

            if selection == hyperbolic_options.index(1):
                function_operators.InverseHyperbolic()

    #while loop triggers if user input is invalid 1
            if selection > 1:
                while attempt_count < attempt_limit:
                    try_again = int(input ("Error, enter a number 1 or 2 to select. Function type: "))

                    try_again = try_again - 1

                    if try_again == hyperbolic_options.index(0):
                        function_operators.HyperbolicOperator()
                        break  

                    if try_again == hyperbolic_options.index(1):
                        function_operators.InverseHyperbolic()
                        break 
        

        if func_select == func_options.index(2):
            function_operators.LogarithmicOperators()

        
        if func_select == func_options.index(3):
                function_operators.Exponential()

    #while loop triggers if user input is invalid 
        if func_select > 3:
            while attempt_count < attempt_limit:
                try_again = int(input ("Error, enter a number 1 to 4 to select. Function type: "))

                try_again = try_again - 1

                if try_again == func_options.index(0):
                    function_operators.TrigOperator()
                    break  

                if try_again == func_options.index(1):
                    function_operators.HyperbolicOperator()
                    break

                if try_again == func_options.index(2): 
                    function_operators.LogarithmicOperators()
                    break

                if try_again == func_options.index(3): 
                    function_operators.Exponential()
                    break
            












    if int(option_selection) == my_options.index(1):
        statistics_output.Data()








    #if user selects probabilty tool 

    if int(option_selection) == my_options.index(2):     
        probability_operators.ProbabilityOperator()