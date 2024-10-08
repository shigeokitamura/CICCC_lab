import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.random.rand(50) # 50 random x-values between 0 and 1
y = np.random.rand(50) # 50 random y-values between 0 and 1

# Plotting
plt.scatter(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
plt.show()
