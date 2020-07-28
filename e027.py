n = str(input('Digite seu nome completo: ')).strip()
sepa = n.split()
print('Seu primeiro nome é {}'.format(sepa[0]))
print('Seu último nome é {}'.format(sepa[len(sepa)-1]))