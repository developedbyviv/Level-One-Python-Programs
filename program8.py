# Python program to interchange first and last elements in a list

# define a funtion to swap first and last elements
import numbers


def swapFunction(newList):
    size = len(newList)

    # swapping the numbers
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList

# intialise the list
newList = [1,4,7,12,65,34,89,45]

# print the final swap list
print(swapFunction(newList))

