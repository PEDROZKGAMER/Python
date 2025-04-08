

opcao_geometria = int(input("Informe a geometria que queira estadar:\n1 ==> Geometria plana\n2 ==> Geometria espacial\n3 ==> Sair: "))

if(opcao_geometria == 1):
    opcao_poligono = int(input("Informe o poligono da geometria abaixo:\n1 ==> Triangulo\n 2 ==> Ciculo\n==> "))

    if(opcao_poligono == 2):
        from Geometria_Plana import circunferencia_circulo
        circunferencia_circulo()

