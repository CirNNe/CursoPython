t = 0
while True:
    t = int(input('Digite um número para ver sua tabuada: '))
    if t < 0:
        break
    for v in range(1, 11):
        print(f'{t} x {v} = {t*v}')
