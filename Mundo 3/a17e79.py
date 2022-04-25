# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


lista = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in lista:
        lista.append(valor)
    else:
        print('Valor duplicado!')
    continuar = ' '
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Comando inválido, digite novamente [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
lista.sort()
print(lista)
