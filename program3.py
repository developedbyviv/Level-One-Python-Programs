# this program about the calculate the sum and multiplication of two numbers.

import numbers
from secrets import choice
from unittest import result


choice = int(input("Enter the 1 for add or 2 for mulplication :"))

if(choice == 1):
    num1 = int(input("Enter the first number :"))
    num2 = int(input("Enter the second number :"))
    result = num1 + num2
    print("The sum is ", result)
elif(choice ==2):
    num1 = int(input("Enter the first number :"))
    num2 = int(input("Enter the second number :"))
    result = num1 * num2
    print("The multiplication is ", result)
# else:
#     print("Please choose correct number")
