numerador = int(input("Informe a tabuada do numero: "))
operador = input("Informe o operador artimético queira calcular, onde(+ --> soma, - --> sub, * --> multi, / --> div): ")

if numerador <= 0:
    print("Erro, tabuada inválida!")
    exit()

soma = "+"
subtracao = "-"
divisao = "/"
multiplicacao = "*"

if operador == soma:
    print("\n\nTabuada da soma!")
    for x in range(11):
        print(f"{x} + {numerador} = {x + numerador}")
elif operador == subtracao:
    print("\n\nTabuada da subtração!")
    for y in range(11):
        print(f"{numerador} - {y} = {numerador - y}")
elif operador == multiplicacao:
    print("\n\nTabuada da multi!")
    for z in range(11):
        print(f"{z} * {numerador} = {z * numerador}")
elif operador == divisao:
    print("\n\nTabuada da divisão!")
    for w in range(1, 11):
        print(f"{numerador} / {w} = {numerador / w}")
else:
    print("Erro, não existe este operador!")
    exit()