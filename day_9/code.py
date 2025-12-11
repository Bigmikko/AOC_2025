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

# Legacy
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

# Legacy
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

# Legacy
def _checkAndFillShapes(grid):
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] in ("X", "#"):
                if j < grid.shape[1]:
                    for k in range(j + 1, grid.shape[1]):
                        if grid[i, k] in ("X", "#"):
                            for l in range(k - 1, j, -1):
                                if grid[i, l] in ("X", "#"):
                                    break
                                else:
                                    grid[i, l] = "O"

# Legacy
def _checkAndDrawGreenTiles(tile, grid):
    for i in range(tile[1] - 1, -1, -1):
        if grid[i, tile[0]] == "#":
            for j in range(i + 1, tile[1]):
                grid[j, tile[0]] = "X"

    for i in range(tile[0] + 1, grid.shape[1]):
        if grid[tile[1], i] == "#":
            for j in range(i - 1, tile[0], -1):
                grid[tile[1], j] = "X"
    
# Legacy    
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

    grid = np.full([largest_y - smallest_y, largest_x - smallest_x], ".", dtype = str)
    
    for tile in tiles:
        grid[tile[1], tile[0]] = "#"

    for tile in tiles:
        _checkAndDrawGreenTiles(tile, grid)
        _checkAndFillShapes(grid)

    return grid

# Legacy
def _checkAndAddGreenTiles(tile, allowed_positions, largest_x, largest_y):
    for i in range(len(allowed_positions)):
        if tile == allowed_positions[i]:
            for j in range(tile[0] + 1, largest_x + 1):
                if (j, tile[1]) in allowed_positions:
                    for k in range(j - 1, tile[0], -1):
                        allowed_positions.append((k, tile[1]))

            for j in range(tile[1] + 1, largest_y + 1):
                if (tile[0], j) in allowed_positions:
                    for k in range(j - 1, tile[1], -1):
                        allowed_positions.append((tile[0], k))

# Legacy
def _sortAndRemoveDuplicates(allowed_positions):
    allowed_positions.sort()
    i = 0
    while(True):
        if i >= len(allowed_positions) - 1:
            break
        if allowed_positions[i] == allowed_positions[i + 1]:
            allowed_positions.pop(i)
            i -= 1
        i += 1

# Legacy
def _createRanges(allowed_positions):
    allowed_range = []
    current_range = []

    current_row = -1

    for i in range(len(allowed_positions)):

        if current_row < 0:
            current_row = allowed_positions[i][0]
            start_col = allowed_positions[i][1]

        elif current_row != allowed_positions[i][0]:
            current_range.append(current_row)
            current_range.append(range(start_col, allowed_positions[i - 1][1]))
            allowed_range.append(current_range)
            current_range = []
            current_row = allowed_positions[i][0]
            start_col = allowed_positions[i][1]

        elif i == len(allowed_positions) - 1:
            current_range.append(current_row)
            current_range.append(range(start_col, allowed_positions[i][1]))
            allowed_range.append(current_range)

    return allowed_range

# Legacy
def _createShapes(allowed_positions):
    shapes = []
    amount_of_shapes = 0
    current_shape = []
    print("Making shapes")
    for i in range(len(allowed_positions)):
        if len(current_shape) == 0:
            amount_of_shapes += 1
            current_shape.append(allowed_positions[i])
        elif amount_of_shapes > 0:
            is_pos_found = False
            for j in range(len(shapes)):
                for k in range(len(shapes[j])):
                    if allowed_positions[i][0] == shapes[j][k][0] or allowed_positions[i][1] == shapes[j][k][1]:
                        for pos in current_shape:
                            shapes[j].append(pos)
                        current_shape = []
                        amount_of_shapes -= 1
                        is_pos_found = True
                        break

                if is_pos_found:
                        break
            if not is_pos_found:
                shapes.append(current_shape)
                current_shape = []
    i = 0
    print("Making shapes complete")
    while(True):
        temp_shape = 0
        if i >= len(shapes) - 1:
            break

        for j in range(len(shapes[i])):
            for k in range(i + 1, len(shapes)):
                for l in range(len(shapes[k])):
                    if shapes[i][j][0] == shapes[k][l][0] or shapes[i][j][1] == shapes[k][l][1]:
                        temp_shape = shapes[i] + shapes[k]
                        shapes.pop(k)
                        shapes.pop(i)
                        shapes.append(temp_shape)
                        break
                if temp_shape != 0:
                    break
            if temp_shape != 0:
                    break
        if temp_shape == 0 and i >= len(shapes) - 1:
            break
        elif temp_shape != 0:
            i = 0

        else:
            i += 1
    print("Shapes done")
    return shapes

