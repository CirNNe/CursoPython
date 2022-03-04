frase = str(input('Digite um frase: ')).strip().lower()
palavras = frase.split() # GERAR UM LISTA
junto = ''.join(palavras) # JUNTAR A LISTA
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('Essa frase é um palídomo!')
else:
    print('Essa frase NÃO É um palídromo!')