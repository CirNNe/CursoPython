salario = float(input('Digite o valor do seu salário R$: '))
if salario >= 1250:
    aumento10 = salario + (salario * 10/100)
    print('O seu salário passa a ser R$: {:.2f}'.format(aumento10))
else:
    aumento15 = salario + (salario * 15/100)
    print('O seu salário pasas a ser de R$: {:.2f}'.format(aumento15))