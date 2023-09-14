import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-100, 100, 0.1)
plt.plot(x,((x**3 - 4)/((x-1)**3)))
plt.show()
print('По графику видно, что 1 - точка максимума (больше экстремумов нет).')