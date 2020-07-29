a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
ma = a 
if (b > ma):
    ma = b
if (c > ma):
    ma = c
print('O maior número é {}'.format(ma))
mn = a
if (b < mn):
    mn = b
if (c < mn):
    mn = c
print('O menor número é {}'.format(mn))