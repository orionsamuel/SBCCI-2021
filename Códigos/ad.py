import pandas as pd
import numpy as np
import random
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import RepeatedKFold, train_test_split

def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

error = []
instancias = []

dados = pd.read_csv("4x4_latency_train.csv")

X = dados.iloc[:,:-1].values
target = dados.iloc[:,-1].values

for i in range(10):
    rand = random.randint(1,1000)
    rkf = RepeatedKFold(n_splits=10, n_repeats=10, random_state=990)

    for train, test in rkf.split(X, target):
        X_train = X[train]
        X_test = X[test]
        target_train = target[train]
        target_test = target[test]

    ad = DecisionTreeRegressor(criterion='friedman_mse', max_depth=10,
                               random_state=rand, min_impurity_decrease=37.9)

    ad.fit(X_train, target_train)

    target_pred = ad.predict(X_test)

    error.append(mean_absolute_percentage_error(target_test, target_pred))

for i in range(len(target_test)):
    instancias.append(i) 

print("Média Erro MAPE: ", np.mean(error))
print("Desvio Padrão Erro Mape: ", np.std(error))
