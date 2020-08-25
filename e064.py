soma = 0
cont = 0
num = 0
while num != 999:
    digi = int(input('Digite um valor, quando quiser parar, digite 999: '))
    if digi == 999:
        break
    soma += digi
    cont += 1
print('Progama finalizado, você digitou ao todo {} valores. A soma desses valores é igual a {}'.format(cont, soma))