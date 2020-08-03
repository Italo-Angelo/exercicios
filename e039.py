from datetime import date

ano = date.today().year
na = int(input('Digite o ano em que você nasceu: '))
idade= ano - na
anoal = na + 18 
if idade == 18:
    print('CORRE, QUEM NASCEU EM {} DEVE SE ALISTAR IMEDIATAMENTE. COM {} ANOS VOCÊ JÁ DEVE ESTAR CAPINANDO CALÇADA!'.format(na, idade))
elif idade > 18:
    print('Com {} anos você já deveria ter se alistado em {}'.format(idade, anoal))
else:
    print('Você ainda é um feto, só vai precisar se alistar em {}!'.format(anoal))