n = int(input('Digite um número inteiro: '))
opcao = int(input('''Você deseja converter para:
[1]BINÁRIO
[2]OCTAL
[3]HEXADECIMAL
Sua opção: '''))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida, por favor digite o valor de uma das opções listadas.')
