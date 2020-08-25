sex = str(input('''Digite seu sexo:
[M] Masculino
[F] Feminino
''')).strip().upper()
while sex not in 'FM':
    sex = str(input('\033[1;31mOpção invalida, tente novamente: ')).strip().upper()
print('\033[1;32mSexo {} registrado com sucesso!'.format(sex))