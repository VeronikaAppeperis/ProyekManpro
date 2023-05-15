import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score,precision_score,recall_score, confusion_matrix, ConfusionMatrixDisplay,classification_report

#STEP 1: DATA READING AND UNDERSTANDING

df = pd.read_csv("Data.csv")


drop_columns = ["permalink","name","homepage_url","category_list","funding_total_usd","status", "country_code",
                "state_code","region","city","founded_at","first_funding_at","last_funding_at",
                "category_funding","CountryKey","stateKey","funding_rounds"]
df.drop(labels=drop_columns, axis=1, inplace=True)
#print(df.head())
Y = df['statusKey'].values
Y=Y.astype('int')
X=df.drop(labels=['statusKey'], axis=1)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=30)

from sklearn.svm import SVC
from sklearn.svm import LinearSVC
model = SVC(C=7,random_state=30)
model.fit(X_train, y_train)

prediction_test = model.predict(X_test)
print(X_test)
cm=confusion_matrix(y_test,prediction_test)
print(cm)
print("Accuracy: ",accuracy_score(y_test,prediction_test))
print("precision = ", precision_score(y_test, prediction_test))
print("recall = ", recall_score(y_test, prediction_test))
tp, fn, fp, tn = cm.ravel()
specificity = tn / (tn + fp)
print("Specificity:", specificity)
print(classification_report(y_test, prediction_test))


# hitung specificity


# feature_list=list(X.columns)
# feature_imp=pd.Series(svc.feature_importances_,index=feature_list).sort_values(ascending=False)
# print(feature_imp)
# accuracy = accuracy_score(y_test, prediction_test)
# precision = precision_score(y_test, prediction_test,pos_label='positive',average='micro')
# recall = recall_score(y_test, prediction_test,pos_label='positive',average='micro')

# print("Accuracy:", accuracy)
# print("Precision:", precision)
# print("Recall:", recall)
from sklearn import metrics
print("Accuracy = ", metrics.accuracy_score(y_test, prediction_test))
from sklearn.model_selection import GridSearchCV
  
# defining parameter range
# param_grid = {'C': [0.1, 1, 10, 100, 1000], 
#               'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
#               'kernel': ['rbf']} 
  
# grid = GridSearchCV(SVC(), param_grid, refit = True, verbose = 3)
  
# fitting the model for grid search
# grid.fit(X_train, y_train)
# print best parameter after tuning
# print(grid.best_params_)

# print how our model looks after hyper-parameter tuning
#print(grid.best_estimator_)
