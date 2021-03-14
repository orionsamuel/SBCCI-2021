import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import RepeatedKFold

def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

dados = pd.read_csv("16x16_latency_train.csv")

X = dados.iloc[:,:-1].values
target = dados.iloc[:,-1].values

rkf = RepeatedKFold(n_splits=10, n_repeats=10, random_state=990)

for train, test in rkf.split(X, target):
    X_train = X[train]
    X_test = X[test]
    target_train = target[train]
    target_test = target[test]

mlp = MLPRegressor(activation='identity', solver='lbfgs', momentum=0.8, hidden_layer_sizes=(300),
                    learning_rate='constant', learning_rate_init=0.001,
                    max_iter=5000, random_state=1)

mlp.fit(X_train, target_train)

target_pred = mlp.predict(X_test)

err = str(mean_absolute_percentage_error(target_test, target_pred))

print("Erro MAPE: ", err)
