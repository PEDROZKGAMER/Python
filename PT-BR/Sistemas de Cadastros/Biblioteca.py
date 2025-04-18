Livros = []
id_atual = 1
livros_removidos = []

while(True):
    opcao = int(input("Informe uma das opções abaixo:\n1 ==> Cadastrar livros\n2 ==> Listar livros\n3 ==> Alterar dados\n4 ==> Remover livro\n5 ==> Restaurar Livro\n6 ==> Encerrar o programa\n==> "))

    if(opcao == 1):
        continuar_cadastrar = True
        while(continuar_cadastrar):
            nome_autor = input("Informe o nome do autor: ").upper().strip()

            if(nome_autor == ""):
                print("Nome de autor inválido! Por favor informar o nome do autor correto!")
                continue

            nome_livro = input("Informe o nome do livro: ").upper().strip()

            if(nome_livro == ""):
                print("O nome do livro inválido! Por favor informar o nome do livro correto!")
                continue

            quantidade_livro = int(input("Informe a quantidade desse livro: "))

            if(quantidade_livro < 0):
                print("Quantidade inválida! Por favor informar a quantia correta!")
                continue

            while(True):
                confirmar = input("Deseja cadastrar esses dados? (S/N): ").upper().strip()

                if(confirmar == "S"):
                    Livro = {"ID": id_atual, "Autor": nome_autor, "Livro": nome_livro, "Quantidade": quantidade_livro}
                    Livros.append(Livro)
                    id_atual += 1
                    print("O livro foi adicionado com sucesso!")
                    break
                elif(confirmar == "N"):
                        print(f"O livro não foi adicionado!")
                        break
                else:
                    print("Opção inválido!")

            while(True):
                cadastrar_outro = input("Deseja cadastrar outro livro? (S/N): ").upper().strip()

                if(cadastrar_outro in ["S", "N"]):
                    if(cadastrar_outro == "N"):
                        print("Voltando pro menu anterior!")
                        continuar_cadastrar = False
                        break
                    elif(cadastrar_outro == "S"):
                        break
                else:
                    print("Opção inválida!")
    elif(opcao == 2):
        if(Livros == []):
            print("nenhum livro foi adicionado!")
        else:
            print("Lista dos livros cadastrados!")
            for livro in Livros:
                print(f"ID: {livro['ID']} || Nome do livro: {livro['Autor']} || Nome do livro: {livro['Livro']} || Quantidade desse livro: {livro['Quantidade']}")
            print(f"Quantidade de livros: {len(Livros)}")
    elif(opcao == 3):
        continuar_alteracao = True
        while(continuar_alteracao):
            if(Livros == []):
                print("nenhum livro foi adicionado!")
                break
            else:
                print("Lista dos livros cadastrados!")
                for livro in Livros:
                    print(f"ID: {livro['ID']} || Nome do livro: {livro['Autor']} || Nome do livro: {livro['Livro']} || Quantidade desse livro: {livro['Quantidade']}")
                print(f"Quantidade de livros: {len(Livros)}")
        
            id_livro = int(input("Informe o id do livro para alterar: "))

            if(id_livro < 0):
                print("Id inválido! Por favor informar o id válido!")
                continue

            for alterar in Livros:
                if(alterar['ID'] == id_livro):
                    print("\nID encontrado!\n")

                    opcao_alterar = int(input("Informe a opção pra alterar o livro:\n1 ==> Alterar o nome do autor\n2 ==> Alterar o nome do livro\n3 ==> Alterar a quantidade\n==> "))

                    if(opcao_alterar == 1):
                        nome_antigo = alterar['Autor']

                        nome_novo = input("Informe o novo nome do autor: ").upper()

                        if(nome_novo == ""):
                            print("Nome de autor incorreto!")
                            continue

                        confirmar = input("Deseja alterar esse dado? (S/N): ").upper()

                        if(confirmar == "N"):
                            print("Alteração de dado cancelado!")
                            break
                        elif(confirmar == "S"):
                            alterar['Autor'] = nome_novo
                            
                            print(f"O nome do autor {nome_antigo} foi alterado para {alterar['Autor']}")
                    elif(opcao_alterar == 2):
                        nome_livro_antigo = alterar['Livro']

                        novo_nome_livro = input("Informe o novo nome do livro: ").upper()

                        if(novo_nome_livro == ""):
                            print("Nome de livro inválido!")
                            continue

                        confirmar = input("Deseja alterar esse dado? (S/N): ").upper()

                        if(confirmar == "N"):
                            print("Alteração de dado cancelado!")
                            break
                        elif(confirmar == "S"):
                            alterar['Livro'] = novo_nome_livro
                            
                            print(f"O nome do livro {nome_livro_antigo} foi alterado para {novo_nome_livro}")
                    elif(opcao_alterar == 3):
                        quantidade_antiga = alterar['Quantidade']

                        nova_quantidade = int(input("Informe a nova quantidade de livros: "))

                        if(nova_quantidade < 0):
                            print("Quantidade inválida! Por favor informar a quantidade correta!")
                            continue

                        confirmar = input("Deseja alterar esse dado? (S/N): ").upper()

                        if(confirmar == "N"):
                            print("Alteração de dado cancelado!")
                            break
                        elif(confirmar == "S"):
                            alterar['Quantidade'] = nova_quantidade
                            
                            print(f"A quantidade antiga de livros '{quantidade_antiga}', foi alterada para '{nova_quantidade}'")
                    else:
                        print("Opção inválida! Por favor informar a opção correta!")
                        continue
                    while(True):
                        sair_programa = input("Deseja alterar outro livro? (S/N): ").upper()

                        if(sair_programa == "N"):
                            print("Voltando pro menu anterior!")
                            continuar_alteracao = False
                            break
                        elif(sair_programa == "S"):
                            break
                        else:
                            print("Opção inválida! Por favor informar a opção correta!")
                else:
                    print("ID inválido!")
                    continue
    elif(opcao == 4):
        continuar_remocao = True
        while(continuar_remocao):
            if(Livros == []):
                print("nenhum livro foi adicionado!")
                break
            else:
                print("Lista dos livros cadastrados!")
                for livro in Livros:
                    print(f"ID: {livro['ID']} || Nome do livro: {livro['Autor']} || Nome do livro: {livro['Livro']} || Quantidade desse livro: {livro['Quantidade']}")
                print(f"Quantidade de livros: {len(Livros)}")
            
            id_remocao = int(input("Informe o ID do livro a ser removido: "))

            if(id_remocao <= 0 ):
                print("ID inválido! Por favor informar o ID correto!")
                continue

            for remocao in Livros:
                if(remocao['ID'] == id_remocao):
                    while(True):
                        confirmar = input("Deseja remover esse livro? (S/N): ").upper()

                        if(confirmar == "S"):
                            print(f"O livro {remocao['Livro']} foi removido com sucesso!")
                            Livros.remove(remocao)
                            livros_removidos.append(remocao)
                        elif(confirmar == "N"):
                            print("Remoção cancelada!")
                            break
                        else:
                            print("Opção inválida!")
                        
                    while(True):
                            sair_programa = input("Deseja remover outro livro? (S/N): ").upper()

                            if(sair_programa == "N"):
                                continuar_remocao = False
                                break
                            elif(sair_programa == "S"):
                                break
                            else:
                                print("Opção inválida! Por favor informar a opção correta!")
                else:
                    print("ID Inválido!")