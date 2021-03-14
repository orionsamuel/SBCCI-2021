import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import RepeatedKFold, train_test_split

def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

dados = pd.read_csv("4x4_norm.csv")

X = dados.iloc[:,:-1].values
target = dados.iloc[:,-1].values

X_train, X_test, target_train, target_test = train_test_split(
    X, target, test_size = 0.3, random_state = 1)

knn = KNeighborsRegressor(n_neighbors=3, metric='euclidean')
knn.fit(X_train, target_train)
target_pred = knn.predict(X_test)
err = str(mean_absolute_percentage_error(target_test, target_pred))
print("Erro MAPE: ", err)
print(target_test)
print(target_pred)
