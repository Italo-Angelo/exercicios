a = int(input('Digite um número inteiro: '))
print('''Escolha qual opção deseja para a conversão:
[1]BINARIO
[2]OCTA
[3]HEXADECIMAL''')
select =int(input('Escolha a opção: '))
if select == 1:
    print('O número {} em BINARIO é {}'.format(a, bin(a)[2:]))
elif select == 2:
    print('O número {} em OCTA é {}'.format(a, oct(a)[2:]))
elif select == 3:
    print('O número {} em HEXADECIMAL é {}'.format(a, hex(a)[2:]))
else:
    print('Por favor, {} NÃO está entre as opções, tente novamente.'.format(select))
