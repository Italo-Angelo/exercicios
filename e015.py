km = float(input('Quantos km você percorreu: '))
dias = float(input('Quantos dias você ficou com o carro? '))
calc = km * 0.15
calc1 = dias * 60
calc3 = calc+calc1
print('O total a pagar é R${}'.format(calc3))
