from random import randint
from time import sleep

computador = randint(1, 11)
soma = soma1 = 0
print('=-'*11)
print('JOGO DO PAR OU IMPAR')
print('=-'*11)
while True:
    jogador = int(input('Digite um valor: '))
    escolha = str(input('PAR [P] ou IMPAR [I]: ')).strip().upper()
    result = computador + jogador
    if escolha == 'P':
        par = result % 2
        if par == 0:
            print(f'Você venceu, pois o computador pensou em {computador} e você em {jogador}, portanto a soma desses números é igual a {result} que é par')
            sleep(1)
            print('Hmmmm, não aceito perder... VAMOS DE NOVO')
            sleep(1)
            print('=-'*11)
            soma += 1
        else:
            print(f'HAHAHA GAMER OVER, EU VENCI, pensei em {computador} e você em {jogador}, todos sabemos que {result} que é impar!!!')
            break
            sleep(1)
            soma1 += 1
    if escolha == 'I':
        impar = result % 2
        if impar != 0:
            print(f'Você venceu, pois o computador pensou em {computador} e você em {jogador}, portanto a soma desses números é igual a {result} que é impar')
            sleep(1)
            print('Hmmmm, não aceito perder... VAMOS DE NOVO')
            sleep(1)
            print('=-'*11)
            soma += 1
        else:
            print(f'HAHAHA GAMER OVER, EU VENCI, pensei em {computador} e você em {jogador}, todos sabemos que {result} que é que é PAR')
            break
            sleep(1)
            soma1 += 1
if soma > soma1:
    sleep(1)
    print(f'Você venceu {soma} vezes, por hoje é só... Você até que é bom')
else:
    sleep(1)
    print('É melhor parar enquanto estou ganhando. Até a proxima!')
