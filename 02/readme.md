# Day 02 Cube Conundrum

> [!NOTE]
> Day 02 was about filtering numbers bound to different colors in a game.

## Part 1
The first part was about checking if a game is valid in a given string. <br/>
```
Game 62: 6 red, 3 blue; 1 blue, 2 red, 2 green; 3 red, 1 blue
```

The conditions were that `red` would not exceed `12`, `green` would not exceed `13` and `blue` would not exceed `14`. <br/>
For this purpose I coded the script below. <br/>
```py
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
```

This script simply loops through the lines, checks all scores of different colored cubes and checks if it needs to add the game-ID to the sum.

## Part 2

Now the only thing which is different in part 2 is that we need to check for the highest numbered cube instead for the sum and remove the filter for amount of cubes. <br/>
Knowing this I changed the script just a bit to get the correct solution. <br/>
```py
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
            
        sum += int(blue_count * green_count * red_count)

    return sum

print(get_sum("input.txt"))
```

This script is essentially the same but simply multiplies the the highest amount of each color to get the correct sum.