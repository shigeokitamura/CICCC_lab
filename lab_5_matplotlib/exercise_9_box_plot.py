import matplotlib.pyplot as plt
import numpy as np

# Data
dataset1 = np.random.normal(60, 10, 100) # 100 data points around mean 60
dataset2 = np.random.normal(70, 15, 100) # 100 data points around mean 70
dataset3 = np.random.normal(80, 5, 100) # 100 data points around mean 80

# Plotting
plt.boxplot([dataset1, dataset2, dataset3], labels=["Dataset 1", "Dataset 2", "Dataset 3"])
plt.xlabel("Dataset")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()

