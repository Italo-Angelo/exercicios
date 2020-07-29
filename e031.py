a = int(input('Qual a distância da sua viagem em km? '))
b = 0.50 * a 
c = 0.45 * a
if a <=200:
    print('O valor da sua viagem é de R${:.2f}'.format(b))
else:
    print('O valor da sua viagem é R${:.2f}'.format(c))