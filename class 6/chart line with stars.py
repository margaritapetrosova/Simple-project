import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot([1,2,3,4],[10,20,25,30],color='green', linewidth=2)
ax.scatter([0.9, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='blue', marker='*',linewidths=3)
ax.set_xlim(0.5, 4.5)
plt.show()