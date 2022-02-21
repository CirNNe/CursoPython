n1 = int(input('Digite um valor: '))
n2 = int(input('Digite mais um valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
print(f'A soma é {s}, a multiplicação é {m}, a divisão é {d:.3f}', end='')
print(f', a potência é {e} e a divisão inteira é {di}')