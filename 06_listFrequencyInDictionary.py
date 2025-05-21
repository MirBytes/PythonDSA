nums = [1, 1, 5, 7, 5, 8, 9, 9, 1]

def FrequencyChecker(list):
    frequency_map = dict()

    for i in range (0, len(list)):
        if list[i] in frequency_map:
            frequency_map[list[i]] += 1
        else:
            frequency_map[list[i]] = 1

    return frequency_map

print(f'Frequency of Digits in List is {FrequencyChecker(nums)}')

def occurenceChecker(list, number):
    occurence = 0
    for i in range (0, len(list)):
        if number == list[i]:
            occurence += 1
    
    return occurence

print(f'Occurence of 1 in list is {occurenceChecker(nums, 1)}')

def HASHFrequencyChecker(list):
    hash_map = dict()

    for i in range (0, len(list)):
        hash_map[list[i]] = hash_map.get(list[i], 0) + 1

    return hash_map

print(f'Frequency of Digits in List is {HASHFrequencyChecker(nums)}')