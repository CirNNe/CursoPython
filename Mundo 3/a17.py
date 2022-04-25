num = [2, 5, 9, 1]
num[2] = 3 # muda o valor no indice apontado
num.append(7) # adiciona um valor no fim da lista
num.sort(reverse=True) # coloca a lista em ordem e de trás para frente
num.insert(2, 0) # insere um valor na posição apontada: 2
num.pop(2) # remove o valor na posição
num.remove(3)# remove o valor
print(len(num)) # lê o tamanho da lista'''
print(num)
print('-' * 40)


valores = []
valores.append(1)
valores.append(2)
valores.append(3)
for c, v in enumerate(valores): # printando a posição e o valor na lista
    print(f'Na posição {c} encontrei o valor {v}!')
print(valores)
print('-' * 40)

numeros = []
for cont in range(0, 5): # adicionando valores a lista pelo teclado
    numeros.append(int(input('Digite um valor: ')))
print(numeros)
print('-' * 40)

a = [1, 2, 3, 4]
b = a
b[2] = 8 # isso irá mudar tanto a lista B quando a lista A, pois existe uma ligação entre as listas, não é uma cópia
b = a[:] # isso fará com que a lista B vire uma cópia da lista A
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('-' * 40)
