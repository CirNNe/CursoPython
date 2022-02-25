r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 or r2 + r3 > r1 or r3 + r1 > r2:
    print('Essas retas podem formar um triângulo!')
else:
    print('O valor dessas retas são insuficientes para formar um triângulo!')