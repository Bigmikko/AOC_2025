# Advent of Code 2025
# Day 9
# Coded by Bigmikko in Python

# The different input file locations
TEST_INPUT_FILE = "day_9/test_input.txt"
INPUT_FILE = "day_9/input.txt"

# Switch between test input and the problem parts
PART2 = False
TEST_INPUT = False

# A function that takes 2 points and calculates the area between the two points 
# adds one to each line since a point counts as a 1x1 tile
def _getArea(p1, p2):

    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

# A function that takes the position of 1x1 tiles and checks the largest rectangle possible out of the points in the tiles positions
def largestRectangle(tiles):

    # Saves the current largest area and tiles in possible_tiles (area, tile1, tile2)
    possible_tiles = [-1, -1, -1]

    # Loops through all tiles and compares them to all other tiles to get the largest area possible
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):

            # Get the area from the _getArea() function, if it's bigger than the current largest area, save the new one in possible_tiles
            area = _getArea(tiles[i], tiles[j])
            if(area > possible_tiles[0]):
                possible_tiles = (area, tiles[i], tiles[j])

    return possible_tiles


# Main function starts here

# Switches between the test and normal inputs
if TEST_INPUT == True:
    file = TEST_INPUT_FILE
else:
    file = INPUT_FILE

red_tiles = []

# Saves each row in a list of a red tiles (x, y)
with open(file) as f:
    for row in f:
        red_tile = tuple(map(int, row.strip().split(",")))
        red_tiles.append(red_tile)

# Gets the largest possible rectangle from the tiles provided
area = largestRectangle(red_tiles)

print(area)