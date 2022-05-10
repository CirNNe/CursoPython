# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

from datetime import datetime

fichas = dict()
lista_pessoas = list()

soma_idade = 0 # CONTADOR PARA SOMAR A IDADE

while True:
    fichas['nome'] = str(input('Nome: ')) # INPUT DO NOME

    fichas['sexo'] = str(input('Sexo [M/F/Outro]: ')).strip().upper()[0] # INPUT DO SEXO
    while fichas['sexo'] not in 'MFO':
        fichas['sexo'] = str(input('Comando inválido, digite novamente [M/F/Outro]: ')).strip().upper()[0]

    nascimento = int(input('Ano de nascimento: ')) # INPUT DA IDADE
    fichas['idade'] = datetime.now().year - nascimento
    soma_idade += fichas['idade']

    lista_pessoas.append(fichas.copy()) # ADICIONANDO OS DICIONÁRIOS A LISTA FINAL
    fichas.clear()

    continuar = str(input('Deseja adicionar outra ficha [S/N]: ')).strip().upper()[0] # CONTINUAR OU NÃO
    while continuar not in 'SN':
        continuar = str(input('Comando inválido, digite novamente [N/S]: '))
    if continuar == 'N':
        break

media_idade = soma_idade / len(lista_pessoas) # CALCULO DA MÉDIA DE IDADE DAS PESSOAS

print('-=' * 20)

print(f'=> PESSOAS CADASTRADAS: {len(lista_pessoas)}') # QUANTIDADE DE PESSOAS CADASTRADAS

print(f'=> MÉDIA DE IDADE: {media_idade:.2f}') # MÉDIA DE IDADE DAS PESSOAS CADASTRADAS

print('=> MULHERES CADASTRADAS:') # LISTA DE MULHERES CADASTRADAS
for p in lista_pessoas:
    if p['sexo'] == 'F':
        print(f"Nome: {p['nome']} / Idade: {p['idade']}")

print('=> PESSOAS ACIMA DA MÉDIA DE IDADE:') # LISTA DAS PESSOAS COM IDADE ACIMA DA MÉDIA DO GRUPO
for p in lista_pessoas:
    if p['idade'] > media_idade:
        print(f"Nome: {p['nome']} / Sexo: {p['sexo']} / Idade: {p['idade']}")

print('-=' * 20)


