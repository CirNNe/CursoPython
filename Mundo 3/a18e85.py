# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

n = [[], []]
valor = 0
for v in range(1, 8):
    valor = int(input(f'Digite o {v} valor: '))
    if valor % 2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
n[0].sort()
n[1].sort()
print(f'Valor(es) par(es) digitado(s): {n[0]}')
print(f'Valor(es) ímpar(es) digitado(s): {n[1]}')
