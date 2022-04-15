def max(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print("Num1 is greater")
    elif num2 >num1 and num2 > num3:
        print("Num2 is greater")
    else:
        print("num3 is greater")

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))

max(num1,num2,num3)