from random import randint

cont = 0

while True:
    usu = int(input('Digite um número: '))        # ESCOLHAS DO USU
    parimpar = str(input('Par ou Ímpar? [P/I]:')).strip().upper()

    pc = randint(0, 10) # ESCOLHA DO PC

    soma = usu + pc # SOMA DAS ESCOLHAS

    if soma % 2 == 0: # DEFININDO SE PAR
        resultado = 'PAR'
    if soma % 2 == 1: # DEFININDO SE ÍMPAR
        resultado = 'IMPAR'

    if parimpar in 'Pp': # USU: ESCOLHE PAR
        if soma % 2 == 0: # USU: SE A SOMA FOR PAR, ELE GANHA
            cont += 1
            print(f'''
Você jogou {usu} e o PC jogou {pc}
{soma} é {resultado}!
VOCÊ VENCEU!
''')

        elif soma % 2 == 1: # USU: SE A SOMA FOR ÍMPAR, ELE PERDE
            print(f'''
Você jogou {usu} e o PC jogou {pc}
{soma} é {resultado}!
VOCÊ PERDEU!
{cont} VITÓRIAS CONSECUTIVAS!''')
            break

    if parimpar in 'Ii': # USU: ESCOLHE ÍMPAR
        if soma % 2 == 1: # USU: SE A SOMA FOR ÍMPAR, ELE GANHA
            cont += 1 
            print(f'''
Você jogou {usu} e o PC jogou {pc}
{soma} é {resultado}!
VOCÊ VENCEU!
''')
        if soma % 2 == 0: # USU: SE A SOMA FOR PAR, ELE PERDE
            print(f'''
Você jogou {usu} e o PC jogou {pc}
{soma} é {resultado}!
VOCÊ PERDEU!
{cont} VITÓRIAS CONSECUTIVAS!''')
            break
