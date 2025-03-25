import hw5_util, math

def get_nbrs(row, col, rows, columns):
    neighbors = []
    
    if row - 1 >= 0:
        neighbors.append((row-1, col))

    if col - 1 >= 0:
        neighbors.append((row, col-1))

    if col + 1 <= columns-1:
        neighbors.append((row, col+1))

    if row + 1 <= rows-1:
        neighbors.append((row+1, col))

    return neighbors

def move(path, grid):
    # print(path)
    upward = downward = 0
    legit = True
    i = 1

    while legit and i < len(path):
        # If we increase along the row, we must not move along the column
        if path[i][0] + 1 == path[i-1][0] and path[i][1] == path[i-1][1]:
            # print("first")
            legit = True
        # If we decrease along the row, we must not move along the column
        elif path[i][0] - 1 == path[i-1][0] and path[i][1] == path[i-1][1]:
            legit = True
            # print("second")
        elif path[i][1] + 1 == path[i-1][1] and path[i][0] == path[i-1][0]:
            legit = True
            # print("third")
        elif path[i][1] - 1 == path[i-1][1] and path[i][0] == path[i-1][0]:
            legit = True
            # print("fourth")
        else:
            print("Path: invalid step from {0} to {1}".format(path[i-1], path[i]))
            upward = downward = 0
            legit = False

        # Get downward or upward
        if legit:
            if grid[path[i][0]][path[i][1]] > grid[path[i-1][0]][path[i-1][1]]:
                upward += abs(grid[path[i][0]][path[i][1]] - grid[path[i-1][0]][path[i-1][1]])
            else:
                downward += abs(grid[path[i][0]][path[i][1]] - grid[path[i-1][0]][path[i-1][1]])

        i+=1

    if legit:
        print("Valid path")
        print("Downward {}".format(downward))
        print("Upward {}".format(upward))
    
if __name__ == '__main__':
    grids = hw5_util.num_grids()
    grid_num = int(input("Enter a grid index less than or equal to 3 (0 to end): "))
    print(grid_num)
    print_grid = (input("Should the grid be printed (Y or N): "))
    print(print_grid)
    print_grid = print_grid.upper()


    grid = hw5_util.get_grid(grid_num)
    if print_grid == 'Y':
        print("Grid", grid_num)
        for i in range(0,len(grid)):
            print(end="  ")
            for j in range(0, len(grid[0]) - 1):
                print(grid[i][j], end="  ")
            print(grid[i][len(grid[i])-1])  
    
    print("Grid has {0} rows and {1} columns".format(len(grid), len(grid[0])))
    
    # Get neighbors
    start_locs = hw5_util.get_start_locations(grid_num)
    for i in start_locs:
        print("Neighbors of {}:".format(i),end = "")
        neighbors = get_nbrs(i[0], i[1], len(grid), len(grid[0]))
        for j in neighbors:
            print("", j, end="")
        print()

    # Check path
    move(hw5_util.get_path(grid_num), grid)
