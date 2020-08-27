cont = soma = 0
while True:
    quest=int(input('Digite um valor, para parar digite [999]: '))
    if quest == 999:
        break
    cont += 1
    soma += quest
print(f'Processo finalizado com sucesso, ao todo foram digitado {cont} valores, e a somatoria desses valores é igual a {soma}')