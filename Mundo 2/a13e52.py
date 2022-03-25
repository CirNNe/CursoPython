num = int(input('Digite um número para saber se ele é primo: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
print('O número {} pode ser dividido {}x'.format(num, tot))
if tot == 2:
    print('O {} só pode ser dividido por 1 e por ele mesmo, por isso ele é PRIMO!'.format(num))
else:
    print('Por isso ele NÃO é PRIMO!')
