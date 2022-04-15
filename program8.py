# Python program to interchange first and last elements in a list

# define a funtion to swap first and last elements

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

# swap first and last element with help of tuple Variable
def swapFunctionByTuple(newList1):

    # creating the tuple Variable
    nums = newList1[0],newList1[-1]
    newList1[-1],newList1[0] = nums

    return newList1

newList1 = [4,2,6,7,89,3,4,2,5]
print("This is done by the tuple variable : ",swapFunctionByTuple(newList1))

# swap first and last element with help of * operator


def swapFunctionByOperator(newList2):
    start,*middle,end = newList2
    newList2 = end, *middle, start

    return newList2

newList2 = [3,2,5,6,7,8,3,4,7]
print("This is done by the * opeartor : ",swapFunctionByOperator(newList2))

def swapFunctionByInBuilt(newList3):
    first = newList3.pop(0)
    end = newList3.pop(-1)

    newList3.insert(0,end)
    newList3.append(first)
    
    return newList3
newList3 = [2,4,5,6,7,2,3,5,4,5]
print("This is done by the in-built function : ",swapFunctionByInBuilt(newList3))