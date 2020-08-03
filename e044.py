preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] Em dinheiro
[2] à vista no cartão
[3] 2x no cartão
[4] 4x no cartão''')
vista = preço-((10*preço)/100)
viscar = preço-((5*preço)/100)
cartao3 = preço+((20*preço)/100)
cartao2 = preço /2
como = int(input('Qual é a opção de pagamento?'))
if como == 1:
    print('Sua compra de R${} a vista recebe um desconto de 10%, custando agora R${}'.format(preço, vista)) 
elif como ==2:
    print('Sua compra de R${} a vista no cartão recebe um desconto de 5%, custando agora R${}'.format(preço, viscar))
elif como ==3:
    print('Sua compra ficou parcelada em 2x de R${} sem juros'.format(cartao2))
elif como ==4:
    a=int(input('Quantas parcelas?'))
    b = cartao3/a
    print('Sua compra de R${} dividido foi dividido em {}x, ficando no valor de R${} por parcela, com um valor final de {} devido ao aumento de 20% de juros!'.format(preço, a, b, cartao3))
else:
    print('Opção invalida, tente novamente.')