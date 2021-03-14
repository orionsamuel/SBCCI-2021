import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import RepeatedKFold

def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

dados = pd.read_csv('4x4_latency_train.csv')

X = dados.iloc[:,:-1].values
target = dados.iloc[:,-1].values

rkf = RepeatedKFold(n_splits=10, n_repeats=10, random_state=990)

for train, test in rkf.split(X, target):
    X_train = X[train]
    X_test = X[test]
    target_train = target[train]
    target_test = target[test]

regressor = Sequential()
regressor.add(Dense(units = 4145, activation = 'relu', input_shape=(X.shape[1], )))
regressor.add(Dense(units = 4145, activation = 'relu'))
regressor.add(Dense(units = 1, activation = 'linear'))
regressor.compile(loss = 'mean_absolute_error', optimizer = 'adam',
                  metrics = ['mean_absolute_error'])
regressor.fit(X, target, batch_size = 300, epochs = 100)

target_pred = regressor.predict(X_test)

err = str(mean_absolute_percentage_error(target_test, target_pred))

print("Erro MAPE: ", err)
print("Média target: ", target.mean())
print("Média previsões: ", target_pred.mean())




















