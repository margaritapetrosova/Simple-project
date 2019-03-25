import matplotlib.pyplot as plt
import numpy as np

x = np.array([2, 3, 4, 3])
plt.plot(x, label='chart',color='green', marker='o', linestyle='dashed')
plt.legend()
plt.savefig("chartt.png")