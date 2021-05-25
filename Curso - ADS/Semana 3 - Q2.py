'''Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
o total a pagar com desconto de 10%;
o valor de cada parcela, no parcelamento de 3x sem juros;
a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)'''

v = int(input('Digite um valor : '))

desc = (v * 90/100)
par = (v / 3)
c1 = (95/100 * desc)
c2 = (v* 95/100)

print(20 * '-')
print('Valor a pagar com 10% de desconto : R${}'.format(desc))
print('Valor a pagar parcenlando em 3x : R${:.2f}'.format(par))
print('\t')
print('Comissão caso pague à vista : R${}'.format(c1))
print('Comissão caso pague parcelado : R${}'.format(c2))
