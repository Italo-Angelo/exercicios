so = 0
ac = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        so = so + c
        ac = ac +1
print(f'A soma dos {ac} valores, é igual a {so}')