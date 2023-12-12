numbers_dict = {  # dictionary for string-conversion
    'one': 'one1one',
    'two': 'two2two',
    'three': 'three3three',
    'four': 'four4four',
    'five': 'five5five',
    'six': 'six6six',
    'seven': 'seven7seven',
    'eight': 'eight8eight',
    'nine': 'nine9nine',
}

pattern = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] # Pattern to get written numbers

actualStrings = [] # store converted file

def get_sum(file): # Function to replace written Numbers with actual numbers
    for line in open(file, "r").readlines(): # loop to convert written nums to actual digits
        for p in pattern:
            if p in line and not p.isdigit():
                current_letter = numbers_dict[p]
                line = line.replace(p, current_letter)
        actualStrings.append(line)
    
    sum = 0

    for line in actualStrings: # loop for digits only
        nums = []
        string = list(line)

        for num in string:
            if num.isdigit() == True:
                nums.append(num)

        sum += int(str(nums[0]) + str(nums[len(nums) - 1]))

    return sum

print(get_sum("input.txt"))


