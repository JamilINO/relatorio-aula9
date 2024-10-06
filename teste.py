import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) Axes.
plt.plot(x, x * ( x * 9), label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x labe')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()