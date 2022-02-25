from random import choice, shuffle

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')
lista = [nome1, nome2, nome3, nome4]
sorteio = choice(lista)
shuffle(lista)
print('O sorteado para apagar o quadro é {}'.format(sorteio))
print('E a ordem de apresentação é essa:', lista)