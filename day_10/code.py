# Advent of Code 2025
# Day 10
# Coded by Bigmikko in Python

# The different input file locations
TEST_INPUT_FILE = "day_10/test_input.txt"
INPUT_FILE = "day_10/input.txt"

# Switch between test input and the problem parts
PART2 = True
TEST_INPUT = False


ITERATIONS = 0

# A function that cleans up the machines information, removes [] {} and makes a list of the switches
def parseMachines(machines):

    new_machines = []

    for machine in machines:
        new_machine = []
        machine_lights = list(machine[0].replace("[", "").replace("]", ""))
        joltage_requirements = list(map(int,machine[-1].replace("{", "").replace("}", "").split(",")))
        switches = []
        
        for i in range(1, len(machine) - 1):
            switches.append(machine[i].replace(")", "").replace("(", ""))

        list_of_switches = []

        for i in range(len(switches)):
            switch = list(map(int, switches[i].split(",")))
            list_of_switches.append(switch)

        list_of_switches = sorted(list_of_switches, key=len, reverse=True)

        new_machine.append(machine_lights)
        new_machine.append(joltage_requirements)
        new_machine.append(list_of_switches)

        new_machines.append(new_machine)

    return new_machines

# A function that takes the lights and 1 button press. It then returns the results of pressing that button
def _pressButton(button, lights):
         
    # Switches the buttons correspondig lights
    for i in range(len(button)):
        if PART2:
            lights[button[i]] -= 1

        else:       
            if lights[button[i]] == ".":
                lights[button[i]] = "#"

            elif lights[button[i]] == "#":
                lights[button[i]] = "."


# A function that takes a machine and a test and runs the test, if no combination of pressing buttons work, returns 1M, else returns the button presses
# A test is a for example 1 0 1, which means pressing the first and last buttons to change those lights
def _runTest(machine, test):

    lights = []

    # Makes a lights list with len(machine lights) and sets them all to off (".")
    for i in range(len(machine[0])):
        lights.append(".")

    button_presses = 0

    # Using the test, presses the button correspondig to a "1"
    for i in range(len(test)):
        if test[i] == 1:
            _pressButton(machine[2][i], lights)
            button_presses += 1

    # If the lights are in the prefered lights configuration, return the amount of button presses needed
    if lights == machine[0]:
        return button_presses

    else:
        return 1000000

# A function that takes an amount and creates a list of all of the binary numbers with size "amount", 2 for be [0 0, 0 1, 1 0, 1 1]
def _generateListOfTests(amount):
    tests = []

    # The list has to be length 2^amount
    for i in range(2 ** amount):
        test = []
        
        # The binary equivelent of i
        binary_number = "{0:b}".format(i)

        # Fills the start of the test with "0" so the length will be len(amount)
        for j in range(amount - len(binary_number)):
            test.append(0)
        
        # Adds the binary number at the end
        for j in range(len(binary_number)):
            test.append(int(binary_number[j]))

        tests.append(test)
    return tests      

def _recursiveJoltageCalculator(joltage, buttons):

    print(joltage)
    current_joltage = joltage.copy()

    for i in range(len(current_joltage)):
        if current_joltage[i] < 0:
            return 1000000
        
    for i in range(len(current_joltage)):    
        if current_joltage[i] != 0:
            break
    
        elif i == len(current_joltage) - 1:
            return 0
        
    priority_for_test = []
    for i in range(len(current_joltage)):
        priority_for_test.append((current_joltage[i], i))

    priority_for_test.sort(reverse=True)

    buttons_test = []
    buttons_copy = buttons.copy()

    for i in range(len(priority_for_test)):
        if len(buttons_copy) == 0:
            break
        for k in range(len(buttons_copy[0]), 0, -1):
            for j in range(len(buttons_copy)):
                if j >= len(buttons_copy):
                    break

                elif priority_for_test[i][1] in buttons_copy[j] and k == len(buttons_copy[j]):
                    buttons_test.append(buttons_copy[j])
                    buttons_copy.pop(j)
                    j -= 1


    x = 0

    for i in range(len(buttons)):

        test_joltage = current_joltage.copy()
        _pressButton(buttons_test[i], test_joltage)
        test = _recursiveJoltageCalculator(test_joltage, buttons_test)
        if test < 1000000:
            ITERATIONS = 0
            return test + 1



    #button_presses += _recursiveJoltageCalculator(joltage, buttons)

    return 1000000

# A function that takes a machine and calculates and returns the fewest amount of button presses needed to achieve that machines prefered lighting configuration
def getFewestButtonPresses(machine):

    fewest_button_presses = 100000

    if not PART2:
        # Generates the tests
        tests = _generateListOfTests(len(machine[2]))

        # Runs all of the tests, if a test has fewer button presses saves it
        for i in range(len(tests)):
            test_results = _runTest(machine, tests[i])
            if test_results < fewest_button_presses:
                fewest_button_presses = test_results
 
    else:
        fewest_button_presses = _recursiveJoltageCalculator(machine[1], machine[2])

    return fewest_button_presses

# Main function starts here

# Switches between the test and normal inputs
if TEST_INPUT == True:
    file = TEST_INPUT_FILE
else:
    file = INPUT_FILE

machines = []

# Saves each row in a list of a red tiles (x, y)
with open(file) as f:
    for row in f:
        machine = row.strip().split(" ")
        machines.append(machine)

machines = parseMachines(machines)

sum = 0
i = 0

for machine in machines:
    i += 1
    print(f"Machine: {i}")
    sum += getFewestButtonPresses(machine)

print(sum)