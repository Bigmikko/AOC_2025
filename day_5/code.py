#Advent of Code 2025
#Day 5
#Coded by Bigmikko in Python

#The different input file locations
TEST_INPUT_FILE = "day_5/test_input.txt"
INPUT_FILE = "day_5/input.txt"

#Switch between test input and the problem parts
PART2 = True
TEST_INPUT = False

#FOR PART2, function takes a list of ranges and returns the amount of unique ids in those ranges
def getRanges(ranges):
    i = 0

    #Merges ranges if they are overlapping or consecutive
    while(i < len(ranges) - 1):
        newRange = []

        #Checks if the next range overlaps
        if ranges[i][1] >= ranges[i + 1][0] - 1:
            newRange.append(ranges[i][0])
            
            #Checks if the current range or the next range has the largest ending value
            if ranges[i][1] <= ranges[i + 1][1]:
                newRange.append(ranges[i + 1][1])
            else:
                newRange.append(ranges[i][1])

            #Removes both old entries and inserts the newly created merged entry
            ranges.pop(i)
            ranges.pop(i)
            ranges.insert(i, newRange)
        else:
            i += 1

    #Adds together the amount of range entries
    sum = 0
    for start, end in ranges:
        sum += end - start + 1
    return sum

#For PART1, takes a number and a range and checks if that number exists in that range, returns a bool
def checkId(number, ranges):
    for i in range(0, len(ranges)):
        if number >= ranges[i][0] and number <= ranges[i][1]:
            return True
    return False


#Main function starts here
#Switches between the test and normal inputs
if TEST_INPUT == True:

    file = TEST_INPUT_FILE
else:
    file = INPUT_FILE

isRange = True

ranges = []
ids = []
sum = 0

#Opens the file and saves the part before a blank line into a list of ranges and after the blank line into a list of ids
with open(file) as f:
    for row in f:
        row = row.replace("\n", "")

        if row == '':
            isRange = False
            continue

        if isRange == True:
            row = row.split('-')
            currentRange = []
            currentRange.append(int(row[0]))
            currentRange.append(int(row[1]))
            ranges.append(currentRange)

        else:
            row = int(row)
            ids.append(row)

if PART2:
    ranges.sort()
    sum = getRanges(ranges)

else:
    for id in ids:
        if checkId(id, ranges):
            sum += 1

print(sum)
