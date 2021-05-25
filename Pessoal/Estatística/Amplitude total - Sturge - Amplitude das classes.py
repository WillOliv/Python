print("A -> Amplitude Total \n\
B -> Regra do logaritmo (Sturges) \n\
C -> Amplitude das Classes \n")

tipo = input('Escolha uma opção : ').upper()

if tipo == "A" :
    xmax = float(input("Insira xmax : "))
    xmin = float(input("Insira xmin : "))
    AT = (xmax - xmin)
    print("A amplitude total é : {}".format(AT))

if tipo == "B" :
    n = float(input("Insira n : "))
    print("A fórmula de k é : 1 + 3,3 * log({})".format(n))

if tipo == "C" :
    AT = float(input("Insira a Amplitude Total(AT) : "))
    k = float(input("Insira a Amplitude das Classes(k) : "))
    h = (AT/k)
    print("A amplitude das classes(h) é :  {}".format(h))
