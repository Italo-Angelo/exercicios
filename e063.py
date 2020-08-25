n = int(input('Quantos termos deseja encontrar: '))
primeiro = 0
segundo = 1
print ('{}, {}'.format(primeiro, segundo), end='')
cont = 3
while cont <= n:
    terceiro = segundo + primeiro
    print(', {}'.format(terceiro), end='')
    primeiro = segundo
    segundo = terceiro
    cont +=1
print(', FIM!')