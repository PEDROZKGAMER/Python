medida_atual = input("Informe a medida atual: ")
valor = float(input("Informe o valor: "))
converter_para = input("Informe a medida que queira inverter: ")

metro = "m"
centimetros = "cm"
quilometro = "km"
milimetro = "mm"
decimetro = "dm"
decametro = "dam"
hectometro = "hm"

conversao_realizada = False

#Metros para ...
if medida_atual == metro and converter_para == centimetros:
    print(f"{valor}m --> {valor * 100}cm")
    conversao_realizada = True
elif medida_atual == metro and converter_para == quilometro:
    print(f"{valor}m --> {valor / 1000}km")
    conversao_realizada = True
elif medida_atual == metro and converter_para == milimetro:
    print(f"{valor}m --> {valor * 1000}mm")
    conversao_realizada = True
elif medida_atual == metro and converter_para == decimetro:
    print(f"{valor}m --> {valor * 10}dm")
    conversao_realizada = True
elif medida_atual == metro and converter_para == decametro:
    print(f"{valor}m --> {valor / 10}dam")
    conversao_realizada = True
elif medida_atual == metro and converter_para == hectometro:
    print(f"{valor}m --> {valor / 100}hm")
    conversao_realizada = True

#centimetros para ...
if medida_atual == centimetros and converter_para == metro:
    print(f"{valor}cm --> {valor / 100}m")
    conversao_realizada = True
elif medida_atual == centimetros and converter_para == quilometro:
    print(f"{valor}cm --> {valor / 100000}km")
    conversao_realizada = True
elif medida_atual == centimetros and converter_para == decimetro:
    print(f"{valor}cm --> {valor / 10}dm")
    conversao_realizada = True
elif medida_atual == centimetros and converter_para == decametro:
    print(f"{valor}cm --> {valor / 1000}dam")
    conversao_realizada = True
elif medida_atual == centimetros and converter_para == hectometro:
    print(f"{valor}cm --> {valor / 10000}hm")
    conversao_realizada = True
elif medida_atual == centimetros and converter_para == milimetro:
    print(f"{valor}cm --> {valor * 10}mm")
    conversao_realizada = True

#Quilometros para ...
if medida_atual == quilometro and converter_para == metro:
    print(f"{valor}km --> {valor * 1000}m")
    conversao_realizada = True
elif medida_atual == quilometro and converter_para == centimetros:
    print(f"{valor}km --> {valor * 100000}cm")
    conversao_realizada = True
elif medida_atual == quilometro and converter_para == decimetro:
    print(f"{valor}km --> {valor * 10000}dm")
    conversao_realizada = True
elif medida_atual == quilometro and converter_para == decametro:
    print(f"{valor}km --> {valor * 100}dam")
    conversao_realizada = True
elif medida_atual == quilometro and converter_para == hectometro:
    print(f"{valor}km --> {valor * 10}hm")
    conversao_realizada = True
elif medida_atual == quilometro and converter_para == milimetro:
    print(f"{valor}km --> {valor * 1000000}mm")
    conversao_realizada = True

#milimetro para ...
if medida_atual == milimetro and converter_para == metro:
    print(f"{valor}mm --> {valor / 1000}m")
    conversao_realizada = True
elif medida_atual == milimetro and converter_para == quilometro:
    print(f"{valor}mm --> {valor / 1000000}km")
    conversao_realizada = True
elif medida_atual == milimetro and converter_para == decimetro:
    print(f"{valor}mm --> {valor / 100}dm")
    conversao_realizada = True
elif medida_atual == milimetro and converter_para == decametro:
    print(f"{valor}mm --> {valor / 10000}dam")
    conversao_realizada = True
elif medida_atual == milimetro and converter_para == hectometro:
    print(f"{valor}mm --> {valor / 100000}hm")
    conversao_realizada = True
elif medida_atual == milimetro and converter_para == centimetros:
    print(f"{valor}mm --> {valor / 10}cm")
    conversao_realizada = True

#decimetro para ...
if medida_atual == decimetro and converter_para == metro:
    print(f"{valor}dm --> {valor / 10}m")
    conversao_realizada = True
elif medida_atual == decimetro and converter_para == quilometro:
    print(f"{valor}dm --> {valor / 10000}km")
    conversao_realizada = True
elif medida_atual == decimetro and converter_para == centimetros:
    print(f"{valor}dm --> {valor * 10}cm")
    conversao_realizada = True
elif medida_atual == decimetro and converter_para == decametro:
    print(f"{valor}dm --> {valor / 100}dam")
    conversao_realizada = True
elif medida_atual == decimetro and converter_para == hectometro:
    print(f"{valor}dm --> {valor / 1000}hm")
    conversao_realizada = True
elif medida_atual == decimetro and converter_para == milimetro:
    print(f"{valor}dm --> {valor * 100}mm")
    conversao_realizada = True

#decametro para ...
if medida_atual == decametro and converter_para == metro:
    print(f"{valor}dam --> {valor * 10}m")
    conversao_realizada = True
elif medida_atual == decametro and converter_para == quilometro:
    print(f"{valor}dam --> {valor / 100}km")
    conversao_realizada = True
elif medida_atual == decametro and converter_para == decimetro:
    print(f"{valor}dam --> {valor * 100}dm")
    conversao_realizada = True
elif medida_atual == decametro and converter_para == centimetros:
    print(f"{valor}dam --> {valor / 1000}cm")
    conversao_realizada = True
elif medida_atual == decametro and converter_para == hectometro:
    print(f"{valor}dam --> {valor / 10}hm")
    conversao_realizada = True
elif medida_atual == decametro and converter_para == milimetro:
    print(f"{valor}dam --> {valor * 10000}mm")
    conversao_realizada = True

#hectometro para ...
if medida_atual == hectometro and converter_para == metro:
    print(f"{valor}hm --> {valor * 100}m")
    conversao_realizada = True
elif medida_atual == hectometro and converter_para == quilometro:
    print(f"{valor}hm --> {valor / 10}km")
    conversao_realizada = True
elif medida_atual == hectometro and converter_para == decimetro:
    print(f"{valor}hm --> {valor / 1000}dm")
    conversao_realizada = True
elif medida_atual == hectometro and converter_para == decametro:
    print(f"{valor}hm --> {valor * 10}dam")
    conversao_realizada = True
elif medida_atual == hectometro and converter_para == centimetros:
    print(f"{valor}hm --> {valor * 10000}cm")
    conversao_realizada = True
elif medida_atual == hectometro and converter_para == milimetro:
    print(f"{valor}hm --> {valor * 100000}mm")
    conversao_realizada = True

if not conversao_realizada:
    print("Erro, não existe esse tipo de medida!")