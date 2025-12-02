#Advent of Code 2025
#Day 2
#Coded by Bigmikko in Python

#Amount of dial values and where the dial starts
TEST_INPUT_FILE = "day_2/test_input.txt"
INPUT_FILE = "day_2/input.txt"

#Switch between test input and the problem parts
PART2 = True
TEST_INPUT = False

#Takes a value, check if it has duplicate in all of it's substring, for part one, only first half and second half is compared
#For part 2, check all of the possible substrings if it consist only of duplicate numbers
def checkValue(value):

    #If the number has two digits, else return 0
    if value < 10:
        return 0
    
    value = str(value)

    #Range is 1 to half of the length of the number being checked for duplicates
    for i in range(1,(len(value)//2) + 1):
        
        #If it's part 1, make sure it only calculates it if it's divisible 2
        #and it's exactly half the number compared with the other half 

        #For part 2, check is the value consists only of duplicates, no matter the length, like 111 (1) or 1212 (12) or 245245245 (245)
        if not PART2 and (i != len(value)//2 or len(value) % 2 != 0) :
            continue

        else:
            subValues = []

            #Takes each substring of length i
            subValues = [value[j:j+i] for j in range(0, len(value), i)]

            #Checks each entry in subValue against eachother, if they are all the same, return the whole value
            for k in range(0, len(subValues) - 1):

                #If it's not a duplicate, skip that step
                if subValues[k] != subValues[k+1]:
                    break

                #If at the end of the current length numbers being compared and they have all matched so far, return number
                elif k == len(subValues) - 2:
                    return int(value)
            
    return 0

#For each number in range, call checkValue function, sum up the numbers and return the sum
def checkRange(startValue, endValue):
    sum = 0
    for value in range(startValue, endValue + 1):
        sum += checkValue(value)
    return sum


#Main function starts here

#Switches between the test and normal inputs
if TEST_INPUT == True:
    file = TEST_INPUT_FILE
else:
    file = INPUT_FILE

#Reads the file and save it in ranges
finput = open(file)
ranges = finput.read().split(',')
finput.close()

sum = 0

#For all the entries, split the input in to start and end of range, calls checkRanges and outputs the result
for i in ranges:
    values = i.split('-')
    values = [int(v) for v in values]
    sum += checkRange(values[0], values[1])

print(sum)