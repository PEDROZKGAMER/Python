Clients = []
Clients_removed = []
id_people = 1

while(True):
    print("\n#==== Welcome my System Register Clients ====#")
    option = int(input("Please choice your option down:\n1 ==> Register Clients\n2 ==> Listen clients registreds\n3 ==> Alter clients\n4 ==> Remove Clients\n5 ==> Restore clients\n6 ==> exit the system\n==> "))

    if(option == "" and option <= 0):
        print("Inválid option! Please inform option correct")
        continue

    if(option == 1):
        while(True):
            name = input("\nInform the name people: ").upper().strip()

            if(name == ""):
                print("Inválid name! Please inform the name correct!")
                continue

            SSN_people = int(input("Inform the Social Sectury Number the people: "))

            if(SSN_people == "" and SSN_people < 0):
                print("Social Security Number is incorrect! Please inform SSN correct!")
                continue

            email = input("Inform email the people: ")

            if(email == ""):
                print("Email is inválid! Please inform email correct!")
                continue

            People = {"ID": id_people, "Name": name, "SSN": SSN_people, "Email": email}
            Clients.append(People)
            id_people += 1

            confirm = input("You want register the people? (Y/N): ").upper()

            if(confirm == "N"):
                print("People is dont registed in the System!")
                Clients.remove(People)
            
            exit_system = input("You want register the other people? (Y/N): ").upper()

            if(exit_system == "N"):
                print("Return in the previos menu!")
                break
    elif(option == 2):
        if(Clients == []):
            print("None client registed!")
            break
        else:
            print("#=== List the clients registed ===#")
            for client in Clients:
                print(f"ID: {client['ID']} || Name people: {client['Name']} || Your SSN: {client['SSN']} || Your Email: {client['Email']}")
    elif(option == 3):
        if(Clients == []):
            print("None people registed!")
            break
        else:
            print("#=== List the clients registed ===#")
            for client in Clients:
                print(f"ID: {client['ID']} || Name people: {client['Name']} || Your SSN: {client['SSN']} || Your Email: {client['Email']}")
        
        id_people_alter = int(input("Inform the ID people: "))
        
        while(True):
            for client in Clients:
                if(client['ID'] == id_people_alter):
                    option_alter = int(input("Inform the option for alter client:\n1 ==> Alter name people\n2 ==> Alter SSN people\n3 ==> Alter Email People\n4 ==> exit people changes\n==. "))

                    if(option_alter == 1):
                        old_name = client['Name']

                        new_name = input("Inform the new name people: ").upper()

                        if(new_name == []):
                            print("Name people is inválid! Please inform the name people correct!")
                            continue

                        client['Name'] = new_name

                        print(f"The name people old {old_name} is changed for {client['Name']}")
                    elif(option_alter == 2):
                        old_SSN = client['SSN']

                        new_SSN = int(input("If you type the social securty number the people incorret, inform the new SSN whiout error!: "))

                        if(new_SSN == "" and new_SSN < 0):
                            print("Inválid social securty number! Please inform the SSN correct!")
                            continue

                        client['SSN'] = new_SSN

                        print(f"The old Social Securty Number {old_SSN}, is changed for {new_SSN}")
                    elif(option_alter == 3):
                        old_email = client['Email']

                        new_email = input("Inform the new email the people: ")

                        if(new_email == ""):
                            print("Email is inválid! Please inform the email correct!")
                            continue

                        client['Email'] = new_email

                        print(f"The old email {old_email} is changed for {client['Email']}")
                    elif(option == 4):
                        print("Return the previous menu!")
                        break
                    else:
                        print("Option inválid! Please inform the option correct!")
                        continue
    elif(option == 4):
        if(Clients == []):
            print("None people registed!")
            continue
        else:
            print("#=== List the clients registed ===#")
            for client in Clients:
                print(f"ID: {client['ID']} || Name people: {client['Name']} || Your SSN: {client['SSN']} || Your Email: {client['Email']}")
            
        remove_client = int(input("Inform the ID people: "))

        if(remove_client == "" and remove_client <= 0):
            print("Inválid ID! Please inform the ID people!")
            continue

        for remove in Clients:
            if(remove['ID'] == remove_client):
                Clients.remove(remove)
                Clients_removed.append(remove)
                print(f"The client {remove['Name']} is removed!")
        
        out = input("You want remove the other client? (Y/N): ").upper().strip()

        if(out == "N"):
            print("Returnig the previous menu!")
            continue