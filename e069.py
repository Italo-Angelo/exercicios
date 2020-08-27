maior = homem = mu20 = tot = 0
while True:
    print('=-'*10)
    print('CADASTRO DE PESSOAS')
    print('=-'*10)
    per = int(input('Idade: '))
    per1 = str(input('Sexo: [M]/[F]: ')).strip().upper()
    per2 = str(input('Deseja continuar? [S]/[N]: ')).strip().upper()
    if per >= 18:
        maior += 1
    if per1 == 'M':
        homem += 1
        tot += 1
    if per1 == 'F':
        mu = 20
        tot += 1
        if per <= mu:
            mu20 += 1
    if per2 == 'N':
        break
print(f'Ao todo foram registrados {tot} pessoas. Dessas {homem} são homens e {mu18} mulheres são maiores de idade')
print(f'e ao todo {maior} são maiores de idade')
