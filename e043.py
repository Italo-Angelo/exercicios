peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso/(altura*altura)
if imc < 18.5:
    print('Você está abaixo do peso')
if 18.5 <= imc < 25:
    print('Peso normal')
if 25 <= imc < 30:
    print('Sobrepeso')
if 30 <= imc < 40:
    print('Obesidade')
if imc >= 40:
    print('Obesidade Mórbida')