from time import sleep

print('=-'*16)
print('DESCOBRINDO SE O NÚMERO É PRIMO')
print('=-'*16)
num = int(input('Digite o número:'))
print
tudo= 0
for c in range(1, num + 1):
    if num % c == 0:
        tudo+= 1
if tudo == 2:
    sleep(1)
    print('O número {} é primo, porque foi divisivel por um e por ele mesmo'.format(num))
else:
    sleep(1)
    print('O número {} NÃO é primo porque foi divisivel {} veves'.format(num, tudo))
    