import math
selecionar_formula = input("Informe a formula a seguir:\nA ==> área\nAB ==> área base\nAT ==> área total\nV ==> volume\n==>: ").upper()

#Formula da área
if selecionar_formula == "A":
    lado = float(input("Informe o lado do prisma: "))
    altura = float(input("Informe a altura do prisma: "))
    area = lado * altura
    print(f"A área do prisma é: {round(area, 2)}")
#Área da base
elif selecionar_formula == "AB":
    selecionar_base = input("Informe a base a seguir: \nBT ==> base triangular\nBQ ==> base quadrado\nBR ==> base retangular\nBHR ==> base hexagonal regular\nBC ==> base circular\n").upper()
    #Formula da base triangular
    if selecionar_base == "BT":
        base = float(input("\nInforme a base triangular do prisma: "))
        altura = float(input("Informe a altura correspondente à base: "))
        base_triangular = (base * altura) / 2
        print(f"A base triangular do prisma é: {round(base_triangular, 2)}")
    #Formula da base quadrangular
    elif selecionar_base == "BQ":
        lado = float(input("\nInforme o lado da base quadrangular do prisma: "))
        base_quadrado = lado * lado
        print(f"A base quadrangular do prisma é: {round(base_quadrado, 2)}")
    #Formula da base retangular
    elif selecionar_base == "BR":
        largura = float(input("\nInforme a largura da base retangular do prisma: "))
        comprimento = float(input("Informe o comprimento da base retangular do prisma: "))
        base_retangular = largura * comprimento
        print(f"A base retangular do prisma é: {round(base_retangular, 2)}")
    #Formula da base hexagonal
    elif selecionar_base == "BHR":
        lado = float(input("\nInforme o lado da base hexagonal do prisma: "))
        base_hexagonal = (((lado * lado) * 3) * math.sqrt(3)) / 2
        print(f"A base hexagonal do prisma é: {round(base_hexagonal, 2)}")
    #Formula da base cilindrica
    elif selecionar_base == "BC":
        raio = float(input("\nInforme o raio da base circular do prisma: "))
        base_circular = 3.14 * (raio * raio)
        print(f"A base circular do prisma é: {round(base_circular, 2)}")
    else:
        print("Erro, formula inválida!")
#Formula da área total
elif selecionar_formula == "AT":
    area_base = float(input("Informe a area base do prisma: "))
    area_lateral = float(input("Informe a area lateral do prisma: "))
    area_total = area_base + (2 * area_lateral)
    print(f"A área total do prisma é: {round(area_total, 2)}")
#Formula do volume
elif selecionar_formula == "V":
    area_base = float(input("Informe a area base do prisma: "))
    altura = float(input("Informe a altura do prisma: "))
    volume = area_base * altura
    print(f"O volume do prisma é: {round(volume, 2)}")