x = 9.945111111

σ = 0.061074636

lsl = 9.761887204

usl = 10.12833502

def cpk_u ():
    return (usl - x)/(3*σ)

def cpk_l():
    return (x - lsl)/(3*σ)

min_CPK = cpk_l() 
print("L = ", min_CPK) 

max_CPK = cpk_u()
print("U = ", max_CPK)
