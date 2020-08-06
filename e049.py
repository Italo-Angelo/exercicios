calc = int(input('Digite um número inteiro que iremos mostrar a sua tabuada:'))
for c in range(1, 11):
    print('{}x{}={}'.format(calc, c, calc*c))