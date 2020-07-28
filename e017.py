from math import hypot
a = float(input('Digite o valor do cateto adjacente: '))
b = float(input('Digite o valor do cateto oposto: '))
print('A hipotenusa de {} e {} é igual a {:.2f}'.format(a, b, hypot(a, b)))