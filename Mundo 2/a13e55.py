maior = 0
menor = 0
for pessoa in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if pessoa == 1: # SE O VALOR DIGITADO FOR DA 1ª PESSOA, MAIOR E MENOR PASSAM A TER OS VALORES DIGITADOS NO INPUT
        maior = peso
        menor = peso
    else: # SE OS VALORES DIGITADOS FOREM DOS USUARIOS SEGUINTES, SERÃO ANALIZADOS OS VALORES E, SE NECESSÁRIO, SUBSTITUIDOS NOS MAIOR E MENOR
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
