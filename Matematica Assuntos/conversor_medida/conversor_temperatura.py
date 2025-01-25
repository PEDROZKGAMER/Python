selecionar_tempe = input("Informe a temperatura atual:\nC--> Celsius\nK --> kelvin\nF --> Fahren\n-->: ").upper()
selecionar_t_prox = input("Informe a proxima temperatura:\nC--> Celsius\nK --> kelvin\nF --> Fahren\n-->: ").upper()

try:
    valor = float(input("Informe o valor da temperatura: "))
except ValueError:
    print("Por favor, insira um número válido.")
    exit()


#Celcius
if selecionar_tempe == "C" and selecionar_t_prox == "K":
    resultado = valor + 273.15
    print(f"{valor}°C equivale a {round(resultado, 2)}°K")
elif selecionar_tempe == "C" and selecionar_t_prox == "F":
    resultado = (valor * 9 / 5) + 32
    print(f"{valor}°C equivale a {round(resultado, 2)}°F")
#Kelvin
elif selecionar_tempe == "K" and selecionar_t_prox == "C":
    resultado = valor - 273.15
    print(f"{valor} K equivale a {round(resultado, 2)}°C")
elif selecionar_tempe == "K" and selecionar_t_prox == "F":
    resultado = (valor - 273.15) * 9 / 5 + 32
    print(f"{valor} K equivale a {round(resultado, 2)}°F")
#Fahreint
elif selecionar_tempe == "F" and selecionar_t_prox == "C":
    resultado = (valor - 32) * 5 / 9
    print(f"{valor}°F equivale a {round(resultado, 2)}°C")
elif selecionar_tempe == "F" and selecionar_t_prox == "K":
    resultado = (valor - 32) * 5 / 9 + 273.15
    print(f"{valor}°F equivale a {round(resultado, 2)} K")
else:
    print("Opção inválida! Verifique as entradas de temperatura.")