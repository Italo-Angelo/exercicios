from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    a = int(input('Digite o {}° ano de nascimento:'.format(c)))
    atual = ano - a
    if atual <= 18:
        maior += 1
    else:
        menor += 1
print('De 7, {} são maiores de idade'.format(maior))
print('E {} são menores de idade'.format(menor))