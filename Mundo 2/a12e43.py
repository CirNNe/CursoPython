peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu nível de IMC é {:.2f} e você está abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Parabéns, seu nível de IMC é {:.2f} e você está no peso ideal!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu nível de IMC é {:.2f}, você está com sobrepeso!'.format(imc))
elif imc >= 30 and imc < 40:
    print('Cuidado, seu nível de IMC é {:.2f} você está em nível de obesidade!'.format(imc))
else:
    print('Procure se cuidar, seu nível de IMC é {:.2f} e você está em nível de obesidade mórbida!'.format(imc))