reta1 = float(input('Qual o valor da primeira reta: '))
reta2 = float(input('Qual o valor da segunda reta: '))
reta3 = float(input('Qual o valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Você pode formar um triangulo')
    if reta1 == reta2 == reta3 == reta1:
        print('Você tem um triângulo EQUILÁTERO, onde todos os lados são iguais.')
    elif reta1 != reta2 != reta3 != reta1:
        print('Você tem um triangulo ESCALENO, onde todos os lados são diferentes.')
    else:
        print('Você tem um triângulo ISÓSCELES, onde dois lados são iguais e um diferente.')
else:
    print('Você não consegue formar um triangulo')