from random import randint

chute = int(input('Chute um número entre 0 e 10: '))
pc = randint(0, 10)
palpites = 0
while chute != pc:
    chute = int(input('Tente outra vez: '))
    palpites += 1
    if chute < pc:
        print('Maior, tente outra vez: ')
    elif chute > pc:
        print('Menos, tente outra vez: ')
print('Acertou com {} palpite(s)!'.format(palpites +1))
