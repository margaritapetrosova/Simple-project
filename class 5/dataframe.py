import pandas as pd
lst={'Name':['Mar','Arpi','Tigran','Levon',
     'David','Ani','Mari'],
     'Score':[50,60,34,80,
      34,53,76]}

df2=pd.DataFrame(lst,index=['1','2','3','4',
                            '5','6','7'])
row2=df2.iloc[3]
print('row2:', row2)

print(df2)
print(df2.loc[['2','4']])
print('sum:', df2.iloc[:,1].sum())
df2.to_csv('task1.csv')