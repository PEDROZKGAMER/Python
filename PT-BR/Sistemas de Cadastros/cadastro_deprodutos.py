Produtos = []
id_atuais = 1
Produtos_removidos = []

while(True):
    print("\n#==== Bem-vindo ao sistema de cadastro de produtos! ====#")
    opcao = int(input("Informe a opção abaixo: \n1 ==> Cadastrar produto\n2 ==> Listar produtos\n3 ==> Alterar produto\n4 ==> Remover produto\n5 ==> Listar produtos removidos\n6 ==> Sair\n==> "))

    if(opcao == 1):
        while True:
            cadastrar_produto = input("\nInforme o nome do produto: ").upper().strip()

            if cadastrar_produto == "":
                print("Por favor, preencher o nome do produto!")
                continue

            preco = float(input(f"Informe o preço do {cadastrar_produto}: "))

            if preco < 0:
                print("Preço do produto inválido! Por favor informar o preço correto!")
                continue

            quantidade = int(input(f"Informe a quantidade de {cadastrar_produto} que possui: "))

            if quantidade < 0:
                print("Erro, quantidade inválida, por favor informar a quantidade correta!")
                continue

            while True:
                confirmar = input("\nVocê deseja cadastrar esse produto?: (S/N) ").upper().strip()

                if confirmar in ["S", "N"]:
                    break
                print("Erro, opção inválida! Por favor informar a opção válida!")

            if confirmar == "N":
                print(f"Produto {cadastrar_produto} não cadastrado!")
            else:
                produto = {"ID": id_atuais, "Nome": cadastrar_produto, "Preço": preco, "Quantidade": quantidade}
                Produtos.append(produto)
                print(f"O produto {cadastrar_produto} foi cadastrado com sucesso!")
                id_atuais += 1

                while(True):
                    sair = input("\nDeseja cadastrar outro produto?: (S/N) ").upper().strip()

                    if sair == "N":
                        print("Voltando pro menu...")
                        break
                    elif(sair == "S"):
                        continue
                    else:
                        print("Opção inválida!")
                
    elif(opcao == 2):
        if Produtos == []:
            print("\nErro, nenhum produto cadastrado ainda!")
        else:
            print("\nLista dos produtos cadastrados!")
            for produto in Produtos:
                print(f"ID do produto: {produto['ID']} | Nome do produto: {produto['Nome']} | Preço do produto: {produto['Preço']} | Quantidade: {produto['Quantidade']}")
            print(f"Quantidade de produtos: {len(Produtos)}")
    elif(opcao == 3):
        if Produtos == []:
            print("\nErro, nenhum produto cadastrado ainda!")
        else:
            print("\nLista dos produtos cadastrados!")
            for produto in Produtos:
                print(f"ID do produto: {produto['ID']} | Nome do produto: {produto['Nome']} | Preço do produto: {produto['Preço']} | Quantidade: {produto['Quantidade']}")
            print(f"Quantidade de produtos: {len(Produtos)}")
        
        alterar_produto_id = int(input("Informe o id do produto para altera-lo: "))

        for alteracao in Produtos:
            if(alteracao['ID'] == alterar_produto_id):
                print("Produto encontrado. Deixe em branco se não quiser alterar algum campo.")
                alterar_produto = int(input("Informe alguma opção pra alterar algum dado do produto:\n1 ==> Alterar nome\n2 ==> Alterar o preço\n3 ==> Alterar a quantidade\n==> "))

                if(alterar_produto == 1):
                    novo_nome = input("Informe o nome do produto: ").upper().strip()

                    alteracao['Nome'] = novo_nome

                    confirmacao = input("Deseja mesmo alterar esse dado? (S/N)").upper()

                    if(confirmacao == "N"):
                        break
                elif(alterar_produto == 2):
                    novo_preco = float(input("Informe o preço do produto: "))

                    alteracao['Preço'] = novo_preco

                    confirmacao = input("Deseja mesmo alterar esse dado? (S/N)").upper()

                    if(confirmacao == "N"):
                        break
                elif(alterar_produto == 3):
                    nova_quantidade = int(input("Informe a nova quantidade desse produto: "))

                    alteracao['Quantidade'] = nova_quantidade

                    confirmacao = input("Deseja mesmo alterar esse dado? (S/N)").upper()

                    if(confirmacao == "N"):
                        break
                else:
                    print("Erro, esta opção não existe. Por favor inserir a opção correta!")
                    continue
            else:
                print("Id do produto não encontrado!")
    elif(opcao == 4):
        if Produtos == []:
            print("\nErro, nenhum produto cadastrado ainda!")
        else:
            print("\nLista dos produtos cadastrados!")
            for produto in Produtos:
                print(f"ID do produto: {produto['ID']} | Nome do produto: {produto['Nome']} | Preço do produto: {produto['Preço']} | Quantidade: {produto['Quantidade']}")
            print(f"Quantidade de produtos: {len(Produtos)}")

            id_do_produto = int(input("Informe o id do produto a ser removido: "))

            for pr0duto in Produtos:
                if pr0duto['ID'] == id_do_produto:
                    Produtos.remove(pr0duto)
                    Produtos_removidos.append(pr0duto)
                    print(f"\nO produto {pr0duto['Nome']} foi removido com sucesso!")
                    break
            else:
                print("Erro, id de produto inválido!")
    elif(opcao == 5):
        if Produtos_removidos == []:
            print("\nErro, nenhum produto removido ainda!")
        else:
            print("\nLista dos produtos removidos!")
            for produto in Produtos_removidos:
                print(f"ID do produto: {produto['ID']} | Nome do produto: {produto['Nome']} | Preço do produto: {produto['Preço']} | Quantidade: {produto['Quantidade']}")
            print(f"Quantidade de produtos: {len(Produtos_removidos)}")

            id_do_produto_removido = int(input("Informe o id do produto removido para restaurar: "))

            for pr0duto in Produtos_removidos:
                if pr0duto['ID'] == id_do_produto_removido:
                    Produtos_removidos.remove(pr0duto)
                    Produtos.append(pr0duto)
                    print(f"\nO produto {pr0duto['Nome']} foi restaurado com sucesso!\nVoltando pro menu anterior")
                    break
            else:
                print("Erro, ID do produto inválido!")
    elif(opcao == 6):
        print("\nPrograma encerrando, até mais!")
        break
    else:
        print("\nOpção inválida! Tente novamente.")
