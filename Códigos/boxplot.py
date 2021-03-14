import pandas as pd
import matplotlib.pyplot as plt


dados = pd.read_csv("packets-error.csv")

_4x4 = dados["4x4"]
_8x8 = dados["8x8"]
_16x16 = dados["16x16"]

plt.boxplot([_4x4, _8x8, _16x16], labels = ['4x4', '8x8', '16x16'])
plt.title("Error Packets Distribution")
plt.ylabel("Error Rate")
plt.xlabel("Topology Size")
plt.savefig("packets-boxplot")
