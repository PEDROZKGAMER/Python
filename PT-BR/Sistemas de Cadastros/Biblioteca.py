Livros = []
Livros_removidos = []
ID_atual = 1
import colorama

while(True):
    try:
        opcao = int(input(colorama.Fore.LIGHTBLACK_EX +"Informe uma das opções abaixo:\n"+colorama.Style.RESET_ALL+""+colorama.Fore.LIGHTWHITE_EX+"1 ==> Cadastrar livros"+ colorama.Style.RESET_ALL+"\n2 ==> Listar livros\n"+colorama.Fore.LIGHTWHITE_EX+"3 ==> Alterar dados"+ colorama.Style.RESET_ALL+"\n4 ==> Remover livro\n"+colorama.Fore.LIGHTWHITE_EX+"5 ==> Restaurar Livro"+ colorama.Style.RESET_ALL+"\n6 ==> Encerrar o programa\n==> "+ colorama.Style.RESET_ALL))

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
                nome_Autor = input(colorama.Style.BRIGHT +"Informe o nome do autor do livro: "+ colorama.Style.RESET_ALL)

                if(nome_Autor == ""):
                    print(colorama.Fore.YELLOW+ "O nome não digitado ou inválido!"+ colorama.Style.RESET_ALL)
                    continue

                if(not all(verificar.isalpha() or verificar.isspace() for verificar in nome_Autor)):
                    print(colorama.Fore.YELLOW+ "O nome deve conter só letras!"+ colorama.Style.RESET_ALL)
                    continue
                break
            while(True):
                nome_Livro = input(colorama.Style.BRIGHT +"Informe o nome do livro: "+ colorama.Style.RESET_ALL)

                if(nome_Livro == ""):
                    print(colorama.Fore.YELLOW+ "O nome do livro não digitado ou inválido!"+ colorama.Style.RESET_ALL)
                    continue

                if(not all(verificacao.isalpha() or verificacao.isspace() for verificacao in nome_Livro)):
                    print(colorama.Fore.YELLOW+ "O nome do livro deve conter só letras!"+ colorama.Style.RESET_ALL)
                    continue
                break

            ISBN = input(colorama.Style.BRIGHT +"Informe a ISBN do livro: "+ colorama.Style.RESET_ALL).upper()

            if(ISBN == ""):
                print(colorama.Fore.YELLOW+ "ISBN inválido, Por favor informar a ISBN correto!"+ colorama.Style.RESET_ALL)
                continue

            while(True):
                try:
                    quantidade = int(input(colorama.Style.BRIGHT +"Informe a quantidade desse livro: "+ colorama.Style.RESET_ALL))

                    if(quantidade < 0):
                        print(colorama.Fore.YELLOW+ "A quantidade de livro negativo ou opção inválido!"+ colorama.Style.RESET_ALL)
                        continue
                except(ValueError):
                    print(colorama.Fore.YELLOW+ "A quantidade deve ser numérico!"+ colorama.Style.RESET_ALL)
                    continue
                break

            while(True):
                deseja_descricao = input(colorama.Style.BRIGHT +"Deseja adicionar alguma descrição do livro? (S/N): "+ colorama.Style.RESET_ALL).upper()

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
                    opcao_categoria = int(input(colorama.Style.BRIGHT +"Informe a categoria do livro abaixo:\n1 ==> Drama\n2 ==> Romançe\n3 ==> Comédia\n4 ==> Distopia\n5 ==> Ficção\n6 ==> Terror\n7 ==> Conto\n==> "+ colorama.Style.RESET_ALL))

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
                deseja_cadastrar = input(colorama.Style.BRIGHT +"Deseja cadastrar esse livro? (S/N): "+ colorama.Style.RESET_ALL).upper()
                
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
                sair = input(colorama.Style.BRIGHT +"Deseja cadastrar outro livro? (S/N): "+ colorama.Style.RESET_ALL).upper()

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
            print("="*80 +"\n"+"/"*80)
            print(colorama.Fore.CYAN +("Lista de Livros Cadastrados".center(80))+ colorama.Style.RESET_ALL)
            numero_livro = 1
            for livro in Livros:
                print("\n"+colorama.Fore.GREEN+f"Livro #{numero_livro}"+colorama.Style.RESET_ALL+f"\n\nID do Livro: {livro['ID']}\nNome do Autor: {livro['Autor']}\nNome do livro: {livro['Livro']}\nCategoria: {livro['Categoria']}\nQuantidade: {livro['Quantidade']}\n\nDescrição: {livro['Descrição']}\nISBN: {livro['ISBN']}")
                print("=" * 80+"\n"+ "|"*80+"\n"+"="*80)
                numero_livro += 1
            print("\\"*80+"\n"+"="*80)
    elif(opcao == 3):
        continuar_alterando = True
        while(continuar_alterando):
            if(Livros == []):
                print(colorama.Fore.RED + "Nenhum livro foi adicionado ainda!"+ colorama.Style.RESET_ALL)
            else:
                print("="*80 +"\n"+"/"*80)
                print(colorama.Fore.CYAN +("Lista de Livros Cadastrados".center(80))+ colorama.Style.RESET_ALL)
                numero_livro = 1
            for livro in Livros:
                print("\n"+"|"*80 +"\n\n"+colorama.Fore.GREEN+f"Livro #{numero_livro}"+colorama.Style.RESET_ALL+f"\n\nID do Livro: {livro['ID']}\nNome do Autor: {livro['Autor']}\nNome do livro: {livro['Livro']}\nCategoria: {livro['Categoria']}\nQuantidade: {livro['Quantidade']}\n\nDescrição: {livro['Descrição']}\nISBN: {livro['ISBN']}")
                numero_livro += 1
            print("\\"*80+"\n"+"="*80)
            
            try:
                ID_livro = int(input("Informe o ID do livro: "))

                if(ID_livro < 0):
                    print(colorama.Fore.YELLOW+ "O ID do livro negativo ou inválido!" +colorama.Style.RESET_ALL)
                    continue
            except(ValueError):
                print(colorama.Fore.YELLOW+ "O ID deve ser numérico!"+ colorama.Style.RESET_ALL)
            
            livro_encontrado = False
            for alterar in Livros:
                if(alterar['ID'] == ID_livro):
                    livro_encontrado = True
                    print(colorama.Fore.GREEN+f"ID encontrado, Nome do livro: {alterar['Livro']} "+ colorama.Style.RESET_ALL)
                    break

            if(not livro_encontrado):
                print(colorama.Fore.YELLOW+"O ID esta inválido, por favor igitar o ID correto!"+colorama.Style.RESET_ALL)
                continue

            opcao_escolher = True
            while(opcao_escolher):
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
                            confirmar = input("Deseja mesmo alterar o nome do autor? (S/N): ").upper()

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
                elif(opcao_alterar == 2):
                    alteracao_livro = True
                    livro_antigo = alterar['Livro']
                    while(alteracao_livro):
                        novo_livro = input("Informe o novo nome do livro: ")

                        if(novo_livro == "" or not all(verificar_livro.isalpha() or verificar_livro.isspace() for verificar_livro in novo_livro)):
                            print(colorama.Fore.YELLOW+"O nome do livro deve conter só letras ou não digitado inválido!"+colorama.Style.RESET_ALL)
                            continue

                        while(True):
                            confirmar = input("Deseja mesmo alterar o nome do livro? (S/N): ").upper()

                            if(confirmar == "S"):
                                alterar['Livro'] = novo_livro
                                print(colorama.Fore.GREEN+f"O nome do livro '{livro_antigo}' foi alterado para '{alterar['Livro']}'"+ colorama.Style.RESET_ALL)
                                alteracao_livro = False
                                break
                            elif(confirmar == "N"):
                                print(colorama.Fore.RED+"Alteração cancelada!"+colorama.Style.RESET_ALL)
                                alteracao_livro = False
                            else:
                                print(colorama.Fore.YELLOW+"Opção Inválida, por favor informar a opção correta!"+colorama.Style.RESET_ALL)
                                continue
                elif(opcao_alterar == 3):
                    alteracao_ISBN = True
                    ISBN_antigo = alterar['ISBN']
                    while(alteracao_ISBN):
                        novo_ISBN = input("Informe o novo ISBN do livro: ")

                        if(novo_ISBN == ""):
                            print(colorama.Fore.YELLOW+"ISBN não digitado ou inválido!"+colorama.Style.RESET_ALL)
                            continue

                        while(True):
                            confirmar = input("Deseja mesmo alterar o nome do livro? (S/N): ").upper()

                            if(confirmar == "S"):
                                alterar['ISBN'] = novo_ISBN
                                print(colorama.Fore.GREEN+f"A ISBN do livro '{ISBN_antigo}' foi alterado para '{alterar['ISBN']}'"+ colorama.Style.RESET_ALL)
                                alteracao_ISBN = False
                                break
                            elif(confirmar == "N"):
                                print(colorama.Fore.RED+"Alteração cancelada!"+colorama.Style.RESET_ALL)
                                alteracao_ISBN = False
                            else:
                                print(colorama.Fore.YELLOW+"Opção Inválida, por favor informar a opção correta!"+colorama.Style.RESET_ALL)
                                continue
                elif(opcao_alterar == 4):
                    alteracao_quantidade = True
                    quant_antiga = alterar['Quantidade']
                    while(alteracao_quantidade):
                        try:
                            nova_quantidade = int(input("Informe a nova quantidade desse livro "))

                            if(nova_quantidade < 0):
                                print(colorama.Fore.YELLOW+"Quantidade negativo ou inválido!"+colorama.Style.RESET_ALL)
                                continue
                        except(ValueError):
                            print(colorama.Fore.YELLOW+"A quantidade deve ser numérico!"+colorama.Style.RESET_ALL)
                            continue

                        while(True):
                            confirmar = input("Deseja mesmo alterar o nome do livro? (S/N): ").upper()

                            if(confirmar == "S"):
                                alterar['Quantidade'] = nova_quantidade
                                print(colorama.Fore.GREEN+f"A quantidade desse livro '{quant_antiga}' foi alterado para '{alterar['Quantidade']}'"+ colorama.Style.RESET_ALL)
                                alteracao_quantidade = False
                                break
                            elif(confirmar == "N"):
                                print(colorama.Fore.RED+"Alteração cancelada!"+colorama.Style.RESET_ALL)
                                alteracao_quantidade = False
                            else:
                                print(colorama.Fore.YELLOW+"Opção Inválida, por favor informar a opção correta!"+colorama.Style.RESET_ALL)
                                continue
                elif(opcao_alterar == 5):
                    alteracao_descricao = True
                    descricao_antiga = alterar['Descrição']
                    while(alteracao_descricao):
                        nova_descricao = input("Informe a nova descrição do livro: ")

                        if(nova_descricao == ""):
                            print(colorama.Fore.YELLOW+"A descriçao não digitado ou inválido!"+colorama.Style.RESET_ALL)
                            continue

                        while(True):
                            confirmar = input("Deseja mesmo alterar o nome do livro? (S/N): ").upper()

                            if(confirmar == "S"):
                                alterar['Descrição'] = nova_descricao
                                print(colorama.Fore.GREEN+f"A quantidade desse livro '{descricao_antiga}' foi alterado para '{alterar['Descrição']}'"+ colorama.Style.RESET_ALL)
                                alteracao_descricao = False
                                break
                            elif(confirmar == "N"):
                                print(colorama.Fore.RED+"Alteração cancelada!"+colorama.Style.RESET_ALL)
                                alteracao_descricao = False
                            else:
                                print(colorama.Fore.YELLOW+"Opção Inválida, por favor informar a opção correta!"+colorama.Style.RESET_ALL)
                                continue
                elif(opcao_alterar == 6):
                    alteracao_categoria = True
                    categoria_antiga = alterar['Categoria']
                    while(alteracao_categoria):
                        Categorias = {1: "Drama", 2: "Romançe", 3: "Comédia", 4: "Distopia", 5: "Ficção", 6: "Terror", 7: "Conto"}
                                
                        try:
                            nova_categoria = int(input("Informe a categoria do livro abaixo:\n1 ==> Drama\n2 ==> Romançe\n3 ==> Comédia\n4 ==> Distopia\n5 ==> Ficção\n6 ==> Terror\n7 ==> Conto\n==> "))

                            if(nova_categoria < 1 or nova_categoria > 7):
                                print(colorama.Fore.RED+"A Categoria digitada inválida!"+colorama.Style.RESET_ALL)
                                continue
                        except(ValueError):
                            print(colorama.Fore.YELLOW+"O número da categoria deve ser numérica!"+colorama.Style.RESET_ALL)
                            continue

                        if(Categorias):
                            Categoria = Categorias.get(nova_categoria)
                        else:
                            print(colorama.Fore.YELLOW+ "Categoria inválida!"+ colorama.Style.RESET_ALL)
                            continue
                        break

                    while(True):
                        confirmar = input("Deseja mesmo alterar a categoria do livro? (S/N): ").upper()

                        if(confirmar == "S"):
                            alterar['Categoria'] = Categoria
                            print(colorama.Fore.GREEN+f"A categoria desse livro '{categoria_antiga}' foi alterado para '{alterar['Categoria']}'"+ colorama.Style.RESET_ALL)
                            alteracao_categoria = False
                            break
                        elif(confirmar == "N"):
                            print(colorama.Fore.RED+"Alteração cancelada!"+colorama.Style.RESET_ALL)
                            alteracao_categoria = False
                        else:
                            print(colorama.Fore.YELLOW+"Opção Inválida, por favor informar a opção correta!"+colorama.Style.RESET_ALL)
                            continue
                elif(opcao_alterar == 7):
                    print(colorama.Fore.MAGENTA+"Voltando pro menu anterior!"+colorama.Style.RESET_ALL)
                    continuar_alterando = False
                    break

                while(True):
                    sair = input("Você deseja alterar outro livro? (S/N): ").upper()

                    if(sair == "S"):
                        opcao_escolher = False
                        break
                    elif(sair == "N"):
                        print(colorama.Fore.MAGENTA+"Voltando pro menu anterior!"+colorama.Style.RESET_ALL)
                        continuar_alterando = False
                        opcao_escolher = False
                        break
                    else:
                        print(colorama.Fore.YELLOW+"Opção inválida, por favor informar a opção correta!"+colorama.Style.RESET_ALL)
                        continue
    elif(opcao == 4):
        continuar_removendo = True
        while(continuar_removendo):
            if(Livros == []):
                print(colorama.Fore.RED + "Nenhum livro foi adicionado ainda!"+ colorama.Style.RESET_ALL)
                break
            else:
                print("="*80 +"\n"+"/"*80)
                print(colorama.Fore.CYAN +("Lista de Livros Cadastrados".center(80))+ colorama.Style.RESET_ALL)
                numero_livro = 1
            for livro in Livros:
                print("\n"+"|"*80 +"\n\n"+colorama.Fore.GREEN+f"Livro #{numero_livro}"+colorama.Style.RESET_ALL+f"\n\nID do Livro: {livro['ID']}\nNome do Autor: {livro['Autor']}\nNome do livro: {livro['Livro']}\nCategoria: {livro['Categoria']}\nQuantidade: {livro['Quantidade']}\n\nDescrição: {livro['Descrição']}\nISBN: {livro['ISBN']}")
                numero_livro += 1
            print("\\"*80+"\n"+"="*80)
            
            try:
                ID_livro = int(input("Informe o ID do livro a ser removido: "))

                if(ID_livro < 0):
                    print(colorama.Fore.YELLOW+"O ID negativo ou inválido!"+colorama.Style.RESET_ALL)
                    continue
            except(ValueError):
                print(colorama.Fore.YELLOW+"O ID deve ser numérico!"+colorama.Style.RESET_ALL)
                continue

            livro_encontrado = False
            for remover in Livros:
                if(remover['ID'] == ID_livro):
                    livro_encontrado = True
                    print(colorama.Fore.GREEN+f"Livro encontrado, o nome do livro: {remover['Livro']}!"+colorama.Style.RESET_ALL)
                    break

            if(not livro_encontrado):
                print(colorama.Fore.RED+"Livro não encontrado!"+colorama.Style.RESET_ALL)
                continue

            while(True):
                confirmar = input("Deseja mesmo removero livro? (S/N): ").upper()

                if(confirmar == "S"):
                    Livros.remove(remover)
                    Livros_removidos.append(remover)
                    print(colorama.Fore.GREEN+f"O livro foi removido com sucesso!"+ colorama.Style.RESET_ALL)
                    break
                elif(confirmar == "N"):
                    print(colorama.Fore.RED+"remoção cancelada!"+colorama.Style.RESET_ALL)
                    break
                else:
                    print(colorama.Fore.YELLOW+"Opção Inválida, por favor informar a opção correta!"+colorama.Style.RESET_ALL)
                    continue
            
            while(True):
                sair = input("Você deseja remover outro livro? (S/N): ").upper()

                if(sair == "S"):
                    break
                elif(sair == "N"):
                    print(colorama.Fore.MAGENTA+"Voltando pro menu anterior!"+colorama.Style.RESET_ALL)
                    continuar_removendo = False
                    break
                else:
                    print(colorama.Fore.YELLOW+"Opção inválida, por favor informar a opção correta!"+colorama.Style.RESET_ALL)
                    continue
    elif(opcao == 5):
        continuar_restaurar = True
        while(continuar_restaurar):
            if(Livros_removidos == []):
                print(colorama.Fore.RED + "Nenhum livro foi adicionado ainda!"+ colorama.Style.RESET_ALL)
                break
            else:
                print("="*80 +"\n"+"/"*80)
                print(colorama.Fore.CYAN +("Lista de Livros Removidos".center(80))+ colorama.Style.RESET_ALL)
                numero_livro = 1
            for livro in Livros_removidos:
                print("\n"+"|"*80 +"\n\n"+colorama.Fore.GREEN+f"Livro #{numero_livro}"+colorama.Style.RESET_ALL+f"\n\nID do Livro: {livro['ID']}\nNome do Autor: {livro['Autor']}\nNome do livro: {livro['Livro']}\nCategoria: {livro['Categoria']}\nQuantidade: {livro['Quantidade']}\n\nDescrição: {livro['Descrição']}\nISBN: {livro['ISBN']}")
                numero_livro += 1
            print("\\"*80+"\n"+"="*80)
            
            try:
                ID_livro = int(input("Informe o ID do livro a ser restaurado: "))

                if(ID_livro < 0):
                    print(colorama.Fore.YELLOW+"O ID negativo ou inválido!"+colorama.Style.RESET_ALL)
                    continue
            except(ValueError):
                print(colorama.Fore.YELLOW+"O ID deve ser numérico!"+colorama.Style.RESET_ALL)
                continue

            livro_encontrado = False
            for restaurar in Livros_removidos:
                if(restaurar['ID'] == ID_livro):
                    livro_encontrado = True
                    print(colorama.Fore.GREEN+f"Livro removido encontrado, o nome do livro: {restaurar['Livro']}!"+colorama.Style.RESET_ALL)
                    break

            if(not livro_encontrado):
                print(colorama.Fore.RED+"Livro não encontrado!"+colorama.Style.RESET_ALL)
                continue

            while(True):
                confirmar = input("Deseja mesmo restaurar esse livro? (S/N): ").upper()

                if(confirmar == "S"):
                    Livros_removidos.remove(restaurar)
                    Livros.append(restaurar)
                    print(colorama.Fore.GREEN+f"O livro foi restaurado com sucesso!"+ colorama.Style.RESET_ALL)
                    break
                elif(confirmar == "N"):
                    print(colorama.Fore.RED+"remoção cancelada!"+colorama.Style.RESET_ALL)
                    break
                else:
                    print(colorama.Fore.YELLOW+"Opção Inválida, por favor informar a opção correta!"+colorama.Style.RESET_ALL)
                    continue
            
            while(True):
                sair = input("Você deseja restaurar outro livro? (S/N): ").upper()

                if(sair == "S"):
                    break
                elif(sair == "N"):
                    print(colorama.Fore.MAGENTA+"Voltando pro menu anterior!"+colorama.Style.RESET_ALL)
                    continuar_restaurar = False
                    break
                else:
                    print(colorama.Fore.YELLOW+"Opção inválida, por favor informar a opção correta!"+colorama.Style.RESET_ALL)
                    continue
    else:
        print(colorama.Fore.LIGHTBLACK_EX+"Encerrando o programa, até mais!"+colorama.Style.RESET_ALL)
        break