# TUPLAS:

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# ÍNDICE       0           1       2        3
print(lanche)
print(lanche[0])
print(lanche[-1])
print(lanche[1:3])
print(lanche[:3])
print(lanche[:-2])
print(len(lanche))
print('-' * 40)

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('-' * 40)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('-' * 40)

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')
print('-' * 40)

print(sorted(lanche)) # EM ORDEM
print('-' * 40)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5)) # QUANTOS 5 TEM NA TUPLA
print(c.index(8)) # EM QUE POSIÇÃO ESTÁ O 8, BUSCA A PRIMEIRA OCORRÊNCIA
print('-' * 40)

pessoa = ('Higor', 24, 'M', 86.5)
print(pessoa)
print('-' * 40)

paraapagar = ('Apagar')
del(paraapagar) # COMANDO PARA APAGAR A TUPLA, VAI APRESENTAR UM ERRO AO DAR O PRINT
print(paraapagar)
