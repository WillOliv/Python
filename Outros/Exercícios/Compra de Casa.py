valor = int (input ('Qual o valor da casa?'))
tempo = int (input ('Por quantos anos você vai pagar a casa?'))
salario = int (input ('Qual o valor do salário?'))

ano = (tempo * 12)
pm = (valor / ano)

porcentagem = salario * 30/100

if pm > porcentagem :
    print ('Você não pode pagar por essa casa')
if pm < porcentagem :
    print ('Você pode pagar por essa casa, o valor a ser pago é :', pm, 'mensais')
    
