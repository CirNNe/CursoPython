# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


valores = []
for c in range(1, 6):
    valores.append(int(input(f'Digite o {c}º valor: ')))
maior = max(valores)
menor = min(valores)
print(f'O maior número da lista é: {max(valores)} e sua posição é: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i+1}...', end='')
print(f'\nO menor número da lista é: {min(valores)} e sua posição é: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i+1}...', end='')
