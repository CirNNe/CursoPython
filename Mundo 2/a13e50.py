soma = 0
for pares in range(1, 7):
    n = int(input(f'Digite o {pares} número: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos números pares é {soma}')
