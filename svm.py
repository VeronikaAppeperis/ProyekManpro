import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#STEP 1: DATA READING AND UNDERSTANDING

df = pd.read_csv("big_startup.csv")


df.drop('category_list', axis=1, inplace=True)
df.drop('funding_total_usd', axis=1, inplace=True)
df.drop('status', axis=1, inplace=True)
df.drop('country_code', axis=1, inplace=True)
df.drop('category_funding', axis=1, inplace=True)
#print(df.head())
Y = df['statusKey'].values
Y=Y.astype('int')
X=df.drop(labels=['statusKey'], axis=1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=20)

from sklearn.svm import LinearSVC
svc=LinearSVC()
svc.fit(X_train,y_train)
prediction_test = svc.predict(X_test)
print(svc.score(X_test,y_test))
#from sklearn import metrics
#print("Accuracy = ", metrics.accuracy_score(y_test, prediction_test))

