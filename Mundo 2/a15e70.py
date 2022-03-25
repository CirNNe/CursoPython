#C rie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato.

total = prodmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Produto: '))
    valor = float(input('Valor do produto R$: '))
    cont += 1
    total += valor
    if valor > 1000:
        prodmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resposta not in 'S':
        break                         
print(f'''
Valor total da compra: R$ {total:.2f}
Quant. de produtos com valor maior que mil reais: {prodmil}
O produto mais barato foi {barato} que custa R$ {menor:.2f}
''')
