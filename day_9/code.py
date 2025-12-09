# Advent of Code 2025
# Day 9
# Coded by Bigmikko in Python


# Imports
import numpy as np

# The different input file locations
TEST_INPUT_FILE = "day_9/test_input.txt"
INPUT_FILE = "day_9/input.txt"

# Switch between test input and the problem parts
PART2 = True
TEST_INPUT = False

# A function that takes 2 points and calculates the area between the two points 
# adds one to each line since a point counts as a 1x1 tile
def _getArea(p1, p2):

    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def _addTilesToGrid(allowed_grid, tile1, tile2):
    if tile1[0] == tile2[0]:
        if tile1[1] > tile2[1]:
            for i in range(tile2[1], tile1[1] + 1):
                pos = []
                pos.append(tile1[0])
                pos.append(i)
                #if pos not in allowed_grid:
                allowed_grid.append(pos)
        else:
            for i in range(tile1[1], tile2[1] + 1):
                pos = []
                pos.append(tile1[0])
                pos.append(i)
                #if pos not in allowed_grid:
                allowed_grid.append(pos)

    elif tile1[1] == tile2[1]:
        if tile1[0] > tile2[0]:
            for i in range(tile2[0], tile1[0] + 1):
                pos = []
                pos.append(i)
                pos.append(tile1[1])
                #if pos not in allowed_grid:
                allowed_grid.append(pos)
        else:
            for i in range(tile1[0], tile2[0] + 1):
                pos = []
                pos.append(i)
                pos.append(tile1[1])
                #if pos not in allowed_grid:
                allowed_grid.append(pos)

def _createAllowedTiles(tiles):
    allowed_tiles = []
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            _addTilesToGrid(allowed_tiles, tiles[i], tiles[j])

    allowed_tiles.sort()
    i = 1
    while(i < len(allowed_tiles)):
    #for i in range(len(allowed_tiles) - 1):
        if allowed_tiles[i - 1] == allowed_tiles[i]:
            allowed_tiles.pop(i - 1)
        i += 1

    current_col = -1
    allowed_tiles_ranges = []
    tile_range = []
    for i in range(len(allowed_tiles)):
        if i == 0:
            range_start = allowed_tiles[i][1]
            current_col = allowed_tiles[i][0]

        elif allowed_tiles[i][0] > current_col:
            range_end = allowed_tiles[i - 1][1]
            
            tile_range.append(current_col)
            tile_range.append(range_start)
            tile_range.append(range_end)
            allowed_tiles_ranges.append(tile_range)
            tile_range = []
            current_col = allowed_tiles[i][0]

            range_start = allowed_tiles[i][1]
        elif i == len(allowed_tiles) - 1:
            range_end = allowed_tiles[i][1]
            tile_range.append(current_col)
            tile_range.append(range_start)
            tile_range.append(range_end)
            allowed_tiles_ranges.append(tile_range)

        elif allowed_tiles[i][1] != allowed_tiles[i - 1][1] + 1 and allowed_tiles[i + 1][0] == allowed_tiles[i][0] and allowed_tiles[i - 1][1] == allowed_tiles[i][1]:
            range_end = allowed_tiles[i - 1][1]
            
            tile_range.append(current_col)
            tile_range.append(range_start)
            tile_range.append(range_end)
            allowed_tiles_ranges.append(tile_range)
            tile_range = []

            range_start = allowed_tiles[i][1]

    return allowed_tiles_ranges

def _checkAndFillShapes(grid):
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] in True:
                if j < grid.shape[1]:
                    for k in range(j + 1, grid.shape[1]):
                        if grid[i, k] in True:
                            for l in range(k - 1, j, -1):
                                if grid[i, l] in True:
                                    break
                                else:
                                    grid[i, l] = True

def _checkAndDrawGreenTiles(tile, grid):
    for i in range(tile[1] - 1, -1, -1):
        if grid[i, tile[0]] == True:
            for j in range(i + 1, tile[1]):
                grid[j, tile[0]] = True

    for i in range(tile[0] + 1, grid.shape[1]):
        if grid[tile[1], i] == True:
            for j in range(i - 1, tile[0], -1):
                grid[tile[1], j] = True

        
def _createAllowedGrid(tiles):
    smallest_x = 9999999999
    smallest_y = 9999999999
    largest_x = -1
    largest_y = -1

    for tile in tiles:
        if tile[0] < smallest_x:
            smallest_x = tile[0]
        if tile[1] < smallest_y:
            smallest_y = tile[1]
        if tile[0] > largest_x:
            largest_x = tile[0]
        if tile[1] > largest_y:
            largest_y = tile[1]

    for tile in tiles:
        tile[0] -= smallest_x
        tile[1] -= smallest_y

    largest_x += 1
    largest_y += 1

    grid = np.full([largest_y - smallest_y, largest_x - smallest_x], False, dtype = bool)
    
    for tile in tiles:
        grid[tile[1], tile[0]] = True

    for tile in tiles:
        _checkAndDrawGreenTiles(tile, grid)
        _checkAndFillShapes(grid)

    return grid

def _checkRectangleAllowed(p1, p2, grid):
    p3 = p1[1], p2[0]
    p4 = p2[1], p1[0]

    """for i in range(len(allowed_tiles)):
        if p3[0] == allowed_tiles[i][0]:
            if p3[1] in range(allowed_tiles[i][1], allowed_tiles[i][2] + 1):
                for j in range(len(allowed_tiles)):
                    if p4[0] == allowed_tiles[j][0]:
                        if p4[1] in range(allowed_tiles[j][1], allowed_tiles[j][2] + 1):
                            return True
                        
    return False """
    if grid[p3] not in (".") and grid[p4] not in ("."):
        return True
    else:
        return False


# A function that takes the position of 1x1 tiles and checks the largest rectangle possible out of the points in the tiles positions
def largestRectangle(tiles):

    # Saves the current largest area and tiles in possible_tiles (area, tile1, tile2)
    possible_tiles = [-1, -1, -1]
    #allowed_tiles = _createAllowedTiles(tiles)
    grid = _createAllowedGrid(tiles)

    # Loops through all tiles and compares them to all other tiles to get the largest area possible
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
 
            if PART2:
                rectangle_allowed = _checkRectangleAllowed(tiles[i], tiles[j], grid)

                if not rectangle_allowed:
                    break
                        
            # Get the area from the _getArea() function, if it's bigger than the current largest area, save the new one in possible_tiles
            area = _getArea(tiles[i], tiles[j])
            if(area > possible_tiles[0]):
                possible_tiles = (area, tiles[i], tiles[j])

    return possible_tiles[0]


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

red_tiles = np.genfromtxt(file, dtype=int, delimiter=",")

# Gets the largest possible rectangle from the tiles provided
area = largestRectangle(red_tiles)

print(area)