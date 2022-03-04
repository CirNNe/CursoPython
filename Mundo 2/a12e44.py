valor_p = float(input('Digite o valor do produto: R$ '))
forma_pagamento = int(input('''Forma de pagamento:
[1]dinheiro/cheque
[2]1x no cartão
[3]2x no cartão
[4]3x ou mais no cartão
Sua opção: '''))
if forma_pagamento == 1:
    valor = valor_p - (valor_p * 10/100)
    print('O valor do produto com 10% de desconto é R$ {:.2f}'.format(valor))
elif forma_pagamento == 2:
    valor = valor_p - (valor_p * 5/100)
    print('O valor do produto com 5% de desconto é de R$ {:.2f}'.format(valor))
elif forma_pagamento == 3:
    valor = valor_p
    print('O valor final do produto em 2x no cartão é R$ {:.2f}'.format(valor))
elif forma_pagamento == 4:
    valor = valor_p + (valor_p * 20/100)
    print('O valor final do produto em 3x no cartão é de R$ {:.2f}'.format(valor))
else:
    print('Opção inválida, por favor digitar um das opções listadas.')
