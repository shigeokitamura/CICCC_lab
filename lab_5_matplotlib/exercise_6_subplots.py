import matplotlib.pyplot as plt
import numpy as np

# Data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
categories = ["A", "B", "C", "D", "E"]
values = [5, 7, 3, 8, 6]
data = np.random.randn(1000) # 1000 random values
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

# Plotting
fig, axs = plt.subplots(2, 2)

# Line Plot
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Line Plot')

# Bar Plot
axs[0, 1].bar(categories, values)
axs[0, 1].set_title('Bar Plot')

# Histogram
axs[1, 0].hist(data, bins=30, edgecolor='black')
axs[1, 0].set_title('Histogram')

# Scatter Plot
axs[1, 1].scatter(x_scatter, y_scatter)
axs[1, 1].set_title('Scatter Plot')
plt.tight_layout()
plt.show()
