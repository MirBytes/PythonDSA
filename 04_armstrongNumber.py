from math import *

def armstrongNumberFinder(num):
    number = num
    squaredSum = 0
    digits = int(log10(number) + 1)

    while number > 0:
        digit = number % 10
        squaredSum = squaredSum + digit ** digits
        number = number // 10

    return num == squaredSum

print(f'The number 18765 is armstrong number: {armstrongNumberFinder(18765)}')
print(f'The number 153 is armstrong number: {armstrongNumberFinder(153)}')