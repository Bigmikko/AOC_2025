#Advent of Code 2025
#Day 4
#Coded by Bigmikko in Python

#The different input file locations
TEST_INPUT_FILE = "day_4/test_input.txt"
INPUT_FILE = "day_4/input.txt"

#Switch between test input and the problem parts
PART2 = True
TEST_INPUT = False


#Adds one to all of x, y, neighbours in the adjacencyGrid with out-of-bounds check
def adjacencyCorrection(x, y, adjacencyGrid):
    
    #Out-of-bounds check
    if x > 0:
        startX = x - 1
    else:
        startX = x

    if x < len(adjacencyGrid) - 1:
        endX = x + 2
    else:
        endX = x + 1

    if y > 0:
        startY = y - 1
    else:
        startY = y

    if y < len(adjacencyGrid[x]) - 1:
        endY = y + 2
    else:
        endY = y + 1

    #Adds 1 to all the valid neighbours
    for i in range(startX, endX):
        for j in range(startY, endY):
            if not (i == x and j == y):
                adjacencyGrid[i][j] += 1


#Creates a duplicate sized matrix of grid that contains info about the amount of neighbours surronding each entry
def createAdjacencyGrid(grid):
    adjacencyGrid = []

    #Create a duplicate sized grid that only contains '0'
    for i in range(0, len(grid)):
        tempRow = []
        for j in range(0, len(grid[i])):
            tempRow.append(0)
        adjacencyGrid.append(tempRow)
    
    #Adds one to each neighbour if the entry contains '@'
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            if grid[x][y] == '@':
                adjacencyCorrection(x, y, adjacencyGrid)

    return adjacencyGrid


#Function that takes a grid and returns how many rolls can be taken from that grid, if part 1, check one
# if part 2, iterate through it until none can be taken
def calculateAvailableRolls(grid):
    
    totalSum = 0
    while(True):
        #Calls the function to create a duplicate grid where each entry contains the amount of neighbours with a '@' it has 
        adjacencyGrid = createAdjacencyGrid(grid)

        sum = 0
        #Checks each entry if it has less than 4 neighbours and it also contains a roll
        # mark the roll as taken and adds to the sum
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                if adjacencyGrid[x][y] < 4 and grid[x][y] == '@':
                    grid[x][y] = 'x'
                    sum += 1

        totalSum += sum

        #If not part 2, return after one loop, otherwise, goes until the entire 2D matrix is solved
        if sum == 0 or not PART2:
            return totalSum


#Main function starts here

#Switches between the test and normal inputs
if TEST_INPUT == True:
    file = TEST_INPUT_FILE
else:
    file = INPUT_FILE

grid = []
line = []

#Opens the file and creates a 2D matrix
with open(file) as f:
    for row in f:
        row = row.replace("\n", "")
        for content in row:
           line.append(content)
        grid.append(line)
        line = []

sum = calculateAvailableRolls(grid)
print(sum)