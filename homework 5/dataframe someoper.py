import pandas as pd
list={'Name':['Mar','Arus','Vard','Zara',
     'Rafi','Liana','Sarkis'],
     'Language':['Geo','Eng','Ru','Arm',
      'Ar','Ger','Tur']}
df2=pd.DataFrame(list,index=['1','2','3','4',
                            '5','6','7'])
print(df2)
print(df2.loc[['2','4']])

print(df2.keys())
print(df2.product())