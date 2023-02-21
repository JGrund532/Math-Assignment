import math

# Define the class intervals and midpoints
intervals = [(0, 5), (5, 10), (10, 15), (15, 20)]
midpoints = [2.5, 7.5, 12.5, 17.5]

# Define the frequency of each class
frequencies = [3, 5, 7, 4]

# Calculate the mean
total = sum(midpoints[i] * frequencies[i] for i in range(len(midpoints)))
mean = total / sum(frequencies)

# Calculate the variance
variance = sum(frequencies[i] * (midpoints[i] - mean) ** 2 for i in range(len(midpoints))) / sum(frequencies)

# Calculate the standard deviation
stdev = math.sqrt(variance)

print("Mean:", mean)
print("Variance:", variance)
print("Standard deviation:", stdev)