import numpy as np

# Define the data
classes = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80']
frequencies = [5, 10, 20, 40, 30, 20, 10, 5]

# Calculate the midpoints of each class
midpoints = []
for class_range in classes:
    ends = class_range.split('-')
    lower, upper = int(ends[0]),int(ends[1])
    midpoint = (lower + upper) / 2
    midpoints.append(midpoint)
    
# Calculate the mean of the data
mean = np.average(midpoints, weights=frequencies)

# Calculate the variance
variance = np.average((midpoints - mean)**2, weights=frequencies)

# Calculate the standard deviation
std_dev = np.sqrt(variance)

# Calculate the coefficient of variation
coeff_variation = (std_dev / mean) * 100

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation (S.D.):", std_dev)
print("Coefficient of Variation (C.V.):", coeff_variation)
