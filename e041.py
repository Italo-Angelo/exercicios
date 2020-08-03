from datetime import date

atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
cals = atual - ano 
if cals <= 9:
    print('Atleta mirim')
elif cals <=14:
    print('Atleta infantil')
elif cals <=19:
    print('Atleta júnior')
elif cals <=25:
    print('Atleta sênior')
else:
    print('Atleta Master')