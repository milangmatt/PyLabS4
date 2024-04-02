import pandas as pd

# Example data
data = {
    'State': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California'],
    'Population': [4903185, 731545, 7278717, 3017825, 39512223],
    'Murder Rate': [8.3, 8.4, 5.5, 8.6, 4.5]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Compute mean, median, and variance for the population
mean_population = df['Population'].mean()
median_population = df['Population'].median()
variance_population = df['Population'].var()

print("Mean population:", mean_population)
print("Median population:", median_population)
print("Variance of population:", variance_population)
