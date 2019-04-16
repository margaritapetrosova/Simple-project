weather=['Sunny','Sunny','Overcast','Rainy','Rainy',
         'Rainy','Overcast','Sunny','Sunny','Rainy',
         'Sunny','Overcast','Overcast','Rainy']
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool',
      'Mild','Cool','Mild','Mild',
      'Mild','Hot','Mild']
play=['Yes','No','Yes','Yes','Yes','No','Yes','No','Yes',
      'Yes','Yes','Yes','Yes','No']
print(len(weather))
print(len(temp))
print(len(play))
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
weather_encoded=le.fit_transform(weather)
print('weather:', weather_encoded)
temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
print('temp:', temp_encoded)
play_encoded=le.fit_transform(temp)
print('play:', label)
features=list(zip(weather_encoded,temp_encoded))
print('weather&temp', features)
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(features,label)
predicted=model.predict([[0,2]])
print('Predicted Value:', predicted)

from sklearn import datasets
wine=datasets.load_wine()
print('Features:', wine.feature_names)
print('Labels', wine.target_names)
print(wine.data.shape)
print('first 7:', wine.data[0:7])
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(wine.data, wine.target, test_size=0.3,random_state=109)
from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()
gnb.fit(X_train,y_train)
y_pred=gnb.predict(X_test)
from sklearn import metrics
print('Accuracy:',metrics.accuracy_score(y_test,y_pred))
