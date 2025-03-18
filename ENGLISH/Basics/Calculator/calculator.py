import math

option = int(input("Inform one option down:\n1 ==> Calculator simple\n2 ==> Square root\n==>"))

if(option == 1):
    result = 0

    result = float(input("Inform the number: "))

    while(True):
        operator = input("Inform operator: ").upper()

        if(operator == "OK"):
            print("Program closed")
            break

        if(operator != "+" and operator != "-" and operator != "*" and operator != "/"):
            print("Error, operator invalid! Please inform operator correct (+ - * /): ")
            continue

        number = float(input("Inform the number: "))

        if(operator == "+"):
            result += number
        elif(operator == "-"):
            result -= number
        elif(operator == "*"):
            result *= number
        elif(operator == "/"):
            result /= number
    
        print(f"The result partial is: {result}")

    print(f"The result end is: {result}")
elif(option == 2):
    number = float(input("Inform the number: "))

    print("Can't square root number negative" if number < 0 else f"The square root number is {math.sqrt(number)}")