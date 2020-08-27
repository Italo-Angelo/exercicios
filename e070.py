from time import sleep
print('=-'*12)
print('MERCADINHO DO ANGELO')
print('=-'*12)
total = produtos = menor = cont = 0
barato = ''
while True:
    pd = str(input('Produto: '))
    valor = int((input('Valor: R$: ')))
    continuar = str(input('Deseja continuar? [S]/[N]: ')).strip().upper()
    total += valor
    cont =+ 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = pd
    if valor >= 1000:
        produtos += 1
    if continuar == 'N':
        break
    sleep(1)
print('COMPRA REALIZADA COM SUCESSO')
print('A compra ficou no valor de R${:.2f}'.format(total))
print('Temos o total de produtos {} custando acima de R$1000.00'.format(valor))
print('O produto mais barato foi {} custando R${}'.format(barato, menor))