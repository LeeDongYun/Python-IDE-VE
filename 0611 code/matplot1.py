import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(10)
print(x)
plt.plot(x)
plt.show()

x = np.linspace(0.0, 10.0, 1000)

plt.plot(x, x*x)
plt.plot(x, x**3)
plt.title('A simple graph')
plt.legend(['y = x * x', 'y = x * x * x'], loc='upper left')
plt.show()