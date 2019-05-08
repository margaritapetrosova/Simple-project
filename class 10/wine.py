import pandas as pd
white=pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=';')
red=pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';')
print(white.info())
print(red.info())
print(white.head())
import matplotlib.pyplot as plt
fig, ax=plt.subplots(1, 2)
ax[0].hist(red.alcohol, 10, facecolor='red',
           alpha=0.5,label="Red wine")
ax[1].hist(white.alcohol, 10, facecolor='white',
           ec='black', lw=0.5, alpha=0.5,label="White wine")
fig.subplots_adjust(left=0, right=1, bottom=0, top=0.5, hspace=0.05, wspace=1)
ax[0].set_ylim([0,1000])
ax[0].set_xlabel("alcohol in % vol")
ax[0].set_ylabel("Frequency")
ax[1].set_xlabel("Alcohol in%Vol")
ax[1].set_ylabel("Frequency")
fig.suptitle("Distribution of Alcohol in %Vol")
plt.show()

import matplotlib.pyplot as plt
fig, ax=plt.subplots(1, 2, figsize=(8,4))
ax[0].scatter(red['quality'], red["sulphates"], color="red")
ax[1].scatter(white['quality'], white["sulphates"], color="white", edgecolors="black", lw=0.5)
ax[0].set_title("Red Wine")
ax[1].set_title("White Wine")
ax[0].set_xlabel("Quality")
ax[1].set_xlabel("Quality")

ax[0].set_ylabel("Sulphates")
ax[1].set_ylabel("Sulphates")
ax[0].set_xlim([0,10])
ax[1].set_xlim([0,10])
ax[0].set_ylim([0,2.5])
ax[1].set_ylim([0,2.5])
fig.subplots_adjust(wspace=0.5)
fig.subplots("Wine Quality by Amount of Sulphates")
plt.show()

red['type']=1
white['type']=0
wines=red.append(white,ignore_index=True)
red['type']=1
white['type']=0
wines=red.append(white,ignore_index=True)
import numpy as np
from sklearn.model_selection import train_test_split
X=wines.ix[:,0:11]
y=np.ravel(wines.type)
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.33,random_state=42)
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler().fit(X_train)
X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)
