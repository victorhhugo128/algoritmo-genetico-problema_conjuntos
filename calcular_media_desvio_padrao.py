import math
import pickle

with open("resultados_obtidos.pkl", "rb") as resultados_obtidos:
    resultados = pickle.load(resultados_obtidos)

N = len(resultados)

media = 0

for resultado in resultados:
    media += resultado
media = media/N

print(f"Media = {media}")

desvio_padrao = 0

for resultado in resultados:
    desvio_padrao = (resultado - media)**2
desvio_padrao = desvio_padrao/N
desvio_padrao = math.sqrt(desvio_padrao)

print(f"Desvio Padrao = {desvio_padrao}")

maior = 0
menor = 1000

for i in resultados:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(f"Maior: {maior}\nMenor: {menor}")