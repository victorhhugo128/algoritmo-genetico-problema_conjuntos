from matplotlib import pyplot as plt
import pickle

with open("solucoes_pelas_geracoes.pkl", "rb") as resultados:
        solucoes = pickle.load(resultados)

plt.plot(solucoes)
plt.xlabel("Gerações")
plt.ylabel("Número de Câmeras")
plt.show()
