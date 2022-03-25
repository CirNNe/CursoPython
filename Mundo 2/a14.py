# While:
'''
c = 1 # INÍCIO DO CONTADOR
while c < 10: # Enquanto o contador não chegar a 10
    print(c)
    c = c + 1
print('FIM!')


c = 1 # INÍCIO DO CONTADOR
while c != 0: # CONDIÇÃO DE PARADA
    c = int(input('Digite um valor: '))
print('FIM!')
'''


n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
