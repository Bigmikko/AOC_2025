#Advent of Code 2025
#Day 3
#Coded by Bigmikko in Python

#The different input file locations
TEST_INPUT_FILE = "day_4/test_input.txt"
INPUT_FILE = "day_4/input.txt"

#Switch between test input and the problem parts
PART2 = False
TEST_INPUT = True


def checkNeighbours(x, y, grid):
    adjacentRolls = 0

    if x < len(grid[x]) - 1:
        if grid[x + 1][y] == '@':
            adjacentRolls += 1

    if x > 0:
        if grid[x - 1][y] == '@':
            adjacentRolls += 1

    if y > 0:
        if grid[x][y - 1] == '@':
            adjacentRolls += 1
        if x > 0:
            if grid[x - 1][y - 1] == '@':
                adjacentRolls += 1
        if x < len(grid[x]) - 1:
            if grid[x + 1][y - 1] == '@':
                adjacentRolls += 1

    if y < len(grid) - 1:
        if grid[x][y + 1] == '@':
            adjacentRolls += 1
        if x > 0:
            if grid[x - 1][y + 1] == '@':
                adjacentRolls += 1
        if x < len(grid[x]) - 1:
            if grid[x + 1][y + 1] == '@':
                adjacentRolls += 1

    if adjacentRolls < 4:
        return True
    else:
        return False
#Recursive function that that takes a string of numbers, and finds the largest subnumber 
# that is in order but not consecutive with the length of 'digits'
def calculateAvailableRolls(grid):
    sum = 0
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):

            if checkNeighbours(x, y, grid):
                sum += 1
    return sum


#Main function starts here

#Switches between the test and normal inputs
if TEST_INPUT == True:
    file = TEST_INPUT_FILE
else:
    file = INPUT_FILE

#Changes the amount of digits depending on if it's part 1 or part 2
if PART2:
    digits = 12
else:
    digits = 2

grid = []
line = []
#Opens the file, for all the entries, calls the function 'FindLargestNumber'
with open(file) as f:
    for row in f:
        row = row.replace("\n", "")
        for content in row:
           line.append(content)
        grid.append(line)
        line = []
sum = calculateAvailableRolls(grid)
print(sum)