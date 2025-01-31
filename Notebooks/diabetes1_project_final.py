# -*- coding: utf-8 -*-
"""diabetes1_Project_final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Wn5ivyt_Rnl9XZB0BfgZwJR1WaFuVokT

# **Data Preprocessing**
"""

import pandas as pd
import numpy as py

df = pd.read_csv('diabetes_cleaned_final.csv')

df.shape

df.head()

df.tail()

df.info()

df.describe()

df.describe().T

"""# **Histogram For All Columns**"""

p = df.hist(figsize = (20,20))

"""# **value counts of have_diabetes**"""

color_wheel = {1: "#0392cf",
               2: "#7bc043"}
colors = df["have_diabetes"].map(lambda x: color_wheel.get(x + 1))
print(df.have_diabetes.value_counts())
p=df.have_diabetes.value_counts().plot(kind="bar")

import seaborn as sns
corrmat=df.corr()
sns.heatmap(corrmat, annot=True, linewidths=0.4, fmt='.2g', annot_kws={'size': 7})

"""# **Scaling the data**"""

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


X = df.drop(columns=["have_diabetes"])
y = df["have_diabetes"] -1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


X_train_scaled = pd.DataFrame(X_train_scaled, columns=X.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X.columns)

"""#1- KNN
#2- Naive Bayes
#3- SVM
#4- Decision Tree
#5- Random Forest
#6- Logistic Regression
#7- XGBoost

# **1 -  K Nearest Neighbours**
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import GridSearchCV

#List Hyperparameters to tune
knn= KNeighborsClassifier()
n_neighbors = list(range(15,25))
p=[1,2]
weights = ['uniform', 'distance']
metric = ['euclidean', 'manhattan', 'minkowski']

#convert to dictionary
hyperparameters = dict(n_neighbors=n_neighbors, p=p,weights=weights,metric=metric)

#Making model
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
grid_search = GridSearchCV(estimator=knn, param_grid=hyperparameters, n_jobs=-1, cv=cv, scoring='f1',error_score=0)

best_model = grid_search.fit(X_train_scaled,y_train)

train_accuracy = best_model.score(X_train_scaled, y_train)


test_accuracy = best_model.score(X_test_scaled, y_test)

print(f"Training Accuracy: {train_accuracy:.2f}")
print(f"Testing Accuracy: {test_accuracy:.2f}")

if train_accuracy - test_accuracy > 0.1:
    print("The model might be overfitting!")

#Best Hyperparameters Value
print('Best leaf_size:', best_model.best_estimator_.get_params()['leaf_size'])
print('Best p:', best_model.best_estimator_.get_params()['p'])
print('Best n_neighbors:', best_model.best_estimator_.get_params()['n_neighbors'])

#Predict testing set
knn_pred = best_model.predict(X_test_scaled)

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

rf_probabilities = best_model.predict_proba(X_test_scaled)[:, 1]

roc_auc = roc_auc_score(y_test, rf_probabilities)
print(f"ROC-AUC: {roc_auc:.2f}")


fpr, tpr, thresholds = roc_curve(y_test, rf_probabilities)


plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.title('ROC Curve', fontsize=14)
plt.xlabel('False Positive Rate (FPR)', fontsize=12)
plt.ylabel('True Positive Rate (TPR)', fontsize=12)
plt.legend(loc='lower right')
plt.grid()
plt.show()

print("Classification Report is:\n",classification_report(y_test,knn_pred))
print("\n F1:\n",f1_score(y_test,knn_pred))
print("\n Precision score is:\n",precision_score(y_test,knn_pred))
print("\n Recall score is:\n",recall_score(y_test,knn_pred))
print("\n Confusion Matrix:\n")
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, knn_pred),
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['No Diabetes', 'Diabetes'],
    yticklabels=['No Diabetes', 'Diabetes']
)
plt.title('Confusion Matrix', fontsize=14)
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.show()

"""# **2 Naive Bayes**"""

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV

param_grid_nb = {
    'var_smoothing': np.logspace(0,-2, num=100)
}
nbModel_grid = GridSearchCV(estimator=GaussianNB(), param_grid=param_grid_nb, verbose=1, cv=10, n_jobs=-1)

best_model= nbModel_grid.fit(X_train_scaled, y_train)

nb_pred=best_model.predict(X_test_scaled)

train_accuracy = best_model.score(X_train_scaled, y_train)


test_accuracy = best_model.score(X_test_scaled, y_test)

print(f"Training Accuracy: {train_accuracy:.2f}")
print(f"Testing Accuracy: {test_accuracy:.2f}")

if train_accuracy - test_accuracy > 0.1:
    print("The model might be overfitting!")

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

rf_probabilities = best_model.predict_proba(X_test_scaled)[:, 1]

roc_auc = roc_auc_score(y_test, rf_probabilities)
print(f"ROC-AUC: {roc_auc:.2f}")


fpr, tpr, thresholds = roc_curve(y_test, rf_probabilities)


plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.title('ROC Curve', fontsize=14)
plt.xlabel('False Positive Rate (FPR)', fontsize=12)
plt.ylabel('True Positive Rate (TPR)', fontsize=12)
plt.legend(loc='lower right')
plt.grid()
plt.show()

print("Classification Report is:\n",classification_report(y_test,nb_pred))
print("\n F1:\n",f1_score(y_test,nb_pred))
print("\n Precision score is:\n",precision_score(y_test,nb_pred))
print("\n Recall score is:\n",recall_score(y_test,nb_pred))
print("\n Confusion Matrix:\n")
plt.figure(figsize=(6, 4))
sns.heatmap(
    confusion_matrix(y_test, nb_pred),
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['No Diabetes', 'Diabetes'],
    yticklabels=['No Diabetes', 'Diabetes']
)
plt.title('Confusion Matrix', fontsize=14)
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.show()

"""# **3 Support Vector Machine**"""

from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import f1_score, precision_score, recall_score

model = SVC(probability=True)
kernel = ['poly', 'rbf', 'sigmoid']
C = [50, 10, 1.0, 0.1, 0.01]
gamma = ['scale']

# define grid search
grid = dict(kernel=kernel,C=C,gamma=gamma)
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
grid_search = GridSearchCV(estimator=model, param_grid=grid, n_jobs=-1, cv=cv, scoring='f1',error_score=0)

grid_result = grid_search.fit(X_train_scaled, y_train)

svm_pred=grid_result.predict(X_test_scaled)

y_pred_proba = grid_result.predict_proba(X_test_scaled)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
roc_auc = roc_auc_score(y_test, y_pred_proba)


plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

train_accuracy = grid_result.score(X_train_scaled, y_train)


test_accuracy = grid_result.score(X_test_scaled, y_test)

print(f"Training Accuracy: {train_accuracy:.2f}")
print(f"Testing Accuracy: {test_accuracy:.2f}")

if train_accuracy - test_accuracy > 0.1:
    print("The model might be overfitting!")

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score
import seaborn as sns


print("Classification Report is:\n",classification_report(y_test,svm_pred))
print("\n F1:\n",f1_score(y_test,svm_pred))
print("\n Precision score is:\n",precision_score(y_test,svm_pred))
print("\n Recall score is:\n",recall_score(y_test,svm_pred))
print("\n Confusion Matrix:\n")
plt.figure(figsize=(6, 4))
sns.heatmap(
    confusion_matrix(y_test, svm_pred),
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['No Diabetes', 'Diabetes'],
    yticklabels=['No Diabetes', 'Diabetes']
)
plt.title('Confusion Matrix', fontsize=14)
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.show()

#save model
import pickle
filename = 'finalized_model.sav'
pickle.dump(grid_result, open(filename, 'wb'))

"""# **4 Decision Tree**"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import GridSearchCV
dt = DecisionTreeClassifier(random_state=42)

# Create the parameter grid based on the results of random search
params = {
    'max_depth': [5, 10, 20,25],
    'min_samples_leaf': [10, 20, 50, 100,120],
    'criterion': ["gini", "entropy"]
}

grid_search = GridSearchCV(estimator=dt,
                           param_grid=params,
                           cv=4, n_jobs=-1, verbose=1, scoring = "accuracy")

best_model=grid_search.fit(X_train_scaled, y_train)

dt_pred=best_model.predict(X_test_scaled)

train_accuracy = best_model.score(X_train_scaled, y_train)


test_accuracy = best_model.score(X_test_scaled, y_test)

print(f"Training Accuracy: {train_accuracy:.2f}")
print(f"Testing Accuracy: {test_accuracy:.2f}")

if train_accuracy - test_accuracy > 0.1:
    print("The model might be overfitting!")

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

rf_probabilities = best_model.predict_proba(X_test_scaled)[:, 1]

roc_auc = roc_auc_score(y_test, rf_probabilities)
print(f"ROC-AUC: {roc_auc:.2f}")


fpr, tpr, thresholds = roc_curve(y_test, rf_probabilities)


plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.title('ROC Curve', fontsize=14)
plt.xlabel('False Positive Rate (FPR)', fontsize=12)
plt.ylabel('True Positive Rate (TPR)', fontsize=12)
plt.legend(loc='lower right')
plt.grid()
plt.show()

print("Classification Report is:\n",classification_report(y_test,dt_pred))
print("\n F1:\n",f1_score(y_test,dt_pred))
print("\n Precision score is:\n",precision_score(y_test,dt_pred))
print("\n Recall score is:\n",recall_score(y_test,dt_pred))
print("\n Confusion Matrix:\n")
plt.figure(figsize=(6, 4))
sns.heatmap(
    confusion_matrix(y_test, dt_pred),
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['No Diabetes', 'Diabetes'],
    yticklabels=['No Diabetes', 'Diabetes']
)
plt.title('Confusion Matrix', fontsize=14)
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.show()

"""# **5 Random Forest**"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV

# define models and parameters
model = RandomForestClassifier()
n_estimators = [1800]
max_features = ['sqrt', 'log2']

