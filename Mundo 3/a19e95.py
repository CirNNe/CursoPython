# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

fichas = list()
jogador = dict()
c_gols = list()
total_gols = 0

# COLETA DE DADOS:

while True:
    jogador['nome'] = str(input('Nome do Jogador: '))

    partidas = int(input('Q. de partidadas jogadas: '))

    for c in range(0, partidas):
        c_gols.append(int(input(f'Gols feitos na {c} partida: ')))

        total_gols += c_gols[c]

    jogador['sequencia gols'] = c_gols.copy()
    c_gols.clear()

    jogador['total'] = total_gols
    total_gols = 0

    fichas.append(jogador.copy())
    jogador.clear()

    continuar = str(
        input('Deseja adicionar outro jogador?[S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Comando inválido, digite novamente [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

# SAÍDA DOS DADOS:

print('-=' * 25)
for i, v in enumerate(fichas):
    print(f"{i+1} Jogador: {v['nome']} / Gols por partida: {v['sequencia gols']} / Total de gols: {v['total']}")
print('-=' * 25)

while True:
    mostrar_ficha = str(input('Deseja ver a fichar de algum jogador? ')).strip().upper()[0]
    while mostrar_ficha not in 'SN':
        mostrar_ficha = str(input('Comando inválido, digite novamente [S/N]: ')).strip().upper()[0]
    if mostrar_ficha == 'N':
        break
    else:
        print('''
-=-=-=-= FICHAS =-=-=-=-
cod / nome
-=-=-=-=-=-=-=-=-=-=-=-=
''', end='')
        for i, v in enumerate(fichas):
            print(f"{i+1} / {v['nome']}")
        codigo_jogador = int(input('Digite o código do jogador que deseja ver: '))
        while codigo_jogador > len(fichas):
            codigo_jogador = int(input('Código inválido, digite novamente: '))

        print(f'''
-=-= JOGADOR: {fichas[codigo_jogador - 1]['nome']} =-=-
gols / partida
''', end='')
        for g in range(0, len(fichas[codigo_jogador - 1]['sequencia gols'])):
            print(f"{fichas[codigo_jogador - 1]['sequencia gols'][g]} / {g+1}")
        print('-=-=-=-=-=-=-=-')
