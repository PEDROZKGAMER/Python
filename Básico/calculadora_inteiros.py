numero_um_int = int(input("Informe o primeiro valor: "))
numero_dois_int = int(input("Informe o segundo valor: "))
sigla = input("Qual operação matematica vai querer fazer o calculo: ")

soma = "+"
sub = "-"
multi = "*"
div = "/"

if sigla == soma:
    print(f"{numero_um_int} + {numero_dois_int} = {numero_um_int + numero_dois_int}")
elif sigla == sub:
    print(f"{numero_um_int} - {numero_dois_int} = {numero_um_int - numero_dois_int}")
elif sigla == multi:
    print(f"{numero_um_int} * {numero_dois_int} = {numero_um_int * numero_dois_int}")
elif sigla == div:
    print(f"{numero_um_int} / {numero_dois_int} = {numero_um_int / numero_dois_int}")
else:
    print("Erro, operação errada!")