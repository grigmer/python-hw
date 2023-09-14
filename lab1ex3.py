import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-6, 6, 0.1)
y = np.floor((np.sin(x)**2)/(1.1**(2*x)))
plt.plot(x, y)
plt.show()