import math

opcao = int(input("Informe a opcao abaixo:\n1 ==> 'Calculadora normal'\n2 ==> 'Raiz quadrada'\n==> "))

if(opcao == 1):
    resultado = 0

    resultado = float(input("Informe o numero: "))

    while(True):
        operador = input("Informe o operador (+ - * /) ou o 'OK' pra finalizar o programa: ").upper()

        if(operador == "OK"):
            print("Programa finalizado!!")
            break

        if(operador != "+" and operador != "-" and operador != "*" and operador != "/"):
            print("Erro, operador inválido!!")
            continue

        numero = float(input("Informe um numero: "))
        

        if(operador == "+"):
            resultado += numero
        elif(operador == "-"):
            resultado -= numero
        elif(operador == "*"):
            resultado *= numero
        elif(operador == "/"):
            resultado /= numero
        
    
        print("Resultado parcial: ",resultado)

    print("Resultado final: ",resultado)
elif(opcao == 2):
    numero = float(input("Informe o numero: "))

    print("Não pode raiz quadrada de numero negativo" if numero < 0 else f"O resultado é {math.sqrt(numero)}")