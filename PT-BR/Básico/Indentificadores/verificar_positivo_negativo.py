numero = int(input("Informe um valor: "))

print("O valor é negativo!" if numero < 0 else "O valor é positivo!")
print("O valor é par" if numero % 2 == 0 else "O valor é impar")