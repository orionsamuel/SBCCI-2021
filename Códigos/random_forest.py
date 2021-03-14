import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RepeatedKFold


def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


dados = pd.read_csv("4x4_latency_train.csv")

X = dados.iloc[:,:-1].values
target = dados.iloc[:,-1].values

rkf = RepeatedKFold(n_splits=10, n_repeats=10, random_state=990)

for train, test in rkf.split(X, target):
    X_train = X[train]
    X_test = X[test]
    target_train = target[train]
    target_test = target[test]


regr = RandomForestRegressor(criterion='mae', max_depth=2, random_state=0)

regr.fit(X_train, target_train)

target_pred = regr.predict(X_test)

err = str(mean_absolute_percentage_error(target_test, target_pred))

print("Erro MAPE: ", err)
print("Teste")
print(target_test)
print("Predição")
print(target_pred)