# Legacy
def _createAllowedList(tiles):

    largest_x = -1
    largest_y = -1
    
    for tile in tiles:
        if tile[0] > largest_x:
            largest_x = tile[0]
        if tile[1] > largest_y:
            largest_y = tile[1]

    allowed_positions = []

    for tile in tiles:
        allowed_positions.append(tile)

    for tile in tiles:
        print(f"Green Tiles")
        _checkAndAddGreenTiles(tile, allowed_positions, largest_x, largest_y)

    print(f"Sort and remove duplicates")
    # Remove duplicates
    _sortAndRemoveDuplicates(allowed_positions)

    shapes = _createShapes(allowed_positions)

    print(len(shapes))

    return shapes

# A function that checks if the rectangle has any line that intersects it
def _checkRectangleAllowed(rectangle, shapes):

    if rectangle[1][0] >= rectangle[2][0]:
        large_x = rectangle[1][0]
        small_x = rectangle[2][0]
    else:
        large_x = rectangle[2][0]
        small_x = rectangle[1][0]

    if rectangle[1][1] >= rectangle[2][1]:
        large_y = rectangle[1][1]
        small_y = rectangle[2][1]
    else:
        large_y = rectangle[2][1]
        small_y = rectangle[1][1]

    # This checks if any lines intersect the rectangle
    for i in range(len(shapes[0]) - 1):

        if shapes[0][i][0] == shapes[0][i + 1][0]:
            if shapes[0][i][0] in range(small_x + 1, large_x):
                if shapes[0][i][1] < shapes[0][i + 1][1]:
                    if shapes[0][i][1] in range(small_y + 1, large_y) or shapes[0][i + 1][1] in range(small_y + 1, large_y) or shapes[0][i][1] < small_y <= large_y <= shapes[0][i + 1][1]:
                        return False
                elif shapes[0][i + 1][1] in range(small_y + 1, large_y) or shapes[0][i][1] in range(small_y + 1, large_y) or shapes[0][i + 1][1] < small_y <= large_y <= shapes[0][i][1]:
                    return False
                
        elif shapes[0][i][1] == shapes[0][i + 1][1]:
            if shapes[0][i][1] in range(small_y + 1, large_y):
                if shapes[0][i][0] < shapes[0][i + 1][0]:
                    if shapes[0][i][0] in range(small_x + 1, large_x) or shapes[0][i + 1][0] in range(small_x + 1, large_x) or shapes[0][i][0] < small_x <= large_x <= shapes[0][i + 1][0]:
                        return False
                elif shapes[0][i + 1][0] in range(small_x + 1, large_x) or shapes[0][i][0] in range(small_x + 1, large_x) or shapes[0][i + 1][0] < small_x <= large_x <= shapes[0][i][0]:
                    return False
            

    return True

# Adds next consecutive tile to the shape
def _addNextTile(tiles, shape):
    for i in range(len(tiles)):

        # Checks if the x or y matches the last one in "shape"
        if shape[-1][1] == tiles[i][1] or shape[-1][0] == tiles[i][0]:
            shape.append(tiles[i])
            tiles.pop(i)
            return True
    return False

# A function that puts all of the tiles in order ex: (1,2)(3,2)(3,5)(6,5)(6,8)(1,8)
def _getAllowedShapes(tiles):

    shapes = []

    not_found_tiles = tiles.copy()

    # Goes through all of the tiles and creates a shape for each consecutive shape from the input
    while(len(not_found_tiles) > 0):
        current_shape = []
        current_shape.append(not_found_tiles[0])
        not_found_tiles.pop(0)
        new_tiles_found = True
        while(new_tiles_found):
            new_tiles_found = _addNextTile(not_found_tiles, current_shape)
        shapes.append(current_shape)

    return shapes

# A function that takes the position of 1x1 tiles and checks the largest rectangle possible out of the points in the tiles positions
def largestRectangle(tiles):

    # Saves the current largest area and tiles in possible_tiles (area, tile1, tile2)
    rectangles = []
    #allowed_tiles = _createAllowedTiles(tiles)
    #grid = _createAllowedGrid(tiles)
    #allowed_ranges = _createRanges(shapes)
    #print(allowed_ranges)
    #print(f"Amount of shapes: {shapes}")
    # Loops through all tiles and compares them to all other tiles to get the largest area possible
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            # Get the area from the _getArea() function, if it's bigger than the current largest area, save the new one in possible_tiles
            area = _getArea(tiles[i], tiles[j])
            rectangle = (area, tiles[i], tiles[j])
            rectangles.append(rectangle)

    # Rectangles are in order, largest area first, to make sure the first rectangle, where no lines are intersected, is returned
    rectangles.sort(reverse = True)

    # If part2, checks if the rectangle gets intersected by a line
    if PART2:
        i = 1
        shapes = _getAllowedShapes(tiles)
        for rectangle in rectangles:
            print(f"Checking {i}/{len(rectangles)}")
            i += 1
            if _checkRectangleAllowed(rectangle, shapes):
                print(rectangle)
                return rectangle

    return rectangles[0][0]

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

#red_tiles = np.genfromtxt(file, dtype=int, delimiter=",")

# Gets the largest possible rectangle from the tiles provided
area = largestRectangle(red_tiles)

print(area)