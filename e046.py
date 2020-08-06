import emoji
from time import sleep
print('''[1]SIM
[2]NÃO''')
sim = int(input('E ai, preparado para os fogos?'))
if sim ==1:
    for c in range(10, 0, -1):
        print(c)
        sleep(1)
    print(emoji.emojize(':fireworks:'))
else:
    print('OK, até a próxima!')