# Como usar as bibliotecas do Python

# Para importar toda a biblioteca:
# Primeiro exemplo:

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

# Segundo exemplo:

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) # Isso irá arredondar a raiz para cima


# Para importar somente funções específicas:
# Primeiro exemplo:

from math import sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num) # Quando importamos uma função específica da biblioteca, não é necessário referênciar ela: math.sqrt
print('A raiz quadrada de {} é igual a {}'.format(num, raiz))

# Segundo exemplo:

from math import sqrt, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num, floor(raiz))) # Usando a função de arredondamento para baixo


