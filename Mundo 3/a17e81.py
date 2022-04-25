# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

from operator import invert


lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    resp = str(input('Deseja continuar? [S/N]:')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Valor inválido, digite S ou N: ')).strip().upper()
    if resp == 'N':
        break
lista.sort(reverse=True)
if 5 not in lista:
    print('O número 5 não foi digitado')
else:
    print('O número 5 foi digitado na lista')
print(f'Foram digitados {len(lista)} números')
print(f'Lista em ordem decrescente {lista}')
