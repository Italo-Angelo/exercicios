maior = menor = soma = cont = me = 0
lista = []
continuar = 'S'
while continuar == 'S':
    quest = int(input('Digite um valor: '))
    before = str(input('Deseja continuar? [S]/[N]: ')).strip().upper()
    cont += 1
    soma += quest
    if cont == 1:
        maior = menor = quest
    else:
        if quest > maior:
            maior = quest
        if quest < menor:
            menor = quest
    if before == 'N':
        break
me = soma / cont
print('Progama finalizado, você digitou {} valores, com a média de {}, sendo destes o menor número {} e o maior {}'.format(cont, me, menor, maior))