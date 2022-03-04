r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas podem formar um triangulo.')
    if r1 == r2 == r3:
        print('Esse triângulo é Equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Esse triângulo é Isóceles!')
    else:
        print('Esse triângulo é Escaleno!')
else:
    print('Essas retas NÃO podem formar um triangulo.')