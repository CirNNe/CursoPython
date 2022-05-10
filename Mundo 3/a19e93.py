# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
c_gols = list()
total_gols = 0

jogador['nome'] = str(input('Nome do Jogador: '))

partidas = int(input('Q. de partidadas jogadas: '))

for c in range(0, partidas):
    c_gols.append(int(input(f'Gols feitos na {c} partida: ')))
    
    total_gols += c_gols[c]

jogador['sequencia gols'] = c_gols.copy()

jogador['total'] = total_gols

print('-=' * 30)

print(jogador)

print('-=' * 30)

for k, v in jogador.items():
    print(f'{k}: {v}')

print('-=' * 25)

print(f"O jogador {jogador['nome']} jogou {partidas} partidas")
for i, v in enumerate(c_gols):
    print(f'    => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {total_gols} gols')

print('-=' * 25)
