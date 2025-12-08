# Advent of Code 2025
# Day 8
# Coded by Bigmikko in Python

# The different input file locations
TEST_INPUT_FILE = "day_8/test_input.txt"
INPUT_FILE = "day_8/input.txt"

# Switch between test input and the problem parts
PART2 = False
TEST_INPUT = False

# Some vector math for creating the distances between 2 vectors, v1 and v2
def _getVectorLength(v1, v2):
    x = v1[0] - v2[0]
    y = v1[1] - v2[1]
    z = v1[2] - v2[2]
    
    # This is pythagoras in 3 dimenstions d = sqrt(x^2 + y^2 + z^2)
    d = ((x**2)+(y**2)+(z**2))**(1/2)
    return d

# 
def getJunctionBoxesVectors(junction_boxes):
    junction_vectors = []

    # Loops through each box and then every other box with an index higher than that one, calls _getVectorLength to get the distance between the two boxes
    # it then creates a list called junction_vectors where each entry is as follows (distance, box1 coordinates, box2 coordinates)
    for i in range(len(junction_boxes)):
        for j in range(i + 1, len(junction_boxes)):
            junction_vector = (_getVectorLength(junction_boxes[i], junction_boxes[j]), junction_boxes[i], junction_boxes[j])
            junction_vectors.append(junction_vector)

    # It then sorts them based on distance
    junction_vectors.sort()
    return junction_vectors

def getCircuits(boxes, vectors):
    circuits = []

    # Creates a list of all of the boxes to be used for circuits, each circuit starts with one box in each
    for box in boxes:
        circuits.append([box])

    # Loops through the amount of circuits it will try and create
    for i in range(AMOUNT_OF_INDIVIDUAL_CIRCUITS):

        # For readability, they are renamed box1 and box2, it's sorted, with the first being the shortest distance and then ascending
        box1 = vectors[i][1]
        box2 = vectors[i][2]

        # For the first box in vectors[i], it goes through the circuits until it finds the correspondig circuit. If both boxes exists, skip
        for j in range(len(circuits)):
            if box1 in circuits[j] and box2 in circuits[j]:
                break
            else:
                if box1 in circuits[j]:
                    for k in range(len(circuits)):
                        # Appends the circuit where box2 exists to the circuit where box is
                        if box2 in circuits[k]:
                            for c in circuits[k]:
                                circuits[j].append(c)
                            # Removes the old box2 circuit
                            circuits.pop(k)
                            break
                    break
    # Orders the circuit by length descending
    circuits.sort(key=len, reverse=True)
    # Returns product of the 3 largest circuit sizes
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])

# Main function starts here


if TEST_INPUT:
    AMOUNT_OF_INDIVIDUAL_CIRCUITS = 10
else:
    AMOUNT_OF_INDIVIDUAL_CIRCUITS = 1000

# Switches between the test and normal inputs
if TEST_INPUT == True:
    file = TEST_INPUT_FILE
else:
    file = INPUT_FILE

#
junction_boxes = []

# Saves each junction box location as a list of 3 variables (x, y, z) in a list called junction_boxes
with open(file) as f:
    for row in f:
        junction_box = tuple(map(int, row.strip().split(",")))
        junction_boxes.append(junction_box)

# Get the distances between all of the boxes
junction_vectors = getJunctionBoxesVectors(junction_boxes)

# Uses the distances to create circuits between the boxes
circuits = getCircuits(junction_boxes, junction_vectors)


print(circuits)