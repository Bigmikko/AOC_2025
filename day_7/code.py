# Advent of Code 2025
# Day 7
# Coded by Bigmikko in Python

# Imports
import numpy as np

# The different input file locations
TEST_INPUT_FILE = "day_7/test_input.txt"
INPUT_FILE = "day_7/input.txt"

# Switch between test input and the problem parts
PART2 = False
TEST_INPUT = False

# A function that adds "|" on each side of the current colum but one row below
def beamSplitting(diagram_tm, row, col):
    diagram_tm[row + 1, col - 1] = "|"
    diagram_tm[row + 1, col + 1] = "|"
    return diagram_tm

# A function to check if there is a beam hitting a splitter
def checkBeamSplitting(diagram_tm, row, col):
    if row > 0:
        if diagram_tm[row - 1, col] == "|":
            if diagram_tm[row, col] in "^":
                return True
    return False

# A function that continue the beam if there is a "." below the beam
def continueContinuousBeam(diagram_tm, row, col):
    if row < len(diagram_tm) - 1:
        if diagram_tm[row + 1, col] == ".":
            diagram_tm[row + 1, col] = "|"

# Main function starts here

# Switches between the test and normal inputs
if TEST_INPUT == True:
    file = TEST_INPUT_FILE
else:
    file = INPUT_FILE

# Adds the content to a numpy array called diagram_tm
diagram_tm = np.genfromtxt(file, dtype=str, delimiter=1)

# Initiates the amount of beam splits
beam_splits = 0

# Goes through every entry in the array to check and adjust it for the beam
for row in range(len(diagram_tm)):
    for col in range(len(diagram_tm[row])):
        # If start, add beam below
        if diagram_tm[row, col] == "S":
            continueContinuousBeam(diagram_tm, row, col)
        
        # If "^", calls beamSplitting
        elif checkBeamSplitting(diagram_tm, row, col):
            diagram_tm = beamSplitting(diagram_tm, row, col)

            # Every beamsplit except for "S" is counted towards beam_splits
            if diagram_tm[row, col] != "S":
                beam_splits += 1
        # Checks if the entry below current in a "." and the current one is a "|", then add the beam to row below
        elif diagram_tm[row, col] == "|":
            continueContinuousBeam(diagram_tm, row, col)

print(beam_splits)
