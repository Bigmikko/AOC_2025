DIAL_VALUES = 100
DIAL_START_VALUE = 50
INPUT_FILE = "day_1/input.txt"
PART2 = True

def rotate(uinput):
    global dial
    global password

    if uinput[0] == 'R':
        clockwise = True
    elif uinput[0] == 'L':
        clockwise = False
    else:
        print("Invalid Input")

    rotation = int(uinput[1:])

    if not clockwise:
        rotation = -rotation
        
    if dial == 0 and dial + rotation < 0 and PART2:
        password -= 1
    dial += rotation

    while dial < 0 or dial >= DIAL_VALUES:
        if dial != 100 and PART2:
            password += 1
        if dial < 0:
            dial += DIAL_VALUES
        elif dial >= DIAL_VALUES:
            dial -= DIAL_VALUES

    if dial == 0:
        password += 1

dial = DIAL_START_VALUE
password = 0

with open(INPUT_FILE) as f:
    for line in f:
        rotate(line)
        print(dial)

print(password)