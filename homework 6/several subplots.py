import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure(figsize=(10,8))
ax1=fig.add_subplot(231)
ax1.set(title="Chart", xlabel="x",ylabel="y")
ax2=fig.add_subplot(232)
ax3=fig.add_subplot(235)
ax4=fig.add_subplot(234)
ax1.bar([1, 2, 3], [3, 4, 5])
ax2.plot([1,2,3,4],[9,12,15,32],linewidth=2)
ax3.plot(np.array([1.6, 0.5, 1.6, 0.5, 1.6]))
ax3.set_ylim(-2.5, 2.5)
ax4.plot([9,20,27,32], [1,2,3,4],linewidth=2)
plt.show()
