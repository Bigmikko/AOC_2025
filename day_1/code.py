#Advent of Code 2025
#Day 1
#Coded by Bigmikko in Python

#Amount of dial values and where the dial starts
DIAL_VALUES = 100
DIAL_START_VALUE = 50

#Switch between test input and the problem parts
TEST_INPUT_FILE = "day_1/test_input.txt"
INPUT_FILE = "day_1/input.txt"

#Switch between test input and the problem parts
PART2 = True
TEST_INPUT = False

#A function that takes the input and "spins" the dial, calculating multiple variables
def rotate(action):
    global dial
    global password

    #Checks the direction of the dial spin
    if action[0] == 'R':
        clockwise = True
    elif action[0] == 'L':
        clockwise = False
    else:
        print("Invalid Input")

    #Parses out the numbers after the initial 'R' or 'L'
    rotation = int(action[1:])

    if not clockwise:
        rotation = -rotation
        
    #Makes sure that you don't count 0 twice when starting on 0
    if dial == 0 and dial + rotation < 0 and PART2:
        password -= 1
    dial += rotation

    #Adds or removes dials numbers until it lands on a valid one, for part two, we count every iteration as passing 0 once
    while dial < 0 or dial >= DIAL_VALUES:
        if dial != 100 and PART2:
            password += 1
        if dial < 0:
            dial += DIAL_VALUES
        elif dial >= DIAL_VALUES:
            dial -= DIAL_VALUES

    if dial == 0:
        password += 1

#Main function starts here
dial = DIAL_START_VALUE
password = 0

#Switches between the test and normal inputs
if TEST_INPUT == True:
    file = TEST_INPUT_FILE
else:
    file = INPUT_FILE

#Reads the file and calls the rotate function for each row in the file
with open(file) as f:
    for action in f:
        rotate(action)

print(password)