import function_operators
import statistics_operator
import probability_operators


def take_second(elem):
    return elem[1]

def take_third(elem):
    return elem[2]

def take_fourth(elem):
    return elem[3]


class Answer (object):
    def __init__ (self, answer):
        self.answer = answer

    #def graph (self):
     #   print 


#                           _________________________________________________________________________________________________________                        
#initial user input for main_________________________________________________________________________________________________________ 



while True: 
        
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

        while True:
            try:
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
                    break

                if func_select == func_options.index(1):
                    
                    hyperbolic_options = ['1 = Hyperbolic', '2 = Inverse hyperbolic']
                    for x in hyperbolic_options: 
                        print (x)

                    hyperbolic_options[0:] = range(2)

                    while True:
                        try:
                            selection = input('Function Type: ')
                            selection = int(selection)
                            selection = selection - 1


                            if selection == hyperbolic_options.index(0):
                                function_operators.HyperbolicOperator()
                                break

                            if selection == hyperbolic_options.index(1):
                                function_operators.InverseHyperbolic()
                                break
                            
                            if selection != hyperbolic_options.index(0) or hyperbolic_options.index(1):
                                raise ValueError ('Error, enter a number 1 or 2 to select')
                        except ValueError as e:
                            print (e)
                    break

                if func_select == func_options.index(2):
                    function_operators.LogarithmicOperators()
                    break
                        
                if func_select == func_options.index(3):
                    function_operators.Exponential()
                    break

                    #while loop triggers if user input is invalid 
                if func_select > 3:
                    raise ValueError ('Error, enter number 1 - 4 to select')

            except ValueError as e:
                print (e)











    if int(option_selection) == my_options.index(1):
        statistics_operator.Data()








    #if user selects probabilty tool 

    if int(option_selection) == my_options.index(2):     
        probability_operators.BinomialExpander()