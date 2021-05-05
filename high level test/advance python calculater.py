x=2
y=1
while int(x)!=int(y):
    import math
    import operator

    message = "enter your"
    varying_message = "enter your second number"
    opr = input(message + " operater")

    if opr == "**":
        varying_message = "enter your power"
    elif opr == "sqr":
        num2 = "no need"
    elif opr == "/":
        varying_message = "please enter your divisor"
    elif opr == "*":
        varying_message = "please enter your multiplier"

    num1 = float(input(message + " number"))
    num2 = float(input(varying_message))

    addition_operation = num1 + num2
    subtraction_operation = num1 - num2
    multiplication_operation = num1 * num2
    division_operation = num1 / num2
    power_operation = pow(num1, num2)
    square_root_operation = math.sqrt(num1)

    if opr == "+":
        print(addition_operation)
    elif opr == "-":
        print(subtraction_operation)
    elif opr == "*":
        if multiplication_operation == 14:
            int(multiplication_operation)
            print("happy birthday Taha Munawar your " + str(multiplication_operation) + " old")
        else:
            print(multiplication_operation)
    elif opr == "/":
        print(division_operation)
    elif opr == "**":
        print(power_operation)
    elif opr == "sqr":
        print(square_root_operation)
    else:
        print("syntax error")
    input("do you want to exit(1=no,2=yes)")