import emoji
print('=-'*44)
print('Aqui iremos lhe mostrar todos os números os números impares divisiveis por 3 de 0 a 50')
print('=-'*44)
print('''Preparado?
\033[34m[1]SIM
\033[31m[2]NÃO\033[1;97m''')
a = int(input(':'))
if a == 1:
    for c in range(0, 52, 2):
        print('\033[31m', c, end=' ')
else:
    print(emoji.emojize('Ok, até mais tarde!:thumbs_up:'))