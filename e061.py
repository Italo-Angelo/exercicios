a = int(input('Primeiro termo:'))
b = int(input('Razão:'))
c = a 
cont = 1
while cont <= 10:
    print('{}, '.format(c), end='')
    c += b
    cont += 1
print('Fim')