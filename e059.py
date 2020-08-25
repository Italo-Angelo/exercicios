from time import sleep
import emoji

question = int(input('Digite um valor: '))
question1 = int(input('Digite um valor: '))
maior = question
if question1 > maior:
    maior = question1
option = 0
while option != 5:
    option1 = int(input('''\033[1;94mO que deseja fazer?
    [1]Somar
    [2]Multiplicar
    [3]Maior valor
    [4]Novos números
    [5]Sair
    Selecione uma opção:\033[0;0m'''))
    if option1 == 1:
        sleep(1)
        print('\033[1;32mA soma entre {} e {} é {}\033[0;0m'.format(question, question1, question + question1))
    if option1 == 2:
        sleep(1)
        print('\033[1;32mA multiplicar {} por {} você tem {}\033[0;0m'.format(question, question1, question * question1))
    if option1 == 3:
        sleep(1)
        print('\033[1;32mO maior número entre {} e {} é {}\033[0;0m'.format(question, question1, maior))
    if option1 == 4:
        sleep(1)
        question = int(input('Digite um valor: '))
        question1 = int(input('Digite um valor: '))
    if option1 >= 6:
        sleep(1)
        erro=int(input('\033[1;31mNúmero invalido, tente novamente apertando 6:\033[0;0m'))
    if option1 == 5:
        sleep(1)
        print(emoji.emojize('Tenha uma boa semana :thumbs_up:'))
        break