# define grid search
grid = dict(n_estimators=n_estimators,max_features=max_features)
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
grid_search = GridSearchCV(estimator=model, param_grid=grid, n_jobs=-1, cv=cv, scoring='accuracy',error_score=0)

best_model = grid_search.fit(X_train_scaled, y_train)

rf_pred=best_model.predict(X_test_scaled)

train_accuracy = best_model.score(X_train_scaled, y_train)


test_accuracy = best_model.score(X_test_scaled, y_test)

print(f"Training Accuracy: {train_accuracy:.2f}")
print(f"Testing Accuracy: {test_accuracy:.2f}")

if train_accuracy - test_accuracy > 0.1:
    print("The model might be overfitting!")

print("Classification Report is:\n",classification_report(y_test,rf_pred))
print("\n F1:\n",f1_score(y_test,rf_pred))
print("\n Precision score is:\n",precision_score(y_test,rf_pred))
print("\n Recall score is:\n",recall_score(y_test,rf_pred))
print("\n Confusion Matrix:\n")
plt.figure(figsize=(6, 4))
sns.heatmap(
    confusion_matrix(y_test, rf_pred),
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['No Diabetes', 'Diabetes'],
    yticklabels=['No Diabetes', 'Diabetes']
)
plt.title('Confusion Matrix', fontsize=14)
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.show()

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

rf_probabilities = best_model.predict_proba(X_test_scaled)[:, 1]

roc_auc = roc_auc_score(y_test, rf_probabilities)
print(f"ROC-AUC: {roc_auc:.2f}")


fpr, tpr, thresholds = roc_curve(y_test, rf_probabilities)


plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.title('ROC Curve', fontsize=14)
plt.xlabel('False Positive Rate (FPR)', fontsize=12)
plt.ylabel('True Positive Rate (TPR)', fontsize=12)
plt.legend(loc='lower right')
plt.grid()
plt.show()

"""# **6 - Logistic Regression**"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import f1_score, precision_score, recall_score,accuracy_score

reg = LogisticRegression()
reg.fit(X_train_scaled,y_train)

lr_pred=reg.predict(X_test_scaled)

train_accuracy = reg.score(X_train_scaled, y_train)


test_accuracy = reg.score(X_test_scaled, y_test)

print(f"Training Accuracy: {train_accuracy:.2f}")
print(f"Testing Accuracy: {test_accuracy:.2f}")

if train_accuracy - test_accuracy > 0.1:
    print("The model might be overfitting!")

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

rf_probabilities = reg.predict_proba(X_test_scaled)[:, 1]

roc_auc = roc_auc_score(y_test, rf_probabilities)
print(f"ROC-AUC: {roc_auc:.2f}")


fpr, tpr, thresholds = roc_curve(y_test, rf_probabilities)


plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.title('ROC Curve', fontsize=14)
plt.xlabel('False Positive Rate (FPR)', fontsize=12)
plt.ylabel('True Positive Rate (TPR)', fontsize=12)
plt.legend(loc='lower right')
plt.grid()
plt.show()

print("Classification Report is:\n",classification_report(y_test,lr_pred))
print("\n F1:\n",f1_score(y_test,lr_pred))
print("\n Precision score is:\n",precision_score(y_test,lr_pred))
print("\n Recall score is:\n",recall_score(y_test,lr_pred))
print("\n Confusion Matrix:\n")
plt.figure(figsize=(6, 4))
sns.heatmap(
    confusion_matrix(y_test, lr_pred),
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['No Diabetes', 'Diabetes'],
    yticklabels=['No Diabetes', 'Diabetes']
)
plt.title('Confusion Matrix', fontsize=14)
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.show()

"""# **7 - XGBoost**"""

!pip install xgboost

from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, f1_score, precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns


xgb_model = XGBClassifier(
    random_state=42,
    use_label_encoder=False,
    eval_metric='logloss',
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8
)


xgb_model.fit(X_train_scaled, y_train)


xg_pred = xgb_model.predict(X_test_scaled)

print("Classification Report is:\n", classification_report(y_test, xg_pred))
print("\n F1:\n", f1_score(y_test, xg_pred))
print("\n Precision score is:\n", precision_score(y_test, xg_pred))
print("\n Recall score is:\n", recall_score(y_test, xg_pred))


plt.figure(figsize=(6, 4))
sns.heatmap(
    confusion_matrix(y_test, xg_pred),
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['No Diabetes', 'Diabetes'],
    yticklabels=['No Diabetes', 'Diabetes']
)
plt.title('Confusion Matrix', fontsize=14)
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.show()

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

rf_probabilities = xgb_model.predict_proba(X_test_scaled)[:, 1]

roc_auc = roc_auc_score(y_test, rf_probabilities)
print(f"ROC-AUC: {roc_auc:.2f}")


fpr, tpr, thresholds = roc_curve(y_test, rf_probabilities)


plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.title('ROC Curve', fontsize=14)
plt.xlabel('False Positive Rate (FPR)', fontsize=12)
plt.ylabel('True Positive Rate (TPR)', fontsize=12)
plt.legend(loc='lower right')
plt.grid()
plt.show()