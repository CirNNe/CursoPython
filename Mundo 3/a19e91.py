# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

import enum
from random import randint
from operator import itemgetter

resultado = [[], [], [], []]
jogadores = dict()
ranking = list()

for c in range(0, 4):
    dado = randint(1, 6)
    resultado[c].append(dado)
    jogadores[c] = dado

for k, v in jogadores.items():
    print(f'jogador {k+1} tirou {v} no dado')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: Jogador {v[0]+1} com {v[1]} pontos')
