def extractor(num):
    number = num
    while number > 0:
        lastDigit = number % 10
        print(f'{lastDigit}')
        number = number // 10

extractor(45634)
