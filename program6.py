import string


# program to reverse a string

def string_reverse(str1):
    rstr1 = ''
    index = len(str1)

    while index > 0:
        rstr1 = rstr1 + str1[index - 1]
        index = index -1
    return rstr1
str1 = input("Enter the string to reverse : ")
# string_reverse(str1)

print("The reverse string is : ",string_reverse(str1))
