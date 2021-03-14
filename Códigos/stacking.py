import pandas as pd
import numpy as np
from sklearn.ensemble import StackingRegressor
from sklearn.linear_model import RidgeCV
from sklearn.svm import LinearSVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RepeatedKFold, train_test_split

def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

dados = pd.read_csv("4x4.csv")

X = dados.iloc[:,:-1].values
target = dados.iloc[:,-1].values

X_train, X_test, target_train, target_test = train_test_split(
    X, target, test_size = 0.3, random_state = 1)

estimators = [('lr', RidgeCV()), ('svr', LinearSVR(random_state=42))]

regr = StackingRegressor(estimators=estimators,
                         final_estimator=RandomForestRegressor(n_estimators=10,
                                                               random_state=42))


regr.fit(X_train, target_train)

target_pred = regr.predict(X_test)

err = str(mean_absolute_percentage_error(target_test, target_pred))

print("Erro MAPE: ", err)
print("Teste")
print(target_test)
print("Predição")
print(target_pred)
