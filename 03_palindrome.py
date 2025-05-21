def reverser(num):
    number = num
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10
    
    return reverse
    
print(f'The reversed number is {reverser(45678)}')

def palindrome(num):
    number = num
    reversedNum = reverser(number)
    if number == reversedNum:
        return True
    else:
        return False
    
print(f'The number you input in palindrome function is {palindrome(1221)}')