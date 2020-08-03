casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual seu salario? R$'))
anos = float(input('Em quantos anos você deseja pagar o imovél?'))
calc = casa/(anos * 12)
porcento = (30 * salario)/100
if calc < porcento:
    print('Parabéns! Você foi aprovado, suas prestações ficaram no valor de R${:.2f}'.format(calc))
else:
    print('Você não foi aprovado, o valor das prestações exedem 30% do seu salario. Tenha um bom dia!')