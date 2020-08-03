num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
ordem = sorted([num1, num2])
if num1 > num2:
    print('O maior número é {}'.format(ordem[1]))
elif num1 < num2:
    print('O maior número é {}'.format(ordem[1]))
else:
    print('Os valores são iguais!')