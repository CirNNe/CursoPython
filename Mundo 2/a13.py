# Laços de Repetição
# FOR:

#Básico:
for c in range(1, 6):
    print('Oi')
print('FIM')

#1 até 6:
for c in range(1, 7):
    print(c)
print('FIM')

#6 até 1:
for c in range(6, 0, -1):
    print(c)
print('FIM')

#De 0 até 6, pulando de 2 em 2:
for c in range(0, 7, 2):
    print(c)
print('FIM')

#de 0 a um número escolhido:
n = int(input('Digite um número: '))
for n in range(0, n + 1):
    print(n)
print('FIM')

#Lendo o início, o fim e de quantos e quantos números pular:
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Pular de: '))
for c in range(i, f + 1, p):
    print(c)
print('FIM')

#Soma dos valores digitados:
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('A soma dos valores é {}'.format(s))
