n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Sua média é {} e está abaixo do esperado, você está REPROVADO'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média é {} e você está em RECUPERAÇÂO, boa sorte!'.format(media))
else:
    print('Parabéns, sua média é de {} e com isso você está APROVADO(a)'.format(media))