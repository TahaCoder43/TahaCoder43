def power_num(base,pow):
    result=1
    for index in range(pow):
        result=result * base
    return result
x=2
y=1
while int(x)!=int(y):
    message = "Please enter in your "
    base = input(message + "base:")
    power = input(message + 'power:')
    print(power_num(int(base), int(power)))
    y=input("Do you want to exit (yes,no)")
    if y!="no":
        y=2
    else:
        y=1