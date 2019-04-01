import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
bankdata=pd.read_csv("100 Sales Records.csv")
print(bankdata.shape)
print(bankdata.head())
print(bankdata.tail())
X=bankdata.drop('Total Profit',axis=1)
Y=bankdata['Total Profit']
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.20)
from sklearn.svm import SVC
svclassifier=SVC(kernel='linear')
svclassifier.fit(X_train, Y_train)
y_pred=svclassifier.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix
print("conf matr", confusion_matrix(Y_test, y_pred))
print("class report", classification_report(Y_test, y_pred))