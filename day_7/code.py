# Advent of Code 2025
# Day 7
# Coded by Bigmikko in Python

# Imports
import numpy as np

# The different input file locations
TEST_INPUT_FILE = "day_7/test_input.txt"
INPUT_FILE = "day_7/input.txt"

# Switch between test input and the problem parts
PART2 = True
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

# A function that finds start ("S") in the first row, returns the column
def find_start(diagram_tm):
    for i in range(len(diagram_tm[0])):
        if diagram_tm[0, i] == "S":
            return i

# A recursive function that finds every path through diagram_tm
def recursiveTimelineFinder(diagram_tm, row, col, solved_timelines):

    # Initiates sum of timelines
    sum = 0

    # For every row before the last one
    if row < len(diagram_tm):

        # If this path has already been solved, return the solution
        if (row, col) in solved_timelines:
            return solved_timelines[(row, col)]
        
        # If a splitter is encountered, call the recursive function for both timelines
        elif diagram_tm[row, col] == "^":
            sum += recursiveTimelineFinder(diagram_tm, row + 1, col - 1, solved_timelines)
            sum += recursiveTimelineFinder(diagram_tm, row + 1, col + 1, solved_timelines)

        # If there is no splitter, go down one row and continue the search
        else:
            sum += recursiveTimelineFinder(diagram_tm, row + 1, col, solved_timelines)

        # When the current branch is solved, add the sum to the solved_timelines dictionaries with the current position as key
        solved_timelines[(row, col)] = sum

        # Return sum at the end of the current recursion
        return sum
    
    # In on the last row, returns 1
    else:
        return 1

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

# Part 1
# Goes through every entry in the array to check and adjust it for the beam
if not PART2:
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

# Part 2
else:
    # Finds the start column
    start_col = find_start(diagram_tm)

    # Calls recursiveTimelineFinder function to find every timeline 
    timeslines = recursiveTimelineFinder(diagram_tm, 1, start_col, solved_timelines={})

    print(timeslines)
