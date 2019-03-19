import pandas as pd
import matplotlib.pyplot as plt
list={'Name':['Mar','Arus','Vard','Zara',
     'Rafi','Liana','Sarkis'],
     'Productivity':[50,26,34,54,
      65,23,43]}
df2=pd.DataFrame(list,index=['1','2','3','4',
                            '5','6','7'])
print(df2)
df2.plot(color='green',marker='o', linestyle='dashed')
plt.show()