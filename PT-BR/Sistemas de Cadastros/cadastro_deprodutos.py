import time
Produtos = []
Produtos_removidos = []
id_atual = 1

#print("Inicializando o sistema...")
#time.sleep(6)

while(True):
    try:
        opcao = int(input("\nBem Vindo ao sitema de produtos!\nSelecione uma das opções abaixo:\n1 ==> Cadastro de produtos\n2 ==> Listar produtos\n3 ==> Alterar produtos\n4 ==> Remover produtos\n5 ==> Restaurar produto\n6 ==> Encerrar o programa\n==> "))

        if(opcao < 0):
            print("Opção negativo ou inválido! Por favor inserir a opção correta!")
            continue
    except(ValueError):
        print("A opção tem ser em número, por favor inserir uma opção correta!")
        continue

    if(opcao == 1):
        continar_cadastrar = True
        while(continar_cadastrar):
            fornecedor = input("Informe o nome do fornecedor: ").upper()

            if(fornecedor == ""):
                print("O nome do fornecedor não digitado ou inválido!")
                continue

            if(not all(verificacao.isalpha() or verificacao.isspace() for verificacao in fornecedor)):
                print("O nome do fornecedor deve conter só letras!")
                continue

            while(True):
                nome_produto = input("Informe o nome do produto: ").upper()

                if(nome_produto == ""):
                    print("O produto não foi digitado ou inválido!")
                    continue

                if(not all(verificar.isalpha() or verificar.isspace() for verificar in nome_produto)):
                    print("O nome deve conter só letras, por favor inserir o nome do produto correto!")
                    continue
                break
            while(True):
                deseja_descricao = input("Deseja adicionar a descrição do produto? (S/N): ").upper()

                if(deseja_descricao == "S"):
                    descricao = input("Informe a descrição do produto: ")

                    if(descricao == ""):
                        print("A descrição não digitado ou inválido!")
                        continue
                    break
                elif(deseja_descricao == "N"):
                    descricao = "Nenhuma descrição adicionada!"
                    break
                else:
                    print("Opção inválida, por favor informar a opção correta!")
                    continue

            try:
                preco = float(input("Informe o preço do produto: "))

                if(preco < 0):
                    print("O preço do produto não pode ser negativo!")
                    continue
            except(ValueError):
                print("O preço deve ser em números!")
                continue

            try:
                quantidade = int(input("Informe a quantidade desse produto: "))

                if(quantidade < 0):
                    print("A quantidade não pode ser negativo ou inválido!")
                    continue
            except(ValueError):
                print("A quantidade tem que ser em número!")
                continue

            codigo_produto = input("Informe o código do produto: ").upper()

            if(codigo_produto == ""):
                print("O código do produto não digitado ou inválido!")
                continue

            categoria = input("Informe a categoria desse produto: ").upper()

            if(categoria == ""):
                print("A categoria do produto não digitado ou inválido!")
                continue

            if(not all(verificar_categoria.isalpha() or verificar_categoria.isspace() for verificar_categoria in categoria)):
                print("A categoria deve conter só letras!")
                continue
            
            while(True):
                confirmar = input("Deseja cadastrar esse produto? (S/N): ").upper()

                if(confirmar == ""):
                    print("A opção incorreta, por favor inserir a opção correta!")
                    continue

                if(confirmar == "S"):
                    produto = {"ID": id_atual,"Fornecedor": fornecedor,"Nome": nome_produto,"Descrição": descricao,"Categoria": categoria, "Preço": preco, "Quantidade": quantidade, "Codigo do produto": codigo_produto}
                    Produtos.append(produto)
                    id_atual += 1
                    print(f"O produto '{nome_produto}' foi cadastrado com sucesso!")
                    break
                elif(confirmar == "N"):
                    break
                else:
                    print("Opção incorreta, por favor informar a opção correta!")
                    continue
                
            while(True):
                sair = input("Deseja cadastrar outro produto? (S/N): ").upper()

                if(sair == ""):
                    print("A opção incorreta, por favor inserir a opção correta!")
                    continue

                if(sair == "S"):
                    break
                elif(sair == "N"):
                    print("Voltando pro menu anterior!")
                    continar_cadastrar = False
                    break
                else:
                    print("Opção inválida, por favor inserir a opção correta!")
                    continue
    elif(opcao == 2):
        #print("Carregando a lista...")
        #time.sleep(6)

        if(Produtos == []):
            print("Nenhum produto cadastrado ainda!")
        else:
            print("==== Lista de Produtos! ====")
            numero_produto = 1
            for produto in Produtos:
                print(f"\nProduto #{numero_produto}\nID: {produto['ID']} | Fornecedor: {produto['Fornecedor']} | Nome do produto: {produto['Nome']} | Descrição: {produto['Descrição']}\nCategoria: {produto['Categoria']} | Preço do produto: {produto['Preço']} | Quantidade: {produto['Quantidade']} | Código do produto: {produto['Codigo do produto']}")
                numero_produto += 1
    elif(opcao == 3):
        #print("Carregando a lista...")
        #time.sleep(6)

        continuar_alterar = True
        while(continuar_alterar):
            if(Produtos == []):
                print("Nenhum produto cadastrado ainda!")
            else:
                print("==== Lista de Produtos! ====")
                numero_produto = 1
                for produto in Produtos:
                    print(f"\nProduto #{numero_produto}\nID: {produto['ID']} | Fornecedor: {produto['Fornecedor']} | Nome do produto: {produto['Nome']} | Descrição: {produto['Descrição']}\nCategoria: {produto['Categoria']} | Preço do produto: {produto['Preço']} | Quantidade: {produto['Quantidade']} | Código do produto: {produto['Codigo do produto']}")
                    numero_produto += 1
            
            try:
                ID_produto = int(input("Informe o ID do produto para altera-lo: "))

                if(ID_produto < 0):
                    print("O ID do produto negativo ou inválido!")
                    continue
            except(ValueError):
                print("O ID do produto tem que ser em número!")
            
            for product in Produtos:
                if(product['ID'] == ID_produto):
                    print("Produto encontrado!")
                
                try:
                    alterar_dado = int(input("Informe a opção para altera-lo:\n1 ==> Alterar o nome do fornecedor\n2 ==> Alterar o nome do produto\n3 ==> Alterar a descrição do produto\n4 ==> Alterar a quantidade\n5 ==> Alterar a categoria\n6 ==> alterar o preço\n7 ==> alterar o código do produto\n==> "))

                    if(alterar_dado < 0):
                        print("A opção negativo ou inválido!")
                        continue
                except(ValueError):
                    print("A opção deve ser em número!")
                    continue

                if(alterar_dado == 1):
                    fornecedor_antigo = product['Fornecedor']
                    novo_fornecedor = input("Informe o novo nome do fornecedor: ")

                    if(novo_fornecedor == ""):
                        print("O fornecedor não digitado ou inválido!")
                        continue

                    while(True):
                        confirmar_alteracao = input("Deseja mesmo fazer essa alteração? (S/N): ").upper()

                        if(confirmar_alteracao == ""):
                            print("A opção não informada ou inválida!")
                            continue

                        if(confirmar_alteracao == "S"):
                            product['Fornecedor'] = novo_fornecedor
                            print(f"O nome do fornecedor {fornecedor_antigo} foi alterado para {product['Fornecedor']}!")
                            break
                        elif(confirmar_alteracao == "N"):
                            break
                        else:
                            print("Opção inválida!")
                            continue
                elif(alterar_dado == 2):
                    produto_antigo = product['Nome']
                    novo_produto = input("Informe o novo nome do produto: ")

                    if(novo_produto == ""):
                        print("O produto não digitado ou inválido!")
                        continue

                    while(True):
                        confirmar_alteracao = input("Deseja mesmo fazer essa alteração? (S/N): ").upper()

                        if(confirmar_alteracao == ""):
                            print("A opção não informada ou inválida!")
                            continue

                        if(confirmar_alteracao == "S"):
                            product['Nome'] = novo_produto
                            print(f"O nome do produto {produto_antigo} foi alterado para {product['Nome']}!")
                            break
                        elif(confirmar_alteracao == "N"):
                            break
                        else:
                            print("Opção inválida!")
                            continue
                elif(alterar_dado == 3):
                    descricao_antiga = product['Descrição']
                    nova_descricao = input("Informe a nova descrição do produto: ")

                    if(nova_descricao == ""):
                        print("A descrição do produto não digitado ou inválido!")
                        continue

                    while(True):
                        confirmar_alteracao = input("Deseja mesmo fazer essa alteração? (S/N): ").upper()

                        if(confirmar_alteracao == ""):
                            print("A opção não informada ou inválida!")
                            continue

                        if(confirmar_alteracao == "S"):
                            product['Descrição'] = nova_descricao
                            print(f"A descrição {descricao_antiga} foi alterado para {product['Descrição']}!")
                            break
                        elif(confirmar_alteracao == "N"):
                            break
                        else:
                            print("Opção inválida!")
                            continue
