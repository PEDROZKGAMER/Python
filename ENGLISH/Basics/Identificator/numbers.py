try:
    number = int(input("Inform the value: "))

    print("This number is negative!" if number < 0 else "This number is positive!")
except ValueError:
    print("This number inválid!")