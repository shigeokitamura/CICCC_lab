import matplotlib.pyplot as plt

# Data
categories = ["Marketing", "Development", "Sales", "Support"]
values = [20, 35, 25, 20]

# Plotting
plt.pie(values, labels=categories, autopct="%1.1f%%")
plt.legend(title="Departments", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Pie Chart")
plt.show()
