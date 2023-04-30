import matplotlib.pyplot as plt
import numpy as np

# Define the range of x values
x = np.linspace(-10, 10, 100)

# Define the equation for the parabolic curve
y = x ** 2

# Plot the curve
plt.plot(x, y)

# Add labels and a title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Parabolic Curve')

# Show the plot
plt.show()
