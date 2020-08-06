frase = str(input('Digite uma frase: ')).strip().upper()
pa = frase.split()
ju = ''.join(pa)
inv = ''
for c in range(len(ju) -1, -1, -1):
    inv += ju[c]
if inv == ju:
    print('Temos aqui um PALÍNDROMO, {} de trás pra frente fica {}'.format(frase, inv))
else:
    print('Não temos um PALÍNDROMO!')