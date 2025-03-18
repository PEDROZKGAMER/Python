import math
selecionar_formula = input("Informe a formula a seguir\nTP ==> tronco da piramide\nTC ==> tronco do cone\nTPR ==> tronco do prisma\nTCL ==> tronco do cilindro\n==>: ").upper()

#Formula do tronco da piramide
if selecionar_formula == "TP":
    altura = float(input("Informe a altura do tronco da piramide: "))
    base_maior = float(input("Informe a base maior: "))
    base_menor = float(input("Informe a base menor: "))
    tronco_piramide = (altura / 3) * (base_maior + base_menor + math.sqrt((base_maior * base_menor)))
    print(f"O tronco da piramide é: {round(tronco_piramide, 2)}")
#Formula do tronco do cone
elif selecionar_formula == "TC":
    altura = float(input("Informe a altura do tronco do cone: "))
    raio_maior = float(input("Informe o raio maior do tronco: "))
    raio_menor = float(input("Informe o raio menor do tronco: "))
    tronco_cone = ((3.14 * altura) / 3) * ((raio_maior**2) + (raio_maior * raio_menor) + (raio_menor**2))
    print(f"O tronco do cone é: {round(tronco_cone, 2)}")
#Formula do tronco do prisma
elif selecionar_formula == "TPR":
    altura = float(input("Informe a altura do tronco do prisma: "))
    base_maior = float(input("Informe a base maior do prisma: "))
    base_menor = float(input("Informe a base menor do prisma: "))
    tronco_prisma = ((altura * base_maior) + base_menor) / 2
    print(f"O tronco do prisma é: {round(tronco_prisma, 2)}")
#Formula do tronco cilindrico
elif selecionar_formula == "TCL":
    altura = float(input("Informe a altura do tronco do cilindro: "))
    raio_maior = float(input("Informe o raio maior: "))
    raio_menor = float(input("Informe o raio menor: "))
    tronco_cilindro = (3.14 * altura) * ((raio_maior * raio_maior) + (raio_menor * raio_menor))
    print(f"O tronco do cilindro é: {round(tronco_cilindro, 2)}")
else:
    print("Error, formula inválida!")