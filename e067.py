while True:
    tabu=int(input('Qual número deseja saber a tabuada? '))
    if tabu <= 0:
        break
    for c in range (1, 11):
        print(f'{tabu}x{c}={tabu*c}')
print('Tabuada encerrada. Tenha um bom dia!')