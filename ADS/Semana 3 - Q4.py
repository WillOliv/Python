'''Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte o nome,
a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. No
final exiba o nome e a quantidade total de dias perdidos. Considere que um ano sempre possui 365 dias.'''

n = input('Nome : ')
cd = int(input('Cigarros por dia : '))
a = int(input('Anos fumando : '))

ano = (a * 365)

# Anos em minutos
aem = (cd * ano * 10)

# Horas em minutos
hem = (aem / 60)

# dias em minutos
dem = (hem / 24)

print(20 * '-')
print('Nome : {} \nCigarros por dia : {} \nAnos fumando : {} \nDias perdidos : {:.1f}'.format(n, cd, a, dem))
