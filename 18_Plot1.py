import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**2 + 2*x - 3

# Generate x values
x = np.linspace(-10, 10, 100)  # 100 points between -10 and 10
y = f(x)

# Scatter points
x_scatter = np.arange(-10, 11, 1)  # Integer points from -10 to 10
y_scatter = f(x_scatter)

# Plot the curve
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Curve (y = x^2 + 2x - 3)", color="blue", linewidth=2)

# Plot the scatter points
plt.scatter(x_scatter, y_scatter, color="red", label="Scatter Points")

# Add labels, legend, and title
plt.title("Plot of y = x^2 + 2x - 3", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Add x-axis
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Add y-axis
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
