import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from file
data = pd.read_csv(r'C:\Users\SANSHIYA\Downloads\data1.csv')

# Create a histogram of the data
hist, bins = np.histogram(data, bins=10)

# Calculate the midpoint of each bin
bin_midpoints = (bins[1:] + bins[:-1]) / 2

# Plot the histogram
plt.figure(figsize=(8, 5))

plt.hist(data, bins=20, color= 'purple')
plt.xlabel("Weight (in pounds)")
plt.ylabel("Frequency")
plt.title("Distribution of Newborn Weights")
plt.axvline(x = 3.393193, linestyle='--', color='red')
plt.grid(True)
plt.legend(loc = 'lower left', bbox_to_anchor=(1, 0.5))


# Add legends
plt.legend(['Mean value = 3.393193', 'w'], loc='upper right')

# Calculate the average weight
average_weight = np.mean(data)

# Calculate X such that 33% of newborns are born with a weight above X
X = np.percentile(data, 33)

# Print the values of average weight and X on the graph
plt.text(plt.xlim()[1] * 0.7, plt.ylim()[1] * 0.8, f"Average weight: {average_weight:.2f}")
plt.text(plt.xlim()[1] * 0.7, plt.ylim()[1] * 0.7, f"X: {X:.2f}")

plt.show()
