import pandas as pd
import numpy as np
import random
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import RepeatedKFold, train_test_split

def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


error = []
instancias = []

dados = pd.read_csv("8x8_latency_train.csv")

X = dados.iloc[:,:-1].values
target = dados.iloc[:,-1].values

for i in range(10):
    rand = random.randint(1,1000)
    rkf = RepeatedKFold(n_splits=10, n_repeats=10, random_state=rand)

    for train, test in rkf.split(X, target):
        X_train = X[train]
        X_test = X[test]
        target_train = target[train]
        target_test = target[test]

    ad = DecisionTreeRegressor(criterion='friedman_mse', random_state=rand)


    ad.fit(X_train, target_train)

    target_pred = ad.predict(X_test)

    error.append(mean_absolute_percentage_error(target_test, target_pred))

for i in range(len(target_test)):
    instancias.append(i) 

plt.title("Mapping by Latency - 8x8")
plt.ylabel("Latency (Log Scale)")
plt.xlabel("Instancies")
plt.yscale('log')

plt.plot(instancias, target_test, color='red', label ='Real')
plt.plot(instancias, target_pred, color='purple', label ='Predict')
plt.legend(loc = 'upper right')
plt.savefig("latency_8x8.png")


saida = open('result_latency_8x8.txt', 'w')

saida.write("Média do Erro: " + str(np.mean(error)) + "\n")
saida.write("Desvio Padrão: " + str(np.std(error)) + "\n")
saida.write("\n")
saida.write("Valores dos Erros: \n")
saida.write("\n")
for i in range(len(error)):
    saida.write(str(error[i]) + "\n")

saida.close()
