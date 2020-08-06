soma = 0
idade = 0
contador = 0
maior = 0
for c in range(1, 5):
    print('{} pessoa'.format(c))
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = int(input('SEXO [1] Feminino [2] Masculino: '))
    soma += idade
    media = soma/4
    if sexo == 1 and idade < 20:
        contador += + 1
    if sexo == 2:
      if idade > maior:
          maior = idade
          nom = nome
    else:
          nom = 'Não tem homem na lista'
print('Média de idade: {}'.format(media))
print('Nome do homem mais velho: {}'.format(nom))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(contador))