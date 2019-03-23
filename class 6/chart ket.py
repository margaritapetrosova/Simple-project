import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure(figsize=(7,7))
ax=fig.add_subplot(111)
ax.scatter(np.linspace(1, 2, 6), np.linspace(0, 5, 6))
plt.show()