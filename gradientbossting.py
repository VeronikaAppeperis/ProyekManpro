# import library
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score,classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split

# load dataset
df = pd.read_csv("data.csv")

# pisahkan antara fitur dan target
drop_columns = ["permalink","name","homepage_url","category_list","funding_total_usd","status",
                "country_code","state_code", "region","city","funding_rounds","founded_at", 
                "first_funding_at","last_funding_at","category_funding","stateKey","CountryKey"]
df.drop(labels=drop_columns, axis=1, inplace=True)
X = df.drop('statusKey',axis=1).copy()
y = df['statusKey'].copy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=30,stratify=y)

# buat model Gradient Boosting
model = GradientBoostingClassifier(n_estimators=310, learning_rate=0.5, max_features=2, max_depth=7, random_state=30)
model.fit(X_train, y_train)
predictions = model.predict(X)

print("Confusion Matrix:")
cm = confusion_matrix(y, predictions)
print(cm)

print("Classification Report")
print(classification_report(y, predictions))
feature_list=list(X.columns)
feature_imp=pd.Series(model.feature_importances_,index=feature_list).sort_values(ascending=False)
print(feature_imp)
print("accuracy ", accuracy_score(y, predictions))
print("precision ", precision_score(y, predictions))
print("recall ", recall_score(y, predictions))
# hitung specificity
tp, fn, fp, tn = cm.ravel()

specificity = tn / (tn + fp)
# import library
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score,classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split

# load dataset
df = pd.read_csv("data.csv")

# pisahkan antara fitur dan target
drop_columns = ["permalink","name","homepage_url","category_list","funding_total_usd","status",
                "country_code","state_code", "region","city","funding_rounds","founded_at", 
                "first_funding_at","last_funding_at","category_funding","stateKey","CountryKey"]
df.drop(labels=drop_columns, axis=1, inplace=True)
X = df.drop('statusKey',axis=1).copy()
y = df['statusKey'].copy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=30,stratify=y)

# buat model Gradient Boosting
model = GradientBoostingClassifier(n_estimators=310, learning_rate=0.5, max_features=2, max_depth=7, random_state=30)
model.fit(X_train, y_train)
predictions = model.predict(X)

print("Confusion Matrix:")
cm = confusion_matrix(y, predictions)
print(cm)

print("Classification Report")
print(classification_report(y, predictions))
feature_list=list(X.columns)
feature_imp=pd.Series(model.feature_importances_,index=feature_list).sort_values(ascending=False)
print(feature_imp)
print("accuracy ", accuracy_score(y, predictions))
print("precision ", precision_score(y, predictions))
print("recall ", recall_score(y, predictions))
# hitung specificity
tp, fn, fp, tn = cm.ravel()

specificity = tn / (tn + fp)

print("Specificity:", specificity)