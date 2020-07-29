from random import randint
num1 = randint(1, 5)
num = int(input('O computador pensou em um número, consegue advinhar? Digite um número de 1 a 5: '))
if num == num1:
    print('Parabéns! Você venceu!')
else:
    print('HAHAHAHAHAHA PERDEU! O NÚMERO ERA {} :o'.format(num1))