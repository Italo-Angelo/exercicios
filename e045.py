from random import randint
from time import sleep
games = ('Pedra', 'Papel', 'Tesoura')
com = randint(0, 2)
print('''Suas opções:
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogada = int(input('Escolha sua jogada'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('Computador jogou {}'.format(games[com]))
print('Jogador jogou {}'.format(games[jogada]))
if com == jogada:
    print('EMPATE')
elif com ==0:
    if jogada ==1:
        print('O jogador venceu!')
    if jogada ==2:
        print('O computador venceu!')
elif com ==1:
    if jogada ==2:
        print('O jogador venceu!')
    if jogada ==0:
        print('O computador venceu!')
elif com ==2:
    if jogada == 1:
        print('O computador venceu!')
    if jogada ==0:
        print('O jogador venceu!')