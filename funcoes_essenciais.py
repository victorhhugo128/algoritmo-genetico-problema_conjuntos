from random import randint, choice
import pickle
from time import sleep, time


def algoritmo_genetico(n_populacao: int, taxa_mutacao: float, geracoes: int):
    populacao = []

    for individuo in range(n_populacao):
        populacao.append(gerar_individuo())

    contagem = 0
    while contagem < geracoes:
        filhos = []
        roleta = gerar_roleta_selecao(populacao)
        elite_indice = retornar_individuo_mais_apto(populacao)
        filhos.append(populacao[elite_indice])  # passa o individuo mais apto diretamente para a próxima geração
        while len(filhos) < n_populacao:
            pai1 = 0
            pai2 = 0
            while pai1 == pai2:
                pai1 = choice(roleta)
                pai2 = choice(roleta)
            filhos_gerados = crossover(populacao, [pai1, pai2], taxa_mutacao)
            """ valido = individuo_valido(filhos_gerados[0]) and individuo_valido(filhos_gerados[1])
            if not valido:
                continue """
            for filho in filhos_gerados:
                if len(filhos) == n_populacao:
                    continue
                filhos.append(filho)
        populacao = filhos
        contagem += 1

    return populacao


def gerar_individuo() -> list:
    verificar_individuo = dict()

    for i in range(1, 1001):
        verificar_individuo[str(i)] = 0

    possibilidades = [False]
    [possibilidades.append(True) for i in range(10)]

    while True:
        verificar_individuo = dict.fromkeys(verificar_individuo, 0)
        individuo = []
        for i in range(200):
            cromossomo = choice(possibilidades)
            individuo.append(cromossomo)
        individuo_indice = 0
        with open("instance.txt", "r") as instance:
            for camera in instance.readlines():
                if individuo[individuo_indice]:
                    area_list = camera.strip()
                    area_list = area_list.split(", ")
                    for area in area_list:
                        verificar_individuo[area] += 1
                individuo_indice += 1
        if 0 not in verificar_individuo.values():
            return individuo


def fitness(individuo: list) -> int:
    qtd_cameras = 0
    for i in individuo:
        if i:
            qtd_cameras += 1
    if not individuo_valido(individuo):
        return 1
    return int((200 - qtd_cameras)**2)


def retornar_individuo_mais_apto(populacao: list) -> int:
    individuo_mais_apto = populacao[0]
    indice = 0
    contagem = 0
    for individuo in populacao:
        aptidao = fitness(individuo)
        if aptidao > fitness(individuo_mais_apto):
            individuo_mais_apto = individuo
            indice = contagem
        contagem += 1
    return indice # retorna índice do indivíduo mais apto


def gerar_roleta_selecao(populacao: list) -> list:
    roleta = []

    for individuo in range(0, len(populacao)):
        fitness_individuo = fitness(populacao[individuo])
        for i in range(fitness_individuo):
            roleta.append(individuo)
    return roleta


def crossover(populacao: list, indice_pais: list, taxa_mutacao: float) -> list:
    individuos_separados = []
    indice_separados = 0
    for indice in indice_pais:
        individuos_separados.append([])
        for partes in range(0, 200, 50):
            individuos_separados[indice_separados].append(populacao[indice][partes: partes + 50])
        indice_separados += 1

    pai1 = individuos_separados[0]
    pai2 = individuos_separados[1]

    filho1 = pai1[0] + pai2[1] + pai1[2] + pai2[3]
    filho2 = pai2[0] + pai1[1] + pai2[2] + pai1[3] 
    
    peso = int(taxa_mutacao * 100)
    roleta = []
    [roleta.append(True) for chance in range(peso)]
    while len(roleta) < 100: roleta.append(False) 

    for cromossomo in range(0, len(filho1)):
        rodada = randint(0, 99)
        if roleta[rodada]:
            filho1[cromossomo] = not filho1[cromossomo]

    for cromossomo in range(0, len(filho2)):
        rodada = randint(0, 99)
        if roleta[rodada]:
            filho2[cromossomo] = not filho2[cromossomo]

    return [filho1, filho2]


def individuo_valido(individuo: list) -> bool:
    verificar_individuo = dict()

    for i in range(1, 1001):
        verificar_individuo[str(i)] = 0

    individuo_indice = 0
    with open("instance.txt", "r") as instance:
        for camera in instance.readlines():
            if individuo[individuo_indice]:
                area_list = camera.strip()
                area_list = area_list.split(", ")
                for area in area_list:
                    verificar_individuo[area] += 1
            individuo_indice += 1
    if 0 in verificar_individuo.values():
        return False
    return True


def contar_cameras(individuo: list) -> int:
    contador = 0
    for i in individuo:
        if i:
            contador += 1
    return contador


if __name__ == "__main__":
    solucoes = []

    for i in range(20):
        populacao = algoritmo_genetico(50, 0.01, 200)

        melhor_individuo = populacao[retornar_individuo_mais_apto(populacao)]

        solucoes.append(contar_cameras(melhor_individuo))
    
    """ with open("resultados_obtidos.pkl", "wb") as resultados:
        pickle.dump(solucoes, resultados)
    with open("resultados_obtidos.pkl", "rb") as resultados:
        x = pickle.load(resultados)
    print(x) """