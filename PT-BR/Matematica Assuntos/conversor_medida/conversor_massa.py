medida_atual = input("Informe a medida atual:\nTM --> tonelada métrica\nKG --> quilograma\nGM --> grama\nML --> miligrama\nMG --> micrograma\nTD --> tonelada de deslocamento\nTC --> tonelada curta\nST --> stone\nLB --> libra\nON --> onça\n-->:").upper()
converter_para = input("Informe a proxima medida:\nTM --> tonelada métrica\nKG --> quilograma\nGM --> grama\nML --> miligrama\nMG --> micrograma\nTD --> tonelada de deslocamento\nTC --> tonelada curta\nST --> stone\nLB --> libra\nON --> onça\n-->: ").upper()
valor = float(input("Informe o valor: "))

if medida_atual == "TM" and converter_para == "KG":
    converter = valor * 1000
    print(f"{valor}°TM --> {converter}°KG")

elif medida_atual == "TM" and converter_para == "GM":
    converter = valor * 1_000_000
    print(f"{valor}°TM --> {converter}°GM")

elif medida_atual == "TM" and converter_para == "ML":
    converter = valor * 1_000_000_000
    print(f"{valor}°TM --> {converter}°ML")

elif medida_atual == "TM" and converter_para == "MG":
    converter = valor * 1000000000000
    print(f"{valor}°TM --> {converter}°MG")

elif medida_atual == "TM" and converter_para == "TC":
    converter = valor * 1.10231
    print(f"{valor}°TM --> {converter}°TC")

elif medida_atual == "TM" and converter_para == "ST":
    converter = valor * 1.10231
    print(f"{valor}°TM --> {converter}°ST")

elif medida_atual == "TM" and converter_para == "LB":
    converter = valor * 2204.62
    print(f"{valor}°TM --> {converter}°LB")

elif medida_atual == "TM" and converter_para == "ON":
    converter = valor * 35274
    print(f"{valor}°TM --> {converter}°ON")
