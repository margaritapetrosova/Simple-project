import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
train_url="http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train=pd.read_csv(train_url)
test_url="http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test=pd.read_csv(test_url)
print("****Train_Set****")
print(train.describe())
print("\n")
print("****Test_Set****")
print(test.describe())
print(test.columns.values)
print(train.isna().head())
print(train.isna().sum())
print(test.isna().head())
print(test.isna().sum())
train.fillna(train.mean(),inplace=True)
test.fillna(test.mean(),inplace=True)

print(train[['Pclass','Survived']].groupby(['Pclass'],
                                           as_index=False).mean().sort_values
                                        (by='Survived',ascending=False))
print(train[['Sex','Survived']].groupby(['Sex'],
                                        as_index=False).mean().sort_values
                                        (by='Survived',ascending=False))
print(train[['SibSp','Survived']].groupby(['SibSp'],
                                          as_index=False).mean().sort_values
                                        (by='Survived',ascending=False))
train.plot()
test.plot()
plt.show()
train.info()
train=train.drop(['Name','Ticket','Cabin','Embarked'], axis=1)
test=test.drop(['Name','Ticket','Cabin','Embarked'], axis=1)
print('COLUMNS', test.columns.values)
labelEncoder=LabelEncoder()
labelEncoder.fit(train['Sex'])
labelEncoder.fit(test['Sex'])
train['Sex']=labelEncoder.transform(train['Sex'])
test['Sex']=labelEncoder.transform(test['Sex'])
train.info()
X=np.array(train.drop(['Survived'],1).astype(float))
y=np.array(train['Survived'])
kmeans=KMeans(n_clusters=2)
kmeans.fit(X)
correct=0
for i in range(len(X)):
    predict_me=np.array(X[i].astype(float))
    predict_me=predict_me.reshape(-1,len(predict_me))
    prediction=kmeans.predict(predict_me)
    if prediction[0]==y[i]:
        correct+=1
print(correct/len(X))
kmeans=KMeans(n_clusters=2, max_iter=600, algorithm='auto')