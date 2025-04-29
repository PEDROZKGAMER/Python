import time
Produtos = []
Produtos_removidos = []
id_atual = 1

print("Inicializando o sistema...")
time.sleep(4)

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
            fornecedor = input("Informe o nome do fornecedor: ")

            if(fornecedor == ""):
                print("O nome do fornecedor não digitado ou inválido!")
                continue

            if(not all(verificacao.isalpha() or verificacao.isspace() for verificacao in fornecedor)):
                print("O nome do fornecedor deve conter só letras!")
                continue

            while(True):
                nome_produto = input("Informe o nome do produto: ")

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
            while(True):
                Categorias = {1: "Alimentos", 2: "Eletrônicos", 3: "Vestuário", 4: "Casa e Decoração", 5: "Esportes e Lazer", 6: "Beleza", 7: "Bebidas"}
                try:
                    opcao_categoria = int(input("Informe uma das categorias abaixo:\n1 ==> Alimentos\n2 ==> Eletrônicos\n3 ==> Vestuário\n4 ==> Casa e Decoração\n5 ==> Esportes e Lazer\n6 ==> Beleza\n7 ==> Bebidas\n==> "))

                    categoria = Categorias.get(opcao_categoria)

                    if(categoria):
                        break
                    else:
                        print("Categoria inválida!")
                except(ValueError):
                    print("A opção de categoria deve ser em número!")
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
                    print("O produto não foi cadastrado!")
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
        print("Carregando a lista dos produtos cadastrados...")
        time.sleep(3)

        if(Produtos == []):
            print("Nenhum produto cadastrado ainda!")
        else:
            print("==== Lista de Produtos! ====")
            numero_produto = 1
            for produto in Produtos:
                print(f"\nProduto #{numero_produto}\nID: {produto['ID']} | Fornecedor: {produto['Fornecedor']} | Nome do produto: {produto['Nome']} | Descrição: {produto['Descrição']}\nCategoria: {produto['Categoria']} | Preço do produto: {produto['Preço']} | Quantidade: {produto['Quantidade']} | Código do produto: {produto['Codigo do produto']}")
                numero_produto += 1
    elif(opcao == 3):
        print("Carregando a lista dos produtos cadastrados...")
        time.sleep(3)

        continuar_alterar = True
        while(continuar_alterar):
            if(Produtos == []):
                print("Nenhum produto cadastrado ainda!")
                break
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
                continue
            
            produto_encontrado = False
            for product in Produtos:
                if(product['ID'] == ID_produto):
                    produto_encontrado = True
                    print("Produto encontrado!")
                    break

            if(not produto_encontrado):
                print("ID inválido! Nenhum produto encontrado com esse ID.")
                continue
                
            try:
                alterar_dado = int(input("Informe a opção para altera-lo:\n1 ==> Alterar o nome do fornecedor\n2 ==> Alterar o nome do produto\n3 ==> Alterar a descrição do produto\n4 ==> Alterar a quantidade\n5 ==> Alterar a categoria\n6 ==> alterar o preço\n7 ==> alterar o código do produto\n8 ==> Cancelar alteração\n==> "))

                if(alterar_dado < 1 or alterar_dado > 8):
                    print("Opção inválida!")
                    continue
            except(ValueError):
                print("A opção deve ser um número!")
                break

            if(alterar_dado == 1):
                fornecedor_antigo = product['Fornecedor']
                novo_fornecedor = input("Informe o novo nome do fornecedor: ")

                if(novo_fornecedor == ""):
                    print("O fornecedor não digitado ou inválido!")
                    continue

                if(not all(verificacao.isalpha() or verificacao.isspace() for verificacao in novo_fornecedor)):
                    print("O nome do fornecedor deve conter só letras!")
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
                        print("Alteração cancelada!")
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

                if(not all(verificacao.isalpha() or verificacao.isspace() for verificacao in novo_produto)):
                    print("O nome do fornecedor deve conter só letras!")
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
                        print("Alteração cancelada!")
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
                        print("Alteração cancelada!")
                        break
                    else:
                        print("Opção inválida!")
                        continue
            elif(alterar_dado == 4):
                quantidade_antiga = product['Quantidade']
                try:
                    quantidade_nova = int(input("Informe a nova quantidade: "))

                    if(quantidade_nova < 0):
                        print("A quantidade negativo ou inválido!")
                        continue
                except(ValueError):
                    print("A quantidade tem que ser em número!")
                    continue

                while(True):
                    confirmar_alteracao = input("Deseja mesmo fazer essa alteração? (S/N): ").upper()

                    if(confirmar_alteracao == ""):
                        print("A opção não informada ou inválida!")
                        continue

                    if(confirmar_alteracao == "S"):
                        product['Quantidade'] = quantidade_nova
                        print(f"A quantidade '{quantidade_antiga}' foi alterado para '{product['Quantidade']}'!")
                        break
                    elif(confirmar_alteracao == "N"):
                        print("Alteração cancelada!")
                        break
                    else:
                        print("Opção inválida!")
                        continue
            elif(alterar_dado == 5):
                Categorias = {1: "Alimentos", 2: "Eletrônicos", 3: "Vestuário", 4: "Casa e Decoração", 5: "Esportes e Lazer", 6: "Beleza", 7: "Bebidas"}
                categoria_antiga = product['Categoria']
                
                try:
                    nova_categoria = int(input("Informe uma nova categoria abaixo:\n1 ==> Alimentos\n2 ==> Eletrônicos\n3 ==> Vestuário\n4 ==> Casa e Decoração\n5 ==> Esportes e Lazer\n6 ==> Beleza\n7 ==> Bebidas\n==> "))

                    nova_categoria = Categorias.get(opcao_categoria)
                except(ValueError):
                    print("A opção deve ser em número!")
                    continue

                while(True):
                    confirmar_alteracao = input("Deseja mesmo fazer essa alteração? (S/N): ").upper()

                    if(confirmar_alteracao == ""):
                        print("A opção não informada ou inválida!")
                        continue

                    if(confirmar_alteracao == "S"):
                        product['Categoria'] = nova_categoria
                        print(f"A categoria do produto {categoria_antiga} foi alterado para {product['Categoria']}")
                        break
                    elif(confirmar_alteracao == "N"):
                        print("Alteração cancelada!")
                        break
                    else:
                        print("Opção inválida!")
                        continue
            elif(alterar_dado == 6):
                preco_antigo = product['Preço']

                try:
                    preco_novo = float(input("Informe o novo preço do produto: "))

                    if(preco_novo < 0):
                        print("O preço do produto negativo ou inválido!")
                        continue
                except(ValueError):
                    print("O preço do produto deve ser em número!")
                    continue

                while(True):
                    confirmar_alteracao = input("Deseja mesmo fazer essa alteração? (S/N): ").upper()

                    if(confirmar_alteracao == ""):
                        print("A opção não informada ou inválida!")
                        continue

                    if(confirmar_alteracao == "S"):
                        product['Preço'] = preco_novo
                        print(f"O preço do produto '{preco_antigo}' foi alterado para {product['Preço']}!")
                        break
                    elif(confirmar_alteracao == "N"):
                        print("Alteração cancelada!")
                        break
                    else:
                        print("A opção inválida!")
                        continue
            elif(alterar_dado == 7):
                codigo_antigo = product['Codigo do produto']
                codigo_novo = input("Informe o novo codigo do produto: ")

                if(codigo_novo == ""):
                    print("O codigo do produto não digitado ou inválido")
                    continue

                while(True):
                    confirmar_alteracao = input("Deseja mesmo fazer essa alteração? (S/N): ").upper()

                    if(confirmar_alteracao == ""):
                        print("A opção não informada ou inválida!")
                        continue

                    if(confirmar_alteracao == "S"):
                        product['Codigo do produto'] = codigo_novo
                        print(f"O código do produto foi alterado de '{codigo_antigo}' para '{product['Codigo do produto']}'!")
                        break
                    elif(confirmar_alteracao == "N"):
                        print("Alteração cancelada!")
                        break
                    else:
                        print("Opção inválida!")
                        continue
            elif(alterar_dado == 8):
                print("Alteração cancelada!")
                continuar_alterar = False
                break

            while(True):
                sair = input("Deseja alterar outro dado de outro produto? (S/N): ").upper()

                if(sair == "S"):
                    break
                elif(sair == "N"):
                    print("Voltando pro menu!")
                    continuar_alterar = False
                    break
                else:
                    print("Opção inválida!")
                    continue

    elif(opcao == 4):
        print("Carregando a lista dos produtos cadastrados...")
        time.sleep(3)

        continuar_removendo = True
        while(continuar_removendo):
            if(Produtos == []):
                print("Nenhum produto cadastrado ainda!")
                break
            else:
                print("==== Lista de Produtos! ====")
                numero_produto = 1
                for produto in Produtos:
                    print(f"\nProduto #{numero_produto}\nID: {produto['ID']} | Fornecedor: {produto['Fornecedor']} | Nome do produto: {produto['Nome']} | Descrição: {produto['Descrição']}\nCategoria: {produto['Categoria']} | Preço do produto: {produto['Preço']} | Quantidade: {produto['Quantidade']} | Código do produto: {produto['Codigo do produto']}")
                    numero_produto += 1
            
            try:
                ID_produto = int(input("Informe o ID do produto para removelo: "))

                if(ID_produto < 0):
                    print("O ID do produto negativo ou inválido!")
                    continue
            except(ValueError):
                print("O ID deve ser em número!")
                continue

            for product in Produtos:
                if(product['ID'] == ID_produto):
                    print(f"O ID do produto encontrado, O nome do produto '{product['Nome']}' e o seu fornecedor '{product['Fornecedor']}'!")

                    while(True):
                        confirmar = input("Deseja deletar esse produto? (S/N): ").upper()

                        if(confirmar == ""):
                            print("A opção não digitada ou inválida!")
                            continue

                        if(confirmar == "S"):
                            Produtos.remove(product)
                            Produtos_removidos.append(product)
                            print(f"O produto {product['Nome']} foi removido com sucesso!")
                            break
                        elif(confirmar == "N"):
                            print("Remoção cancelada!")
                            break
                        else:
                            print("Opção inválida, por favor inserir uma opção correta!")
                            continue
                    
                    while(True):
                        sair = input("Deseja remover outro produto? (S/N): ").upper()

                        if(sair == ""):
                            print("A opção não digitada ou inválida!")
                            continue

                        if(sair == "S"):
                            break
                        elif(sair == "N"):
                            print("Voltando pro menu anterior!")
                            continuar_removendo = False
                            break
                        else:
                            print("Opção inválida, por favor informar uma opção correta!")
                            continue
    elif(opcao == 5):
        print("Carregando a lista dos produtos removidos...")
        time.sleep(3)

        continuar_restaurando = True
        while(continuar_restaurando):
            if(Produtos_removidos == []):
                print("Nenhum produto cadastrado ainda!")
                break
            else:
                print("==== Lista de Produtos! ====")
                numero_produto = 1
                for produto in Produtos_removidos:
                    print(f"\nProduto #{numero_produto}\nID: {produto['ID']} | Fornecedor: {produto['Fornecedor']} | Nome do produto: {produto['Nome']} | Descrição: {produto['Descrição']}\nCategoria: {produto['Categoria']} | Preço do produto: {produto['Preço']} | Quantidade: {produto['Quantidade']} | Código do produto: {produto['Codigo do produto']}")
                    numero_produto += 1
            
            try:
                ID_produto = int(input("Informe o ID do produto para restaura-lo: "))

                if(ID_produto < 0):
                    print("O ID do produto negativo ou inválido!")
                    continue
            except(ValueError):
                print("O ID deve ser em número!")
                continue

            for product in Produtos_removidos:
                if(product['ID'] == ID_produto):
                    print(f"O ID do produto encontrado, O nome do produto '{product['Nome']}' e o seu fornecedor '{product['Fornecedor']}'!")

                    while(True):
                        confirmar = input("Deseja restaurar esse produto? (S/N): ").upper()

                        if(confirmar == ""):
                            print("A opção não digitada ou inválida!")
                            continue

                        if(confirmar == "S"):
                            Produtos_removidos.remove(product)
                            Produtos.append(product)
                            print(f"O produto {product['Nome']} foi restaurado com sucesso!")
                            break
                        elif(confirmar == "N"):
                            print("Restauração cancelada!")
                            break
                        else:
                            print("Opção inválida, por favor inserir uma opção correta!")
                            continue
                    
                    while(True):
                        sair = input("Deseja restaurar outro produto? (S/N): ").upper()

                        if(sair == ""):
                            print("A opção não digitada ou inválida!")
                            continue

                        if(sair == "S"):
                            break
                        elif(sair == "N"):
                            print("Voltando pro menu anterior!")
                            continuar_restaurando = False
                            break
                        else:
                            print("Opção inválida, por favor informar uma opção correta!")
                            continue
    elif(opcao == 6):
        print("Encerrado o programa, Até mais!")
        break
    else:
        print("Opção inválida! por favor informar uma opção correta!")
        continue

