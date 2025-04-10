clientes = []
id_atual = 1
clientes_removidos = []

while True:
    opcao = int(input("\nInforme a opção abaixo:\n1 ==> Cadastrar clientes\n2 ==> Quantidade de clientes\n3 ==> Remoção do cliente\n4 ==> Restaurar cliente\n5 ==> Alterar dados do cliente\n6 ==> Sair do programa\n==> "))

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

            email = input("Informe o email do cliente: ")

            if(email == ""):
                print("Email inválido! Por favor, informar o email válido!")
                continue


            while True:
                confirmar = input("Deseja mesmo cadastrar esse cliente? (S/N): ").strip().upper()
                if confirmar in ["S", "N"]:
                    break
                print("Opção inválida! Digite apenas S ou N.")

            if confirmar == "N":
                print("Cadastro cancelado.")
            else:
                cliente = {"ID": id_atual, "Nome": nome, "CPF": cpf, "Email": email}
                clientes.append(cliente)
                print(f"Cliente {nome} cadastrado com sucesso com ID {id_atual}!")
                id_atual += 1
            
            sair = input("Deseja cadastrar outro cliente? (S/N): ").strip().upper()

            if(sair == "N"):
                print("Voltando ao menu principal...")
                break
    elif(opcao == 2):
        if(clientes == []):
            print("Nenhum cliente cadastrado ainda!")
        else:
            print("Lista de clientes cadastrados!")
            for cliente in clientes:
                print(f"ID: {cliente['ID']} | Nome: {cliente['Nome']} | CPF: {cliente['CPF']} | Email: {cliente['Email']}")
            print(f"Quantidade de clientes: {len(clientes)}")
    elif(opcao == 3):
        if(clientes == []):
            print("Nenhum cliente cadastrado ainda!")
        else:
            print("Lista de clientes cadastrados!")
            for cliente in clientes:
                print(f"ID: {cliente['ID']} Nome: {cliente['Nome']} | CPF: {cliente['CPF']} | Email: {cliente['Email']}")
            print(f"Quantidade de clientes: {len(clientes)}")
        
        remover_produto = int(input("Informe o id do cliente para remove-lo: "))

        for remover in clientes:
            if(remover["ID"] == remover_produto):
                clientes.remove(remover)
                clientes_removidos.append(remover)
                print(f"{remover["Nome"]} foi removido com sucesso!")
                break
        else:
            print("ID inválido! por favor informar o id correto!")
            continue
    elif (opcao == 4):
        if(clientes_removidos == []):
            print("Nenhum cliente foi removido ainda!")
        else:
            print("Clientes removidos!")
            for cliente_removo in clientes_removidos:
                print(f"ID: {cliente_removo["ID"]} | Nome: {cliente_removo["Nome"]} | CPF: {cliente_removo["CPF"]} | Email: {cliente_removo["Email"]}")
            print(f"Quantidade de clientes removidos: {len(clientes_removidos)}")
        
        restaura_cliente = int(input("Informe o ID do cliente a ser restaurar: "))

        for restaurar in clientes_removidos:
            if(restaurar["ID"] == restaura_cliente):
                clientes_removidos.remove(restaurar)
                clientes.append(restaurar)
            print(f"O Cliente {restaurar["Nome"]}, foi restaurado com sucesso!")
            break
        else:
            print("Erro, id inválido!")
            continue
    elif(opcao == 5):
        if(clientes == []):
            print("Nenhum cliente cadastrado ainda!")
        else:
            print("Lista de clientes cadastrados!")
            for cliente in clientes:
                print(f"ID: {cliente['ID']} Nome: {cliente['Nome']} | CPF: {cliente['CPF']} | Email: {cliente['Email']}")
            print(f"Quantidade de clientes: {len(clientes)}")
        
        confirmar_se = int(input("Deseja alterar algum dado do cliente? (1 == Sim/2 ==> Não) "))

        if(confirmar_se not in [1, 2]):
            print("Opção inválida!")
            continue

        if(confirmar_se == "2"):
            print("Voltando pro menu!")
            break
        else:
            id_cliente = int(input("Informe o id do cliente para modificar algums dados: "))

            for alterar in clientes:
                if(alterar["ID"] == id_cliente):
                    opcao_alterado = int(input("Informe qual dado você deseja alterar:\n1 ==> Nome\n2 ==> CPF\n3 ==> Email\n==> "))

                    if(opcao_alterado == 1):
                        nome_antigo = cliente["Nome"]
                        novo_nome = input("Informe o novo nome pro cliente: ").upper().strip()

                        alterar["Nome"] = novo_nome

                        print(f"O {nome_antigo} foi alterado para {alterar["Nome"]} com sucesso!")
                    elif(opcao_alterado == 2):
                        CPF_antigo = cliente["CPF"]
                        cpf_novo = int(input("Em casos de erro de digitação, por favor, informar o cpf do cliente: "))

                        alterar["CPF"] = cpf_novo

                        print(f"O {CPF_antigo} foi modificado para {alterar["CPF"]}")
                    elif(opcao_alterado == 3):
                        email_antigo = cliente["Email"]
                        novo_email = input("Informe o novo email do cliente: ")

                        alterar["Email"] = novo_email

                        print(f"O email {email_antigo} foi alterado para {alterar["Email"]}")
                    else:
                        print("Erro, opção inválida!")
                else:
                    print("Erro, id inválido!")
    else:
        print("Saindo do programa, até mais!")
        break

