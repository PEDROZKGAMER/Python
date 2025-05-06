Livros = []
Livros_removidos = []
ID_atual = 1
import colorama

while(True):
    try:
        opcao = int(input(colorama.Style.BRIGHT +"Informe uma das opções abaixo:\n1 ==> Cadastrar livros\n2 ==> Listar livros\n3 ==> Alterar dados\n4 ==> Remover livro\n5 ==> Restaurar Livro\n6 ==> Encerrar o programa\n==> "+ colorama.Style.RESET_ALL))

        if(opcao < 0):
            print("A opção negativo ou inválido!")
            continue
    except(ValueError):
        print("A opção deve ser numérico!")
        continue

    if(opcao == 1):
        continuar_cadastrando = True
        while(continuar_cadastrando):
            while(True):
                nome_Autor = input("Informe o nome do autor do livro: ")

                if(nome_Autor == ""):
                    print(colorama.Fore.YELLOW+ "O nome não digitado ou inválido!"+ colorama.Style.RESET_ALL)
                    continue

                if(not all(verificar.isalpha() or verificar.isspace() for verificar in nome_Autor)):
                    print(colorama.Fore.YELLOW+ "O nome deve conter só letras!"+ colorama.Style.RESET_ALL)
                    continue
                break
            while(True):
                nome_Livro = input("Informe o nome do livro: ")

                if(nome_Livro == ""):
                    print(colorama.Fore.YELLOW+ "O nome do livro não digitado ou inválido!"+ colorama.Style.RESET_ALL)
                    continue

                if(not all(verificacao.isalpha() or verificacao.isspace() for verificacao in nome_Livro)):
                    print(colorama.Fore.YELLOW+ "O nome do livro deve conter só letras!"+ colorama.Style.RESET_ALL)
                    continue
                break

            ISBN = input("Informe a ISBN do livro: ").upper()

            if(ISBN == ""):
                print(colorama.Fore.YELLOW+ "ISBN inválido, Por favor informar a ISBN correto!"+ colorama.Style.RESET_ALL)
                continue

            while(True):
                try:
                    quantidade = int(input("Informe a quantidade desse livro: "))

                    if(quantidade < 0):
                        print(colorama.Fore.YELLOW+ "A quantidade de livro negativo ou opção inválido!"+ colorama.Style.RESET_ALL)
                        continue
                except(ValueError):
                    print(colorama.Fore.YELLOW+ "A quantidade deve ser numérico!"+ colorama.Style.RESET_ALL)
                    continue
                break

            while(True):
                deseja_descricao = input("Deseja adicionar alguma descrição do livro? (S/N): ").upper()

                if(deseja_descricao == "S"):
                    descricao = input("Informe a descrição do livro: ")

                    if(descricao == ""):
                        print("A descrição não digitada ou inválida!")
                        continue
                    break
                elif(deseja_descricao == "N"):
                    descricao = "Nenhuma descrição adicionada ainda!"
                    break
                else:
                    print(colorama.Fore.RED+ "Opção inválida, Por favor informar a opção correta!"+ colorama.Style.RESET_ALL)
                    continue
            
            while(True):
                Categorias = {1: "Drama", 2: "Romançe", 3: "Comédia", 4: "Distopia", 5: "Ficção", 6: "Terror", 7: "Conto"}
                try:   
                    opcao_categoria = int(input("Informe a categoria do livro abaixo:\n1 ==> Drama\n2 ==> Romançe\n3 ==> Comédia\n4 ==> Distopia\n5 ==> Ficção\n6 ==> Terror\n7 ==> Conto\n==> "))

                    if(opcao_categoria < 1 or opcao_categoria > 7):
                        print(colorama.Fore.YELLOW+ "Categoria inválida!"+ colorama.Style.RESET_ALL)
                        continue
                except(ValueError):
                    print(colorama.Fore.YELLOW+"O numero da categoria deve ser numérico!"+ colorama.Style.RESET_ALL)
                    continue
                
                

                if(Categorias):
                    Categoria = Categorias.get(opcao_categoria)
                else:
                    print(colorama.Fore.YELLOW+ "Categoria inválida!"+ colorama.Style.RESET_ALL)
                    continue
                break

            while(True):
                deseja_cadastrar = input("Deseja cadastrar esse livro? (S/N): ").upper()
                
                if(deseja_cadastrar == "S"):
                    Livro = {"ID": ID_atual, "Autor": nome_Autor, "Livro": nome_Livro, "Categoria": Categoria, "Quantidade": quantidade, "Descrição": descricao, "ISBN": ISBN}
                    Livros.append(Livro)
                    print(f"O livro {nome_Livro} foi cadastrado com sucesso!")
                    ID_atual += 1
                    break
                elif(deseja_cadastrar == "N"):
                    print("O livro não foi cadastrado!")
                    break
                else:
                    print(colorama.Fore.RED+ "Opção inválida, por favor informar a opção correta!"+ colorama.Style.RESET_ALL)
                    continue
            
            while(True):
                sair = input("Deseja cadastrar outro livro? (S/N): ").upper()

                if(sair == ""):
                    print("A opção não digitada ou inválida!")
                    continue

                if(sair == "S"):
                    break
                elif(sair == "N"):
                    print("Voltando pro menu anterior!")
                    continuar_cadastrando = False
                    break
                else:
                    print(colorama.Fore.RED+ "Opção inválida, digite a opção correta!"+ colorama.Style.RESET_ALL)
                    continue
    elif(opcao == 2):
        if(Livros == []):
            print(colorama.Fore.RED + "Nenhum livro foi adicionado ainda!"+ colorama.Style.RESET_ALL)
        else:
            print("="*80,)
            print(colorama.Fore.CYAN +("Lista de Livros Cadastrados".center(80))+ colorama.Style.RESET_ALL)
            numero_livro = 1
            for livro in Livros:
                print(f"\n"+colorama.Fore.GREEN+f"Livro #{numero_livro}"+colorama.Style.RESET_ALL+f"\n\nID do Livro: {livro['ID']}\nNome do Autor: {livro['Autor']}\nNome do livro: {livro['Livro']}\nCategoria: {livro['Categoria']}\nQuantidade: {livro['Quantidade']}\n\nDescrição: {livro['Descrição']}\nISBN: {livro['ISBN']}")
                print("/"*48)
                numero_livro += 1
            print("="*80)
    elif(opcao == 3):
        continuar_alterando = True
        while(continuar_alterando):
            if(Livros == []):
                print(colorama.Fore.RED + "Nenhum livro foi adicionado ainda!"+ colorama.Style.RESET_ALL)
                break
            else:
                print("="*80,)
                print(colorama.Fore.CYAN +("Lista de Livros Cadastrados".center(80))+ colorama.Style.RESET_ALL)
                numero_livro = 1
                for livro in Livros:
                    print(f"\n"+colorama.Fore.GREEN+f"Livro #{numero_livro}"+colorama.Style.RESET_ALL+f"\n\nID do Livro: {livro['ID']}\nNome do Autor: {livro['Autor']}\nNome do livro: {livro['Livro']}\nCategoria: {livro['Categoria']}\nQuantidade: {livro['Quantidade']}\n\nDescrição: {livro['Descrição']}\nISBN: {livro['ISBN']}")
                    print("/"*48)
                    numero_livro += 1
                print("="*80+"\n")
            
            try:
                ID_livro = int(input("Informe o ID do livro: "))

                if(ID_livro < 0):
                    print(colorama.Fore.YELLOW+ "O ID do livro negativo ou inválido!" +colorama.Style.RESET_ALL)
                    continue
            except(ValueError):
                print(colorama.Fore.YELLOW+ "O ID deve ser numérico!"+ colorama.Style.RESET_ALL)

            for alterar in Livros:
                if(alterar['ID'] == ID_livro):
                    print(colorama.Fore.GREEN+f"ID encontrado, Nome do livro: {alterar['Livro']} "+ colorama.Style.RESET_ALL)

                    while(True):
                        try:
                            opcao_alterar = int(input("Informe a opção abaixo:\n1 ==> Alterar o nome do autor\n2 ==> Alterar o nome do livro\n3 ==> Alterar A ISBN do livro\n4 ==> Alterar a quantidade do livro\n5 ==> Alterar a descrição\n6 ==> Alterar a categoria\n7 ==> Cancelar a alteração\n==> "))

                            if(opcao_alterar < 1 or opcao_alterar > 7):
                                print(colorama.Fore.YELLOW+ "A opção negativa ou inválida!" +colorama.Style.RESET_ALL)
                                continue
                        except(ValueError):
                            print(colorama.Fore.YELLOW+"A opção deve ser numérica!"+colorama.Style.RESET_ALL)
                            continue

                        if(opcao_alterar == 1):
                            alteracao_autor = True
                            autor_antigo = alterar['Autor']
                            while(alteracao_autor):
                                novo_autor = input("Digite o novo nome do autor: ")

                                if(novo_autor == "" or not all(verificar_novo_autor.isalpha() or verificar_novo_autor.isspace() for verificar_novo_autor in novo_autor)):
                                    print(colorama.Fore.YELLOW+ "O nome do autor deve conter só letras ou não digitado inválido!"+ colorama.Style.RESET_ALL)
                                    continue

                                while(True):
                                    confirmar = input("Deseja mesmo alterar o nome do autor? (S/N): ")

                                    if(confirmar == "S"):
                                        alterar['Autor'] = novo_autor
                                        print(colorama.Fore.GREEN+f"O nome do autor do autor '{autor_antigo}' foi alterado para '{alterar['Autor']}'"+ colorama.Style.RESET_ALL)
                                        alteracao_autor = False
                                        break
                                    elif(confirmar == "N"):
                                        print(colorama.Fore.RED+"Alteração cancelada!"+colorama.Style.RESET_ALL)
                                        alteracao_autor = False
                                        break
                                    else:
                                        print(colorama.Fore.YELLOW+"Opção Inválida, por favor informar a opção correta!"+colorama.Style.RESET_ALL)
                                        continue