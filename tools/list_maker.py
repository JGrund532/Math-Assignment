#creates a list with n amount of indexes, user inputs each element manually   



data_set = []
n = int(input("Enter the population size "))

print("\n") #Uses n variable to accept data n amount of times 
for i in range(0, n): #starts a for loop with n amount of rows 
    print("Enter element ", i + 1 , )
    item = float(input()) #user input 
    data_set.append(item) #appends the list after each input 