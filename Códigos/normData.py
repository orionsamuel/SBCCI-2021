import pandas as pd

dados = pd.read_csv("4x4.csv")
target = dados["latency"]
dados = dados.drop(["latency"], axis = 1)

dados = (dados-dados.min())/(dados.max()-dados.min())

dados = dados.join(target)

dados.to_csv("4x4_norm.csv", sep=',', index=False)
