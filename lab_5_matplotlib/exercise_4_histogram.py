import matplotlib.pyplot as plt
import numpy as np

# Data
data = np.random.normal(0, 1, 500) # 500 data points from a normal distribution


# Plotting
plt.hist(data, bins=20, edgecolor="black")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()
