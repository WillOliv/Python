numero = int(input('Digite o número base para a tabuada : '))

print(20 * '-')
print('A tabuada de {} é : '.format(numero))
print('\t')

for tabuada in range(1, 11, 1):
    print('{} x {} = {}'.format(numero, tabuada, numero * tabuada))

print(20 * '-')
