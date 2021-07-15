'''Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metros e
cresce 3 centímetros por ano. Escreva um programa que calcule e imprima quantos anos
serão necessários para que Zé seja maior que Chico.'''

chico = 150
ze = 110
anos = 0

while chico >= ze:
    chico = (chico + 2)
    ze = (ze + 3)
    anos = (anos + 1)
    
print('Demorará {} anos para que Zé seja maior que Chico'.format(anos))
print('Em {} anos, Chico terá {}cm anos e Zé {}cm'.format(anos, chico, ze))
