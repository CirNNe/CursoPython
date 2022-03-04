'''
import random

usu = str(input('Pedra, Papel ou Tesoura? ')).strip().lower()
lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
if pc == 'pedra' and usu == 'tesoura':
    print('{} com {} da {}'.format(pc, usu, pc))
elif pc == 'papel' and usu == 'tesoura':
    print('{} com {} da {}'.format(pc, usu, usu))
elif pc == 'tesoura' and usu == 'tesoura':
    print('{} com {} da Empate!'.format(pc, usu))
elif pc == 'pedra' and usu == 'papel':
    print('{} com {} da {}'.format(pc, usu, usu ))
elif pc == 'papel' and usu == 'papel':
    print('{} com {} da empate!'.format(pc, usu))
elif pc == 'tesoura' and usu == 'papel':
    print('{} com {} da {}!'.format(pc, usu, pc))
elif pc == 'pedra' and usu == 'pedra':
    print('{} com {} da empate'.format(pc, usu))
elif pc == 'papel' and usu == 'pedra':
    print('{} com {} da {}!'.format(pc, usu, pc))
elif pc == 'tesoura' and usu == 'pedra':
    print('{} com {} da {}!'.format(pc, usu, usu))
else:
    print('Escolha entre PEDRA, PAPEL ou TESOURA')
'''

from random import randint
from time import sleep

pc = randint(0, 2)
itens = ('Pedra', 'Papel', 'Tesoura')
usu = int(input('''Suas opções:
[0] Pedra
[1] Pepel
[2] Tesoura
Qual é a sua jogada? '''))
if usu == 0 or usu == 1 or usu == 2:
    if pc == 0: # PC JOGA PEDRA
        sleep(1)
        print('PEDRA')
        sleep(1)
        print('PAPEL E')
        sleep(1)
        print('TESOOOURA!!')
        if usu == 0: # JOGADOR JOGA PEDRA
            print('{} com {} da EMPATE!'.format(itens[pc], itens[usu]))
        elif usu == 1: # JOGADOR JOGA PAPEL
            print('{} com {} da PAPEL, você GANHOU!'.format(itens[pc], itens[usu]))
        elif usu == 2: # JOGADOR JOGA TESOURA
            print('{} com {} da PEDRA, você PERDEU!'.format(itens[pc], itens[usu]))
        else:
            print('Opção inválida!')
    elif pc == 1: # PC JOGA PAPEL
        sleep(1)
        print('PEDRA')
        sleep(1)
        print('PAPEL E')
        sleep(1)
        print('TESOOOURA!!')
        if usu == 0: # JOGADOR JOGA PEDRA
            print('{} com {} da PAPEL, você PERDEU!'.format(itens[pc], itens[usu]))
        elif usu == 1: # JOGADOR JOGA PAPEL
            print('{} com {} da EMPATE!'.format(itens[pc], itens[usu]))
        elif usu == 2: # JOGADOR JOGA TESOURA
            print('{} com {} da TESOURA, você GANHOU!'.format(itens[pc], itens[usu]))
        else:
            print('Opção inválida!')
    elif pc == 2: # PC JOGA TESOURA
        sleep(1)
        print('PEDRA')
        sleep(1)
        print('PAPEL E')
        sleep(1)
        print('TESOOOURA!!')
        if usu == 0: # JOGADOR JOGA PEDRA
            print('{} com {} da PEDRA, você GANHOU!'.format(itens[pc], itens[usu]))
        elif usu == 1: # JOGADOR JOGA PAPEL
            print('{} com {} da TESOURA, você PERDEU!'.format(itens[pc], itens[usu]))
        elif usu == 2: # JOGADOR JOGA TESOURA
            print('{} com {} da EMPATE!'.format(itens[pc], itens[usu]))
        else:
            print('Opção inválida!')
else:
    print('Opção inválida!')
