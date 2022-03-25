# PRIMEIRA OPÇÃO:
'''
n = int(input('Digite o número para ver sua tabuada: '))
print('A tabuada de {} é:'.format(n))
for c in range(1, 11):
    t = n * c
    print(n ,'*', c, '=', t)
print('Bons estudos!')
'''

# SEGUNDA OPÇÃO:

n = int(input('Digite um número para ver usa tabuada: '))
for t in range(1, 11):
    r = n * t
    print(f'{n} x {t:2} = {r:2}')
print('Bons estudos!')
