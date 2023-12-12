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
