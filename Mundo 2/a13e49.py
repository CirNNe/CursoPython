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

n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print ('{} x {:2} = {}'. format(n, c, n*c))
print('Bons estudos!')