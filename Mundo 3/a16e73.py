times = ('KAB', 'FUR', 'RCA', 'PAI', 'NMI', 'LIB', 'LOU', 'REN', 'FLA', 'INT')
print(f'Lista dos times do CBLOL: {times}')
print(f'Os 5 primeiros são: {times[:5]}')
print(f'Os últimos 4 são: {times[6:10]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print('A Pain está na {} posição'.format(times.index('PAI')+1))
