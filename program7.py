# program sum of digits

def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum
n = 1234
print(getSum(n))