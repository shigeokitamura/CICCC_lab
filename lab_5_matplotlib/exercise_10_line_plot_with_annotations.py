import matplotlib.pyplot as plt

# Data
x = range(0, 20)
y = [value ** 2 for value in x]

# Plotting
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot with Annotations")
plt.annotate("Lowest Point", xy=(min(x), min(y)), xytext=(min(x) + 2, min(y)), arrowprops=dict(facecolor='blue', shrink=0.05))
plt.annotate("Highest Point", xy=(max(x), max(y)), xytext=(max(x) - 7, max(y)), arrowprops=dict(facecolor='red', shrink=0.05))
plt.show()
