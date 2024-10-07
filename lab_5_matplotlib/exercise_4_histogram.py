import matplotlib.pyplot as plt
import numpy as np

# Data
data = np.random.randn(1000)

# Plotting
plt.hist(data, bins=30, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()
