tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    usu = ' '
    usu = int(input('Digite um número ente 0 e 20: '))
    while usu not in range(0, 21):
        usu = int(input('Valor inválido, digite novamente: '))
    print(f'Você digitou o número {tupla[usu]}')
    continuar = ' '
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Comando inválido, digite S ou N: ')).strip().upper()
    if continuar == 'N':
        break
