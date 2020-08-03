nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1+nota2)/2
if media <= 5.0:
    print('Você não alcançou a nota, precisava de 7.0 pontos, e tirou somente {}. Com tudo, você reprovou.'.format(media))
elif media <= 6.9:
    print('Você não alcançou a nota, precisava de 7.0 pontos e tirou somente {}. Entretando, não reprovou, apenas esta de recuperação.'.format(media))
else:
    print('Parabéns pelo seu esforço, sua média foi de {} pontos. Você passou!'.format(media))