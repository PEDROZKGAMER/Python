Conversor_atual = input("Informe o tipo atual abaixo:\nB ==> Binário\nD ==> Decimal\nH ==> Hexadecimal\nO ==> Octal\n==> ").upper()
Conversor_prox = input("Informe o próximo abaixo:\nB ==> Binário\nD ==> Decimal\nH ==> Hexadecimal\nO ==> Octal\n==> ").upper()

if(Conversor_atual == "D" and Conversor_prox == "B"):
    decimal = int(input("Informe o numero: "))

    convertimento = bin(decimal)[2:]

    print(f"O numero decimal '{decimal}' pra binário ==> {convertimento}")
elif(Conversor_atual == "B" and Conversor_prox == "D"):
    decimal = input("Informe o numero: ")

    convertimento = int(decimal, 2)

    print(f"O numero em binario {decimal} pra decimal é ==> {convertimento}")
elif(Conversor_atual == "H" and Conversor_prox == "D"):
    hexadecimal = input("Informe o valor em hexadecimal: ").upper()

    convertimento = int(hexadecimal, 16)

    print(f"O numero hexadecimal {hexadecimal} pra decimal é ==> {convertimento}")
elif(Conversor_atual == "D" and Conversor_prox == "H"):
    decimal = int(input("Informe o valor em decimal: "))

    convertimento = hex(decimal)[2:]
    
    print(f"O número em decimal {decimal} pra hexadecimal é ==> {convertimento.upper()}")
elif(Conversor_atual == "O" and Conversor_prox == "D"):
    octal = input("Informe o valor em octal: ")

    convertimento = int(octal, 8)

    print(f"O numero em octal {octal} pra decimal é ==> {convertimento}")
elif(Conversor_atual == "D" and Conversor_prox == "O"):
    decimal = int(input("Informe o valor em decimal: "))

    convertimento = oct(decimal)[2:]

    print(f"O numero em decimal {decimal} pra octal é ==> {convertimento}")
elif(Conversor_atual == "H" and Conversor_prox == "B"):
    hexadecimal = input("Informe o valor: ").upper()

    convertimento = bin(int(hexadecimal, 16))[2:]

    print(f"O numero em hexadecimal {hexadecimal} pra binário é ==> {convertimento}")
elif(Conversor_atual == "B" and Conversor_prox == "H"):
    binario = input("Informe o valor em binario: ")

    convertimento = hex(int(binario, 2))[2:]

    print(f"O numero em binário {binario} pra hexadecimal é ==> {convertimento.upper()}")
else:
    print("Convertimento inválido!!")


    