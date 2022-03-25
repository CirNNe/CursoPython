# Faça um programa que leia um número qualquer e mostre o seu fatorial
# exemplo: 5! = 5*4*3*2*1 = 120

n = int(input('Digite um número pra saber seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
