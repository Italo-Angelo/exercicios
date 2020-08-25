a = int(input('Primeiro termo:'))
b = int(input('Razão:'))
c = a 
cont = 1
total = 0
continuar = 10
while continuar != 0:
    total += continuar
    while cont <= total:
        print('{}, '.format(c), end='')
        c += b
        cont += 1
    print('Pausa')
    continuar = int(input('Você deseja adcionar mais termos? Quantos? Se deseja encerrar digite 0:'))
print('Processo finalizado com {} progressões sendo mostrada'.format(total))