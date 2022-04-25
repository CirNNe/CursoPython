# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []

while True:
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        lista.append(valor), lista_par.append(valor)
    elif valor % 2 == 1:
        lista.append(valor), lista_impar.append(valor)
    resp = ' '
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Comando inválido, digite S ou N: ')).strip().upper()
    if resp == 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista com números pares digitados é {lista_par}')
print(f'A lista com números impares digitados é {lista_impar}')
