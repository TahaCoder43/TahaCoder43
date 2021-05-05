def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
       return num1
    elif num2 > num1 and num2 > num3:
        return(num2)
    else:
        return (num3)

type_num1=input("type first number:")
type_num2=input("type second number:")
type_num3=input("type third number:")
print(max_num(type_num1,type_num2,type_num3))