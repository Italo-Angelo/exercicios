print('##'*40)
print('IREMOS ANALISAR SE SUAS MEDIDAS FORMAM UM TRIÂNGULO')
print('##'*40)
reta1 = float(input('Qual o valor da primeira reta: '))
reta2 = float(input('Qual o valor da segunda reta: '))
reta3 = float(input('Qual o valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Você consegue formar um triangulo')
else:
    print('Você não consegue formar um triangulo')


#a soma dos dois lados tem que ser igual ao ultimo lado