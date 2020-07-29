salario = float(input('Qual valor do seu sálario? R$'))
r = salario * 1.1
if salario > 1250:
    print('Seu salario que antes era de R${} agora passará a ser R${:.2f}'.format(salario, r))
else:
    print('Seu salario que antes era de R${} agora passará a ser R${:.2f}'.format(salario, salario * 1.15))