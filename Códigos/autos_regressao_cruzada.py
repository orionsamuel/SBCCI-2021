import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import cross_val_score
from keras.wrappers.scikit_learn import KerasRegressor

base = pd.read_csv('4x4_latency_train.csv')

previsores = base.iloc[:,:-1].values
latency = base.iloc[:,-1].values

def criar_rede():
    regressor = Sequential()
    regressor.add(Dense(units = 158, activation = 'relu', input_dim = 316))
    regressor.add(Dense(units = 158, activation = 'relu'))
    regressor.add(Dense(units = 1, activation = 'linear'))
    regressor.compile(loss = 'mean_absolute_error', optimizer = 'adam',
                      metrics = ['mean_absolute_error'])
    return regressor

regressor = KerasRegressor(build_fn = criar_rede,
                           epochs = 100,
                           batch_size = 300)
resultados = cross_val_score(estimator = regressor,
                             X = previsores, y = latency,
                             cv = 10, scoring = 'mean_absolute_error')
print(resultados.mean())
print(resultados.std())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
