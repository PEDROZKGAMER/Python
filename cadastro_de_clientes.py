clientes = []
id_atual = 1
clientes_removidos = []

while True:
    opcao = int(input("\nInforme a opção abaixo:\n1 ==> Cadastrar clientes\n2 ==> Quantidade de clientes\n3 ==> Remoção do cliente\n4 ==> Restaurar cliente\n5 ==> Sair do programa\n==> "))

    if(opcao == 1):
        while(True):
            nome = input("Informe o nome do cliente: ").strip().upper()

            if(nome == ""):
                print("Erro, por favor informe o nome do cliente!")
                continue

            cpf = int(input("Informe o CPF do cliente (somente números): "))

            if(cpf < 0 and cpf != ""):
                print("Erro, CPF inválido!")
                continue

            while True:
                confirmar = input("Deseja mesmo cadastrar esse cliente? (S/N): ").strip().upper()
                if confirmar in ["S", "N"]:
                    break
                print("Opção inválida! Digite apenas S ou N.")

            if confirmar == "N":
                print("Cadastro cancelado.")
            else:
                cliente = {"ID": id_atual, "Nome": nome, "CPF": cpf}
                clientes.append(cliente)
                print(f"Cliente {nome} cadastrado com sucesso com ID {id_atual}!")
                id_atual += 1
            
            sair = input("Deseja cadastrar outro cliente? (S/N): ").strip().upper()

            if(sair == "N"):
                print("Voltando ao menu principal...")
                break
    elif(opcao == 2):
        if(clientes == []):
            print("Nenhum cliente cadastrado.")
        else:
            print("\n📋 Lista de Clientes:")
            for cliente in clientes:
                print(f"ID: {cliente['ID']} | Nome: {cliente['Nome']} | CPF: {cliente['CPF']}")
            print(f"Quantidade total de clientes: {len(clientes)}")
    elif(opcao == 3):
        if(clientes == []):
            print("Nenhum cliente cadastrado.")
        else:
            print("\n📋 Lista de Clientes:")
            for c in clientes:
                print(f"ID: {c['ID']} | Nome: {c['Nome']} | CPF: {c['CPF']}")
            print(f"Quantidade total de clientes: {len(clientes)}")

            id_remover = int(input("Informe o ID do cliente que deseja remover: "))

            for cliente in clientes:
                if cliente["ID"] == id_remover:
                    clientes.remove(cliente)
                    clientes_removidos.append(cliente)
                    print(f"✅ Cliente {cliente['Nome']} removido com sucesso!")
                    break
            else:
                print("Erro, id inválido!")
                continue
    elif(opcao == 4):
        if(clientes_removidos == []):
            print("Nenhum cliente removido ainda...")
            continue
        else:
            print("\n📋 Lista de Clientes removidos:")
            for c in clientes_removidos:
                print(f"ID: {c['ID']} | Nome: {c['Nome']} | CPF: {c['CPF']}")
            print(f"Quantidade total de clientes removidos: {len(clientes_removidos)}")

        restaurar_cliente = int(input("Deseja restaurar algum cliente removido? (1 - Sim / 2 - Não): "))

        if(restaurar_cliente == 1):
            id_cliente = int(input("Informe o ID do cliente que deseja restaurar: "))

            while True:
                confirmar = input("Deseja mesmo restaurar esse cliente? (S/N): ").strip().upper()
                if confirmar in ["S", "N"]:
                    break
                print("Opção inválida! Digite apenas S ou N.")

            if confirmar == "N":
                print("Rastauração cancelado.")
            else:
                for cliente in clientes_removidos:
                    if(cliente["ID"] == id_cliente):
                        clientes.append(cliente)
                        clientes_removidos.remove(cliente)
                        print(f"Cliente {cliente['Nome']} restaurado com sucesso!\nVoltando pro menu!...")
                        break
                else:
                    print("Erro, id inválido!")
                    continue
    elif(opcao == 5):
        print("Saindo do programa...")
        break
            
            

            
