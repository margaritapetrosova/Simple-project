import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
pdf_file = PdfPages('results.pdf')
fig2=plt.figure()
x = np.array([2, 4, 2, 2.5, 1])
plt.plot(x, label='chart',color='green', marker='o', linestyle='dashed')
plt.legend()
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot([1,2,3,4],[10,20,25,30],color='red', linewidth=2)
ax.scatter([0.9, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='blue', marker='1',linewidth=10)
ax.set_xlim(0.5, 4.5)
pdf_file.savefig(fig)
pdf_file.savefig(fig2)
pdf_file.close()