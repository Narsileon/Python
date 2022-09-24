import settings

def fire(grid, ships):
    row, col = validate_fire(grid)
    print("")
    print("------------------------------")

    # Missed.
    if grid[row][col] == settings.empty:
        print("Leider haben Sie verpasst.")
        grid[row][col] = settings.missed
    
    # Hit.
    elif grid[row][col] == settings.ship:
        print("Erfolgreicher Schuss!", end=" ")
        grid[row][col] = settings.hit
        
        if validate_ship_destruction(grid, ships, row, col):
            print("Ein Schiff wurde versenkt!")
            return 1
        else:
            print("Ein Schiff wurde erschossen!")
            
    print("------------------------------")
    print("")
    return 0

def validate_fire(grid):
    is_target_valid = False
    
    row = -1
    col = -1
    
    maxLetter = settings.alphabet[settings.size_y - 1]
    maxNumber = settings.size_x - 1
    errorMessage = "Fehler: Bitte geben Sie Zeile (A-{}) und Spalte (0-{}) ein (z. B. E4): ".format(maxLetter, maxNumber) 
    
    while is_target_valid is False:
        target = input("Bitte geben Sie die Koordinate ein (z. B. E4): ".format(maxLetter, maxNumber))
        target = target.upper()
        
        if len(target) < 2 or len(target) > 3:
            print("Fehler: Bitte geben Sie nur eine Zeile und eine Spalte ein (z. B. E4): ")
            continue
        
        row = target[0]
        col = target[1:]
        
        if not row.isalpha() or not col.isnumeric():
            print(errorMessage)
            continue
        row = settings.alphabet.find(row)
        if not (-1 < row < settings.size_y):
            print("Fehler: Bitte geben Sie die Koordinate mit einer Zeile zwischen A und {} ein: ".format(maxLetter))
            continue
        col = int(col)
        if not (-1 < col < settings.size_x):
            print("Fehler: Bitte geben Sie die Koordinate mit einer Spalte zwischen 0 und {} ein: ".format(maxNumber))
            continue
        if grid[row][col] == "#" or grid[row][col] == "X":
            print("Sie haben bereits auf diese Koordinate geschossen, suchen Sie sich eine andere aus: ")
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