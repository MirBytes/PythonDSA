def numcounter(num):
    number = num
    i = 0
    while number > 0:
        i = i + 1
        number = number // 10
    return i

from math import *

def countereasy(num):
    return int(log10(num) + 1)
    
print(f'Number of digits in number is {numcounter(34554)}')
print(f'Number of digits in number is {countereasy(34554)}')