from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
sleep(1)
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Ao todo seu nome tem {} letras'.format(len(nome)- nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))