import matplotlib.pyplot as plt

# Data
categories = ["Group 1", "Group 2", "Group 3"]
value1 = [5, 7, 3]
value2 = [6, 8, 4]
value3 = [4, 3, 5]

# Plotting
plt.stackplot(categories, value1, value2, value3)
plt.legend(["Value 1", "Value 2", "Value 3"], loc="upper right")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Stacked Bar Plot")
plt.show()
