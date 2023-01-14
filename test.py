def take_second (element):
    return element [1]

def take_third (element):
    return element[2]

def take_fourth (element):
    return element [3]

def take_fifth (element):
    return element [4]

def take_sixth (element):
    return element [5]


if func_select or try_again == options.index(0):
    
    trig_options = ["1 = Sine", "2 = Cosine", "3 = Tangent", "4 = sin -1", "5 = cos -1", "6 = tan -1"]
    for functions in trig_options:
        print (functions)

trig_options[0:] = range(5)

while attempt_count < attempt_limit:
    selection = input ("Select trig function ")
    if selection = trig_options.index(0):
        TrigonometricOperators.sine(x)
        break
    
    trig_options.sort(key = take_second)
    if selection = trig_options.index(0):
        TrigonometricOperators.cosine(x)
        break
