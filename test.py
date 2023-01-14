attempt_limit = float("inf")
attempt_count = 0

selections = ["1 = population", "2 = sample"] 

for x in selections:
    print (x)

selections[0] = 1
selections[1] = 2

while attempt_count < attempt_limit: 
    sample_type = int(input ("Population or sample? "))
    sample_type = sample_type - 1
    attempt_count += 1

    if sample_type == selections.index(1):
        break

    if sample_type == selections.index(2):
        break

if sample_type == 0:
    print ("yes")

if sample_type == 1:
    print("no")
