import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-15,15,0.1)

y = x**3 + 1

plt.plot(x, y)
plt.show()