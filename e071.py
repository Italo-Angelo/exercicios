print('='*30)
print('{:*^30}'.format('BANCO BPNSC'))
valor = int(input('Que valor você quer sacar? R$'))
tot = valor
money = 50
totmoney = 0
while True:
    if tot >= money:
        tot -= money
        totmoney += 1
    else:
        if totmoney > 0:
            print(f'Total de {totmoney} cédulas de R${money}')
        if money == 50:
            money = 20
        elif money == 20:
            money = 10
        elif money == 10:
            money = 1
        totmoney = 0
        if tot == 0:
            break
print('='*30)
print('O banco BPNSC lhe deseja um ótimo dia. Volte sempre!')