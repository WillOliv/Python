'''Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule e exiba na
tela o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.'''

km = float(input('Quantos Km você percorreu? '))
dia = int(input('Por quantos dias você permaneceu com ele? '))

preco1 = 0.15
preco2 = 60

r1 = (km * 0.15)
r2 = (dia * 60)

print(15 * '-')
print('Preço por Km rodados : R${} \nPreço por dia : R${} '.format(preco1, preco2))
print(15*'-')
print('Km percorridos : {} \nDias de permanência : {}'.format(km, dia))
print('Km : R${} \nDias : R${} \nTotal : R${}'.format(r1, r2, r1+r2))
