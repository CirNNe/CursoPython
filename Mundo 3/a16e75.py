# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.

valor = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')), int(input('Digite o 3º número: ')), int(input('Digite o 4º número: ')))
print(valor)
print(f'O número 9 foi digitado {valor.count(9)}x')
if 3 in valor:
    print(f'A posição do primeiro número 3 foi {valor.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Número(s) par(es): ', end='')
for p in valor:
    if p % 2 == 0:
        print(f'{p}', end=' ')
