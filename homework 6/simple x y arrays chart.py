import matplotlib.pyplot as plt
import numpy as np

x = np.array([2, 3, 2, 3])
y = np.array([4, 2, 6, 7])
plt.plot(x, y, label='chart', color='red')
plt.show()
plt.legend()