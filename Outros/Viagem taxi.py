distancia = int (input ('Qual a distância a percorrer em Km?'))

km1 = 0.50
km2 = 0.45

if distancia <= 200:
    print (distancia * km1 )

if distancia > 200:
    print (distancia * km2)
