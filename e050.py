va = 0
for c in range(1, 7):
    a = int(input('Digite um número inteiro:'))
    if a%2 == 0:
        va += a
print('A soma de todos os números PARES é {}'.format(va))