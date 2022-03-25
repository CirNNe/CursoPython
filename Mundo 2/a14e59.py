# Crie um programa que leia dois valores e mostre um menu na tela:
'''
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
'''
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = 0
while escolha != 4:
    escolha = (int(input('''
    [1] somar
    [2] multiplicar
    [3] novos números
    [4] sair do programa
    Sua escolha: 
    ''')))
    if escolha == 1:
        print('{} + {} = {}'.format(n1, n2, (n1 + n2)))
    elif escolha == 2:
        print('{} x {} = {}'.format(n1, n2, (n1 * n2)))
    elif escolha == 3:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif escolha == 4:
        print('Encerrando o programa...')
    else:
        print('Opção inválida, tente novamente!')
print('Obrigado por usar o programa!')
