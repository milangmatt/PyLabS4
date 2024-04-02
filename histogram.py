import matplotlib.pyplot as plt

# Define the data

frequency = [4, 12, 16, 8]
bin_edges = [135, 140, 145, 150, 155]

# Create the histogram
plt.hist(bin_edges[:-1], bins=bin_edges, weights=frequency, edgecolor='black', alpha=0.7)

# Add labels and title
plt.xlabel('Height')
plt.ylabel('Number of Students')
plt.title('Histogram of Student Heights')

# Show the plot
plt.show()
