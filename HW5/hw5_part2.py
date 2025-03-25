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

def steepest(start_loc, grid, max_step):
    stop = False
    count = 0

    while not stop:
        # Find neighbors
        neighbors = get_nbrs(start_loc[0], start_loc[1], len(grid), len(grid[0]))
        if count > 4:
            count = 0
            print()
        print(start_loc, end=" ")

        loc = start_loc
        val = grid[start_loc[0]][start_loc[1]]
        higher = lower = step = 0
        valid_step = False

        # Compare all neighbors of the current location
        for i in neighbors:
            path_step = grid[i[0]][i[1]] - val
            if path_step > 0:
                higher += 1
                if path_step <= max_step:  # Valid step to a higher neighbor
                    if path_step > step:
                        loc = i
                        step = path_step
                    valid_step = True
            elif path_step < 0:
                lower += 1
                if abs(path_step) <= max_step:  # Valid step to a lower neighbor
                    valid_step = True

        # Check to see if we have a max or not
        if higher == len(neighbors) and not valid_step:
            return -2
        if lower == len(neighbors) and not valid_step:
            stop = True
            break

        # Move to the selected location if valid
        if start_loc == loc:
            stop = True
        else:
            start_loc = loc

        count +=1
    return grid[start_loc[0]][start_loc[1]]

def gradual(start_loc, grid, max_step):
    stop = False
    count = 0

    while not stop:
        # Find neighbors
        neighbors = get_nbrs(start_loc[0], start_loc[1], len(grid), len(grid[0]))
        if count > 4:
            count = 0
            print()
        print(start_loc, end=" ")

        step = max_step
        loc = start_loc
        val = grid[start_loc[0]][start_loc[1]]
        higher = lower = 0
        valid_step = False

        # Compare all neighbors of the current location
        for i in neighbors:
            path_step = grid[i[0]][i[1]] - val
            if path_step > 0:
                higher += 1
                if path_step <= max_step:  # Valid step to a higher neighbor
                    if path_step <= step:
                        loc = i
                        step = path_step
                    valid_step = True
            elif path_step < 0:
                lower += 1
                if abs(path_step) <= max_step:  # Valid step to a lower neighbor
                    valid_step = True

        # Check to see if we have a maximum or no max
        if higher == len(neighbors) and not valid_step:
            return -2
        if lower == len(neighbors) and not valid_step:
            stop = True
            break

        # Move to the selected location if valid
        if start_loc == loc:
            stop = True
        else:
            start_loc = loc

        count += 1

    return grid[start_loc[0]][start_loc[1]]


def find_global_max(grid):
    max = 0
    coordinates = [0, 0]

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] > max:
                max = grid[i][j]
                coordinates[0] = i
                coordinates[1] = j

    return (max, (coordinates[0],coordinates[1]))

if __name__ == '__main__':
    grids = hw5_util.num_grids()
    grid_num = int(input("Enter a grid index less than or equal to 3 (0 to end): "))
    print(grid_num)
    grid = hw5_util.get_grid(grid_num)

    max_step = int(input("Enter the maximum step height: "))
    print(max_step)

    out = input("Should the path grid be printed (Y or N): ")
    print(out)

    print("Grid has {0} rows and {1} columns".format(len(grid), len(grid[0])))
    global_max = find_global_max(grid)
    print("global max: {1} {0}".format(global_max[0], global_max[1]))

    # Get neighbors
    start_locs = hw5_util.get_start_locations(grid_num)
    for i in range(0,4):
        print("===")
        
        # Steepest path output
        print("steepest path") 
        steep = steepest(start_locs[i], grid, max_step)
        print()
        if steep == global_max[0]:
            print("global maximum")
        elif steep == -2:
            print("no maximum")
        else:
            print("local maximum")

        # gradual path output
        print("...")
        print("most gradual path")
        
        grad = gradual(start_locs[i], grid, max_step)
        print()
        if grad == global_max[0]:
            print("global maximum")
        elif grad == -2:
            print("no maximum")
        else:
            print("local maximum")

    print("===")
    print("Path grid")