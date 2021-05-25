'''Uma casa de câmbio vende diferentes moedas para brasileiros que desejam viajar para o
exterior. O cliente informa a moeda desejada e dá um valor em reais para a compra.
O operador do caixa acessa o sistema, informa a letra inicial da moeda a ser comprada,
entra com o valor a ser convertido e o sistema informa o valor da conversão para  a nova moeda.
Implemente um programa que simula o sistema da casa de câmbio. Considere que, se mais de uma conversão
precise ser realizada, o operador do caixa executa o programa novamente. Se a moeda informada não existir
na base de conversão, indique ao usuário que a moeda é inválida.'''

print('e -> Euro : 0,31\nd -> Dólar : 0,42\nm -> Peso Mechicano : 5,55\na -> Peso Argentino : 2,84\nl -> Libra : 0,26')
print('\t')
moeda = input('Digite a moeda desejada : ')
valor = float(input('Diga o valor que deseja converter : '))
print('\t')

euro = (valor * 0.31)
dolar = (valor * 0.42)
pesoM = (valor * 5.55)
pesoA = (valor * 2.84)
libra = (valor * 0.26)

if moeda == 'e':
    print('Conversão em Euro : {}'.format(euro))
elif moeda == 'd':
    print('Conversão em Dólar : {}'.format(dolar))
elif moeda == 'm':
    print('Conversão em Peso Mexicano : {}'.format(pesoM))
elif moeda == 'a':
    print('Conversão em Peso Argentino : {}'.format(pesoA))
elif moeda == 'l':
    print('Conversão em Libra : {}'.format(libra))
else:
    print('Moeda não encontada')
print('\t')
print('Para fazer outra conversão, reinicie o programa.')
