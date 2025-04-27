import time
Clients = []
Clients_removed = []
id_actual = 1

while(True):
    print("System is initialized...")
    time.sleep(5)
    try:
        option = int(input("Inform the option:\n1 ==> Register client\n2 ==> List the people\n3 ==> Alter data people\n4 ==> Remove client\n5 ==> Restoured people\n6 ==> Exit System\n==> "))

        if(option < 0):
            print("The option is negative inválid!")
            continue
    except ValueError:
        print("Option is numéric, try the type option correct!")
        continue

    if(option == 1):
        print("")
