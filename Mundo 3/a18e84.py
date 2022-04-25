# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dados = list()
temp = list()
mais = menos = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(dados) == 0:
        mais = menos = temp[1]
    else:
        if temp[1] > mais:
            mais = temp[1]
        if temp[1] < menos:
            menos = temp[1]

    dados.append(temp[:])
    temp.clear()

    continuar = str(input('Deseja adicionar outra informação?[S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Informação inválida, digite novamente [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Pessoa(s) cadastrada(s): {len(dados)}.')


print(f'O maior peso foi {mais}KG de ', end='')
for p in dados:
    if p[1] == mais:
        print(f'[{p[0]}] ', end='')

print(f'\nO menor peso foi {menos}KG de ', end='')
for p in dados:
    if p[1] == menos:
        print(f'[{p[0]}] ', end='')
