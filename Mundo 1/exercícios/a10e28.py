from random import randint

n = randint(0,5) # faz gerar o número aleatório
chute = int(input('Chute um número de 0 a 5: '))
if chute == n:
    print('Aee, acertou!')
else:
    print('Poxa, que pena, você errou.')