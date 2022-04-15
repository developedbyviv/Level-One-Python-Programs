num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
oper = input("So which operator you want to apply on above numbers?"+"+,-,*,/,%, :")

if num1 == 45 and num2 == 3 and oper == "*":
    print("555")
elif num1 == 56 and num2 == 9 and oper == "+":
    print("77")
elif num1 == 56 and num2 == 6 and oper == "/":
    print("4")
elif oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "*":
    print(num1 * num2)
elif oper == "/":
    print(num1 / num2)
elif oper == "%":
    print(num1 % num2)

