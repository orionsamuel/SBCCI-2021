import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor
from sklearn.model_selection import RepeatedKFold, train_test_split

def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

dados = pd.read_csv("4x4.csv")

X = dados.iloc[:,:-1].values
target = dados.iloc[:,-1].values

X_train, X_test, target_train, target_test = train_test_split(
    X, target, test_size = 0.3, random_state = 1)


r1 = LinearRegression()
r2 = DecisionTreeRegressor()

er = VotingRegressor([r1, r2])

er.fit(X_train, target_train)

target_pred = er.predict(X_test)

err = str(mean_absolute_percentage_error(target_test, target_pred))

print("Erro MAPE: ", err)
print("Teste")
print(target_test)
print("Predição")
print(target_pred)
