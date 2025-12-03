#Advent of Code 2025
#Day 3
#Coded by Bigmikko in Python

#The different input file locations
TEST_INPUT_FILE = "day_3/test_input.txt"
INPUT_FILE = "day_3/input.txt"

#Switch between test input and the problem parts
PART2 = True
TEST_INPUT = False

#Recursive function that that takes a string of numbers, and finds the largest subnumber 
# that is in order but not consecutive with the length of 'digits'
def FindLargestNumber(number, digits):
    largestDigit = 0
    locationDigit = 0

    #Loops through the numbers between index 0 to the amount of digits that are necessary 
    # compares and saves the largest one in 'largestDigit', also save the index of it
    for i in range(0, len(number) - digits + 1):
        if int(number[i]) > largestDigit:
            largestDigit = int(number[i])
            locationDigit = i

    #If on the last digit, return from the recursive function
    if digits == 1:
        return largestDigit
    
    #Calls itself recursivly and adds the first number
    # it reduces the digit by 1 and removes the numbers that are ineligible
    # and it multiplies the current digit with the appropriate power of 10
    return (largestDigit*(10**(digits - 1))) + FindLargestNumber(number[locationDigit + 1:], digits - 1)


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

sum = 0

#Opens the file, for all the entries, calls the function 'FindLargestNumber'
with open(file) as f:
    for number in f:
        sum += FindLargestNumber(number.replace("\n", ""), digits)

print(sum)