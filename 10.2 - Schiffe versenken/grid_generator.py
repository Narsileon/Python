import settings

def create_grid(grid):
    grid = []
    
    for y in range(settings.size_y):
        row = []
        for x in range(settings.size_x):
            row.append(settings.empty)
        grid.append(row)
        
    return grid

def print_grid(grid, debug_mode = False):
    alphabet = settings.alphabet[0: len(grid) + 1]

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")
    for y in range(len(grid)):
        print(alphabet[y], end=") ")
        for x in range(len(grid[y])):
            if grid[y][x] == settings.ship:
                if debug_mode:
                    print(settings.ship, end=" ")
                else:
                    print(settings.empty, end=" ")
            else:
                print(grid[y][x], end=" ")
        print("")
    print("")