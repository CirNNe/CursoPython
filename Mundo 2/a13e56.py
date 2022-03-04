somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, 5):
    print('{}ª PESSOA'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
mediaidade = somaidade / 4
print('A média da idade do grupo é de {} anos'.format(mediaidade))
print('O nome do homem mais velho do grupo é {} com {} anos'.format(nomevelho, maioridadehomem))
print('O total de mulheres com menos de 20 anos é {}'.format(totmulher20))
