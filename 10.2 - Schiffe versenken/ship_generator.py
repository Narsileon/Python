import random
import settings

def create_ships(grid, ships):   
    ships = []
    
    ships_placed = 0

    while ships_placed < settings.ships_count:
        row = random.randint(0, settings.size_y - 1)
        col = random.randint(0, settings.size_x - 1)
        direction = random.choice(["up", "right", "down", "left"])
        length = random.randint(settings.ship_size_min, settings.ship_size_max)
        
        if try_place_ship(grid, ships, row, col, direction, length):
            ships_placed += 1
            
    return ships;

def try_place_ship(grid, ships, row, col, direction, length):
    start_row = row
    end_row = row + 1
    start_col = col
    end_col = col + 1
    
    #Check if we have enough space above.
    if direction == "up":
        if row - length + 1 < 0:
            return False
        start_row = row - length + 1    

    #Check if we have enough space on the right.
    elif direction == "right":
        if col + length >= settings.size_x:
            return False
        end_col = col + length

    #Check if we have enough space below.
    elif direction == "down":
        if row + length >= settings.size_y:
            return False
        end_row = row + length
        
    #Check if we have enough space on the left.        
    elif direction == "left":
        if col - length + 1 < 0:
            return False
        start_col = col - length + 1

    return validate_ship_position(grid, ships, start_row, end_row, start_col, end_col)

def validate_ship_position(grid, ships, start_row, end_row, start_col, end_col):
    is_valid = True
    
    #Check if all positions are free.
    for y in range(start_row, end_row):
        for x in range(start_col, end_col):
            if grid[y][x] != settings.empty:
                is_valid = False
                break
    
    #Add ship if all positions are free.
    if is_valid:
        ships.append([start_row, end_row, start_col, end_col])
        for y in range(start_row, end_row):
            for x in range(start_col, end_col):
                grid[y][x] = settings.ship
                
    return is_valid