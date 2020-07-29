from time import sleep
print('##'*40)
print('IREMOS ANALISAR SE SUAS MEDIDAS FORMAM UM TRIÂNGULO')
print('##'*40)
reta1 = float(input('Qual o valor da primeira reta: '))
reta2 = float(input('Qual o valor da segunda reta: '))
reta3 = float(input('Qual o valor da terceira reta: '))
soma = reta1 + reta2
if soma >= reta3:
    print('Você consegue formar um triangulo')
else:
    print('Você não consegue formar um triangulo')


#a soma dos dois lados tem que ser igual ao ultimo lado