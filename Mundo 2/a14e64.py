# Leia vários números inteiros, o programa só irá parar quando o usuário digitar 999.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag(parada))

num = cont = soma = 0
num = int (input('Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
