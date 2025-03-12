sexos = []
alturas = []
masculino = 0
feminino = 0
soma_altura = 0

while True:
    try:
        sexo = input("Informe o sexo da pessoa (M/F) ou 'OK' para encerrar: ").upper()

        if sexo == "OK":
            print("Comando encerrado!!")
            break

        if sexo == "M":
            masculino += 1
            sexos.append(sexo)
        elif sexo == "F":
            feminino += 1
            sexos.append(sexo)
        else:
            print("Erro, sexo inválido!! Informe apenas 'M' ou 'F'.")
            continue
        while True:
            try:
                altura = float(input("Informe a altura: "))
                if altura < 0.5 or altura >= 2.0:
                    print("Erro, altura inválida! Informe um valor entre 0.5 e 2.0 metros.")
                else:
                    alturas.append(altura)
                    soma_altura += altura
                    break
            except ValueError:
                print("Erro, insira um número válido para altura.")

    except ValueError:
        print("Erro, entrada inválida!!")

soma_sexo = masculino + feminino
media = soma_altura / soma_sexo if soma_sexo > 0 else 0

print("\n===== RESULTADOS =====")
print("Lista de sexos informados:", sexos)
print("Lista de alturas informadas:", alturas)
print("Quantidade total de pessoas:", soma_sexo)
print(f"Soma das alturas: {soma_altura:.2f}")
print(f"Média de altura: {media:.2f}")
