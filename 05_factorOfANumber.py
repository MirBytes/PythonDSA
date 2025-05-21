def bruteFactor(num):
    number  = num
    list = []
    for i in range(1, num + 1):
        if (number % i) == 0:
            list.append(i)
        
    return list

from math import *

def OptimizedFactor(num):
    number  = num
    list = []
    for i in range(1, int(sqrt(num) + 1)):
        if (number % i) == 0:
            list.append(i)
            if (number // i) != i:
                list.append(number // i)
        
    return list

print(f'Factors for 15 are {bruteFactor(15)}')
print(f'Factors for 15 are {OptimizedFactor(15)}')