v_casa = float(input('Qual o valor da casa R$: '))
salario = float(input('Qual sua renda mensal R$: '))
anos = int(input('Em quantos anos deseja pagar: '))
mensalidade = v_casa / (anos * 12)
porcentagem = salario * 30/100
if mensalidade > porcentagem:
    print('O valor da prestação R$: {:.2f} ultrapassa o valor de 30%, R$ {:.2f}, da sua renda mensal.\n EMPRÉSTIMO NEGADO'.format(mensalidade, porcentagem))
else:
    print('Parabéns, seu EMPRÉSTIMO foi APROVADO com a mensalidade de R$ {:.2f}'.format(mensalidade))