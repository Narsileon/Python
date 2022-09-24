import settings

def fire(grid, ships):
    row, col = validate_fire(grid)
    print("")
    print("----------------------------")

    # Missed.
    if grid[row][col] == settings.empty:
        print("You missed!")
        grid[row][col] = settings.missed
    
    # Hit.
    elif grid[row][col] == settings.ship:
        print("You hit!", end=" ")
        grid[row][col] = settings.hit
        
        if validate_ship_destruction(grid, ships, row, col):
            print("A ship was sunk!")
            return 1
        else:
            print("A ship was shot!")
            
    print("----------------------------")
    print("")
    return 0

def validate_fire(grid):
    is_target_valid = False
    
    row = -1
    col = -1
    
    maxLetter = settings.alphabet[settings.size_y - 1]
    maxNumber = settings.size_x - 1
    errorMessage = "Error: Please enter row (A-{}) and column (0-{}), for example B2".format(maxLetter, maxNumber) 
    
    while is_target_valid is False:
        target = input("Enter row (A-J) and column (0-9) such as A3: ")
        target = target.upper()
        
        if len(target) < 2 or len(target) > 3:
            print("Error: Please enter only one row and one column (for example B2).")
            continue
        
        row = target[0]
        col = target[1:]
        
        if not row.isalpha() or not col.isnumeric():
            print(errorMessage)
            continue
        row = settings.alphabet.find(row)
        if not (-1 < row < settings.size_y):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        col = int(col)
        if not (-1 < col < settings.size_x):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        if grid[row][col] == "#" or grid[row][col] == "X":
            print("You have already shot a bullet here, pick somewhere else")
            continue
        if grid[row][col] == "." or grid[row][col] == "O":
            is_target_valid = True
    return row, col

def validate_ship_destruction(grid, ships, row, col):
    for position in ships:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        
        #Check if we found a ship.
        if start_row <= row <= end_row and start_col <= col <= end_col:
            for y in range(start_row, end_row):
                for x in range(start_col, end_col):
                    if grid[y][x] != settings.hit:
                        return False
                    
    return True