import time
Clientes = []
id_atual = 1
Clientes_removidos = []

while(True):
    try:
        opcao = int(input("\nQual opção você deseja?\n1 ==> Cadastrar cliente\n2 ==> Listar Clientes\n3 ==> Alterar Dados\n4 ==> Remover cliente\n5 ==> Restaurar cliente\n6 ==> Sair do programa\n==> "))
    except(ValueError):
        print("\nA opção tem que ser em numero!")
        continue

    if(opcao == 1):
        continuar_cadastrar = True
        while(continuar_cadastrar):
            Nome = input("Informe o nome do cliente: ").upper().strip()

            if(Nome == ""):
                print("O nome não foi informado! Por favor, digite o nome corretamente.")
                continue

            if(not all(verificar.isalpha() or verificar.isspace() for verificar in Nome)):
                print("O nome deve conter só letras!")
                continue

            while(True):
                try:
                    CPF_Cliente = int(input("Informe o CPF do cliente (somente números): "))

                    if(CPF_Cliente < 0):
                        print("O CPF não pode ser número negativo!")
                        continue

                    if(len(str(CPF_Cliente)) != 11):
                        print("CPF com números a menos ou a mais!")
                        continue

                    cpf_ja_cadastrado = any(cliente["CPF"] == CPF_Cliente for cliente in Clientes)

                    print("Verificando se ja existi esse CPF...")
                    time.sleep(8)

                    if(cpf_ja_cadastrado):
                        print("Este CPF já foi cadastrado!")
                        continue
                    else:
                        print("CPF válido.")
                        break
                except(ValueError):
                    print("O CPF tem que ser em número!")
                    continue
            while(True):
                Email = input("Informe o Email do cliente: ").strip()

                if(Email == ""):
                    print("O Email não foi informado! Por favor, digite um Email válido.")
                    continue
                email_ja_cadastrado = any(cliente["Email"].lower() == Email.lower() for cliente in Clientes)

                print("Verificando se ja existe esse email...")
                time.sleep(8)

                if(email_ja_cadastrado):
                    print("Este Email já foi registrado!")
                    continue
                else:
                    print("Email válido.")
                    break
            while(True):
                confirmar = input("Deseja cadastrar esse cliente? (S/N): ").upper()

                if(confirmar == "S"):
                    Cliente = {"ID": id_atual, "Nome": Nome, "CPF": CPF_Cliente, "Email": Email}
                    Clientes.append(Cliente)
                    id_atual += 1
                    print("Usuário registrado com sucesso!")
                    break
                elif(confirmar == "N"):
                    print("Cadastro cancelado.")
                    break
                else:
                    print("Opção inválida! Por favor, informe S ou N.")
                    continue
            while(True):
                Cadastra_outro = input("Deseja cadastrar outro cliente? (S/N): ").upper()

                if(Cadastra_outro == "S"):
                    break
                elif(Cadastra_outro == "N"):
                    print("Voltando para o menu anterior...")
                    continuar_cadastrar = False
                    break
                else:
                    print("Opção inválida! Por favor, informe S ou N.")
    elif(opcao == 2):
        if(Clientes == []):
            print("Ainda não foi cadastrados nenhum cliente!")
        else:
            print("Lista de Clientes Cadastrados!")
            for cliente in Clientes:
                print(f"ID: {cliente['ID']} | Nome: {cliente['Nome']} | CPF: {cliente['CPF']} | Email: {cliente['Email']}")
    elif(opcao == 3):
        continuar_Alteracao = True
        while continuar_Alteracao:
            if(not Clientes):
                print("Ainda não foi cadastrado nenhum cliente!")
                break

            print("Lista de Clientes Cadastrados:")
            for cliente in Clientes:
                print(f"ID: {cliente['ID']} | Nome: {cliente['Nome']} | CPF: {cliente['CPF']} | Email: {cliente['Email']}")

            try:
                ID_alterar = int(input("Informe o ID do cliente para modificar: "))
                if(ID_alterar < 0):
                    print("O ID informado não pode ser negativo!")
                    continue
            except(ValueError):
                print("O ID deve ser um número!")
                continue

            cliente_encontrado = False

            for people in Clientes:
                if(people['ID'] == ID_alterar):
                    cliente_encontrado = True
                    print(f"ID encontrado! Nome do cliente selecionado: {people['Nome']}")
                
                    try:
                        opcao_modificar = int(input("Informe a opção abaixo para modificar os dados:\n1 ==> Alterar nome\n2 ==> Alterar CPF\n3 ==> Alterar Email\n==> "))
                        
                        if(opcao_modificar < 0):
                            print("A opção não pode ser negativa!")
                            continue
                    except(ValueError):
                        print("A opção deve ser um número!")
                        continue

                    if(opcao_modificar == 1):
                        nome_antigo = people['Nome']
                        nome_novo = input("Informe o novo nome: ").strip().upper()

                        if(nome_novo == ""):
                            print("Nome inválido! Não pode estar vazio.")
                            continue
                        
                        if(not all(client.isalpha() or client.isspace() for client in nome_novo)):
                            print("Nome inválido! Use apenas letras e espaços.")
                            continue

                        confirmar = input("Deseja alterar esse dado? (S/N): ").upper()
                        if(confirmar == "S"):
                            people['Nome'] = nome_novo
                            print(f"O nome '{nome_antigo}' foi alterado para '{people['Nome']}'!")
                        else:
                            print("Alteração cancelada.")
                    elif(opcao_modificar == 2):
                        CPF_antigo = people['CPF']
                        try:
                            novo_CPF = int(input("Informe o novo CPF: "))
                            
                            if(novo_CPF < 0):
                                print("CPF não pode ser negativo!")
                                continue
                        except(ValueError):
                            print("CPF deve conter apenas números!")
                            continue

                        print("Verificando se ja existi esse CPF...")
                        time.sleep(8)

                        if(any(dadocliente["CPF"] == novo_CPF and dadocliente["ID"] != people["ID"] for dadocliente in Clientes)):
                            print("Este CPF já está em uso por outro cliente!")
                            continue

                        confirmar = input("Deseja alterar esse dado? (S/N): ").upper()
                        
                        if(confirmar == "S"):
                            people['CPF'] = novo_CPF
                            print(f"O CPF '{CPF_antigo}' foi alterado para '{people['CPF']}'!")
                        else:
                            print("Alteração cancelada.")
                    elif(opcao_modificar == 3):
                        Email_antigo = people['Email']
                        Email_novo = input("Informe o novo Email: ").strip()

                        if(Email_novo == ""):
                            print("Email inválido! Não pode estar vazio.")
                            continue

                        print("Verificando se ja existe esse email...")
                        time.sleep(8)

                        if(any(c["Email"].lower() == Email_novo.lower() and c["ID"] != people["ID"] for c in Clientes)):
                            print("Este Email já está em uso por outro cliente!")
                            continue

                        confirmar = input("Deseja alterar esse dado? (S/N): ").upper()
                        
                        if(confirmar == "S"):
                            people['Email'] = Email_novo
                            print(f"O Email '{Email_antigo}' foi alterado para '{people['Email']}'!")
                        else:
                            print("Alteração cancelada.")
                    else:
                        print("Opção inválida!")
                        break
                while(True):
                    sair = input("Deseja alterar outro dado de outo cliente? (S/N): ").upper()

                    if(sair == "S"):
                        break
                    elif(sair == "N"):
                        print("Voltando pro menu anterior")
                        continuar_Alteracao = False
                        break
                    else:
                        print("Opção inválida! Por favor informar a opção correta!")
                        continue

            if(not cliente_encontrado):
                print("ID não encontrado no banco de dados.")
    elif(opcao == 4):
        continuar_Remocao = True
        while(True):
            if(not Clientes):
                print("Ainda não foi cadastrado nenhum cliente!")
                break

            print("Lista de Clientes Cadastrados:")
            for cliente in Clientes:
                print(f"ID: {cliente['ID']} | Nome: {cliente['Nome']} | CPF: {cliente['CPF']} | Email: {cliente['Email']}")
            
            try:
                ID_cliente = int(input("Informe o ID do cliente que deseja remove-lo: "))

                if(ID_cliente < 0):
                    print("ID não pode ser negativo ou inválido!")
                    continue
            except ValueError:
                print("O ID tem que ser em número!")
                continue

            for people in Clientes:
                if(people['ID'] == ID_cliente):
                    print(f"\nID Encontrado! Nome do cliente: {people['Nome']}\n")
                    while(True):
                        confirmar = input("Deseja mesmo remover esse cliente? (S/N): ").upper()

                        if(confirmar == "S"):
                            print(f"O cliente {people['Nome']} foi removido com sucesso!")
                            Clientes.remove(people)
                            Clientes_removidos.append(people)
                            break
                        elif(confirmar == "N"):
                            break
                        else:
                            print("Opção inválida! Por favor inserir a opção correta!")
                            continue
                    
                    while(True):
                        sair = input("Deseja remover outro cliente? (S/N): ").upper()

                        if(sair == "S"):
                            break
                        elif(sair == "N"):
                            print("Voltando por menu anterior!")
                            continuar_Remocao = False
                            break
                        else:
                            print("Oção inválida! Por favor inserir a opção correta!")
                            continue
    elif(opcao == 5):
        continuar_restaurar = True
        while(continuar_restaurar):
            if(not Clientes_removidos):
                print("Ainda não foi cadastrado nenhum cliente!")
                break

            print("Lista de Clientes Cadastrados:")
            for cliente in Clientes_removidos:
                print(f"ID: {cliente['ID']} | Nome: {cliente['Nome']} | CPF: {cliente['CPF']} | Email: {cliente['Email']}")
            
            try:
                ID_removido = int(input("Informe o id do cliente removido: "))

                if(ID_removido < 0):
                    print("O ID não pode ser negativo ou inválido!")
                    continue
            except ValueError:
                print("O ID tem que ser em número!")
                continue

            for people in Clientes_removidos:
                if(people['ID'] == ID_removido):
                    print(f"O ID do cliente removido foi encontrado! Nome do cliente: {people['Nome']}")
                    
                    while(True):
                        confirmar = input("Deseja restaurar esse cliente? (S/N): ").upper()

                        if(confirmar == "S"):
                            print(f"O Cliente {people['Nome']} foi restaurado com sucesso!")
                            Clientes_removidos.remove(people)
                            Clientes.append(people)
                            break
                        elif(confirmar == "N"):
                            print("Remoção Cancelada!")
                            break
                        else:
                            print("Opção inválida! Por favor informar a opção correta!")
                            continue
                    
                    while(True):
                        sair = input("Deseja restaurar outro cliente? (S/N): ").upper()

                        if(sair == "S"):
                            break
                        elif(sair == "N"):
                            print("Voltando por menu anterior!")
                            continuar_Remocao = False
                            break
                        else:
                            print("Opção inválida! Por favor informar a opção correta!")
                            continue
    elif(opcao == 6):
        print("Encerrando o programa, Até mais!")
        break
    else:
        print("Opção inválida, por favor informar a opção correta!")
        continue





                