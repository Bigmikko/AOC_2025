# Advent of Code 2025
# Day 8
# Coded by Bigmikko in Python

# The different input file locations
TEST_INPUT_FILE = "day_8/test_input.txt"
INPUT_FILE = "day_8/input.txt"

# Switch between test input and the problem parts
PART2 = True
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

# A function that merges the circuits where box1 and box2 respectivly presides
def _adjustCircuits(box1, box2, circuits):
    for j in range(len(circuits)):

        # For the first box in vectors[i], it goes through the circuits until it finds the correspondig circuit. If both boxes exists, skip
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

def getCircuits(boxes, vectors):
    circuits = []

    # Creates a list of all of the boxes to be used for circuits, each circuit starts with one box in each
    for box in boxes:
        circuits.append([box])

    if not PART2:
        # Tries to only make the specified amount of circuits, if one already has both boxes (vectors[i][1] and vectors[i][2]) then it's skipped but (i) still advances
        for i in range(AMOUNT_OF_INDIVIDUAL_CIRCUITS):
            _adjustCircuits(vectors[i][1], vectors[i][2], circuits)

        # Orders the circuit by length descending
        circuits.sort(key=len, reverse=True)

        # The product is the top 3 sizes of circuits
        product = len(circuits[0]) * len(circuits[1]) * len(circuits[2])

    else:
        # This loop is ugly, it keeps going until there is only 1 big circuit
        i = -1
        while len(circuits) > 1:
            i += 1
            _adjustCircuits(vectors[i][1], vectors[i][2], circuits)
        
        # The product is the last two x values multiplied together
        product = vectors[i][1][0] * vectors[i][2][0]

    return product

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