a = int(input('Qual a velocidade do seu carro? '))
b = (a - 80) * 7 
if a <=80:
    print('Tudo certo por aqui, tenha uma boa viagem!')
else:
    print('Você passou do limite de 80km! Você foi multado em um valor de R${},00'.format(b))
