def get_sum(file):
    sum = 0

    for line in open(file, "r").readlines():
        string = list(line)

        # Get Game-Number
        if string[8] == ':':
            currentGame = int(str(string[5]) + str(string[6]) + str(string[7]))
        elif string[7] == ':':
            currentGame = int(str(string[5]) + str(string[6]))
        elif string[6] == ':':
            currentGame = int(string[5])

        last_digit, blue_count, green_count, red_count = 0, 0, 0, 0

        for pos in range(int(len(string))): # Loop through the split up line
            # get cube amounts
            if string[pos].isdigit() and not string[pos - 1].isdigit(): 
                if string[pos + 1].isdigit():
                    last_digit = int(str(string[pos]) + str(string[pos + 1]))
                else:
                    last_digit = string[pos]

            # Check if we reached end of line
            if (pos + 2) > len(string):
                break

            # Check for color
            if string[pos] == 'b' and int(last_digit) > blue_count: # 'b' only occurs in 'blue'
                blue_count = int(last_digit)
            elif string[pos] == 'g' and string[pos + 1] == 'r' and int(last_digit) > green_count: # 'gr' only occurs in 'green'
                green_count = int(last_digit)
            elif string[pos] == 'r' and string[pos + 1] == 'e' and string[pos + 2] == 'd' and int(last_digit) > red_count: # 'red' only occurs in 'red'
                red_count = int(last_digit)
            
        # If Conditions are met add game number to sum
        if red_count <= 12 and green_count <= 13 and blue_count <= 14:
            sum += int(currentGame)

    return sum

print(get_sum("input.txt"))
