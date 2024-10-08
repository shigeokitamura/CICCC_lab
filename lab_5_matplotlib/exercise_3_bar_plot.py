import matplotlib.pyplot as plt

# Data
categories = ["Apples", "Bananas", "Cherries", "Dates", "Elderberries"]
values = [10, 15, 7, 12, 5]

# Plotting
plt.bar(categories, values)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Plot")
plt.show()
