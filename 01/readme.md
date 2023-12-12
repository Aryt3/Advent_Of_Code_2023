# Day 01 Trebuchet?!

> [!NOTE]
> Day 01 was about filtering numbers from a file with a lot of strings.

## Part 1

The goal of the first part was to sort out digits and basically concatenate the first number found in a string with the last number found in a string. <br/>
Having a file as input I wrote a script to solve this. <br/>
```py
def get_sum(file):
    sum = 0

    for line in open(file, "r").readlines():
        nums = []
        string = list(line)

        for num in string:
            if num.isdigit() == True:
                nums.append(num)

        sum += int(str(nums[0]) + str(nums[len(nums) - 1]))

    return sum

print(get_sum("input.txt"))
```

In the script I simply go through each line, filter out the digits, concatenate them and at last print the result of all lines which concludes the first part.

## Part 2

Now this one was a bit harder because we also had to filter written numbers like `two`. <br/>
For this purpose I wrote a script in which I also used the solution of part 1. <br/>
```py
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
```

> [!NOTE]
> I msut say that I ran into a bug in my script because sometimes numbers are melted together as in `oneight`, for this reason I integrated my solution of converting written numbers like `1` into `one1one` which basically prevented the issue of fused numbers.