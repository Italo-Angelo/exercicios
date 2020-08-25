from random import randint
cont = 0
num = randint(0, 10)
print('=-'*40)
print('Jogo da adivinhação')
print('=-'*40)
print('Você consegue advinhar o número? O computador pensou em um número.')
certo = False
while not certo:
    erro = int(input('Qual acha que foi? '))
    cont += 1
    if erro == num:
        certo = True
print(f'Acertou depois de tentar {cont} vezes')