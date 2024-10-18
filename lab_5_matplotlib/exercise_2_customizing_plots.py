import matplotlib.pyplot as plt

# Data
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]

# Plotting
plt.plot(x, y, color="green", linestyle="--", marker="o")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Customized Line Plot")
plt.grid(True)
plt.show()
