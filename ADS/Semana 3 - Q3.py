'''Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente
ao valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada
apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com
base no valor investido.'''

premio = int(input('Digite o valor do prêmio : '))
a1 = int(input('amigo 1: '))
a2 = int(input('amigo 2: '))
a3 = int(input('amigo 3: '))
print('\t')

total = (a1 + a2 + a3)

porc1 = (100 * a1/total)
porc2 = (100 * a2/total)
porc3 = (100 * a3/total)

valor1 = (premio * porc1/100)
valor2 = (premio * porc2/100)
valor3 = (premio * porc3/100)

print('Valor apostado : {}'.format(total))
print(30*'-')
print('Porcentagens : \nPrimeiro amigo : {:.1f}% \nSegundo amigo : {:.1f}% \nTerceiro amigo : {:.1f}%'.format(porc1, porc2, porc3))
print(30*'-')
print('Distribuição : \nPrimeiro amigo : {:.1f} \nSegundo amigo : {:.1f} \nTerceiro amigo : {:.1f}'.format(valor1, valor2, valor3))
