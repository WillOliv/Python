km = int (input('Qual a velocidade percorrida?'))
multa = (km - 80)

if (km <= 80):
    print ('Tudo certo')
if (km > 80):
    print ('Você ultrapassou o limite de velocidade'), print ('Sua multa é de :',multa,'R$')
