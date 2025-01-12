selecionar_tempe = input("Informe a temperatura atual onde (C ou c --> Celsius || K ou k --> kelvin || F ou f --> Fahren): ")
valor = float(input("informe o valor: "))
selecionar_t_prox = input("Informe a proxima temperatura: ")

celsius = "C" and "c"
Kelvin = "K" and "k"
fahren = "F" and "f"

#De cesius pra fah e kelvin
formula_fahrenheit_C = (valor * 9 / 5) + 32
formula_kelvin_C = valor + 273.15

#De fah para celsius
formula_celsius_F = (valor - 32) * 5/9
formula_kelvin_F = (valor - 32) * 5/9 + 273.15

#De kelvin para fah e celsius
formula_celsius_K = valor - 273.15
formula_fahrenheit_K = (valor - 273.15) * 9/5 + 32

#Celsius
if selecionar_tempe == celsius and selecionar_t_prox == Kelvin:
    print(f"{formula_kelvin_C}")
elif selecionar_tempe == celsius and selecionar_t_prox == fahren:
    print(f"{formula_fahrenheit_C}")
#Fahren
elif selecionar_tempe == fahren and selecionar_t_prox == celsius:
    print(f"{formula_celsius_F}")
elif selecionar_tempe == fahren and selecionar_t_prox == Kelvin:
    print(f"{formula_kelvin_F}")
#Kelvin
elif selecionar_tempe == Kelvin and selecionar_t_prox == celsius:
    print(f"{formula_celsius_K}")
elif selecionar_tempe == Kelvin and selecionar_t_prox == fahren:
    print(f"{formula_fahrenheit_K}")