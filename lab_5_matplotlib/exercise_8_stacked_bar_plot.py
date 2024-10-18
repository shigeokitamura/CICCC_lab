import matplotlib.pyplot as plt
import numpy as np


# Data
categories = ["Group 1", "Group 2", "Group 3"]
value1 = [5, 7, 3]
value2 = [6, 8, 4]
value3 = [4, 3, 5]

# Plotting
width = 0.35
x = np.arange(len(categories))

plt.bar(x, value1, width, label='Value 1')
plt.bar(x, value2, width, bottom=value1, label='Value 2')
plt.bar(x, value3, width, bottom=np.array(value1) + np.array(value2), label='Value 3')

plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Stacked Bar Plot")
plt.xticks(x, categories)
plt.legend(loc="upper right")

plt.tight_layout()
plt.show()