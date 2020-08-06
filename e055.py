from time import sleep
maior = 0
menor = 1000
for c in range(1, 6):
    peso = float(input('Digite o {}° peso:'.format(c)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso foi {}kg e o menor foi {}kg'.format(maior, menor))
