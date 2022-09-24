import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math, mathf

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Legend:

empty = "."
ship = "O"
hit = "X"
missed = "#"

#Grid settings:

size_x = 10 #Value muss be between 5 and 26.
size_y = 10 #Value muss be between 5 and 26.

#Ships settings:

ship_size_min = 2 #Value muss be greater than or equal to 2.
ship_size_max = 5 #Value muss be less than or equal to 5.

ships_count = 5 #Value muss be less than or equal to (size_x * size_y / ship_size_max / 4).

#Game settings:

turns_count = 50 #Value muss be greater than or equal to 10.

def validate_settings():
    validate_grid_settings()
    validate_ship_settings()
    validate_game_settings()
    
def validate_grid_settings():
    global size_x
    global size_y
    
    size_min = 5
    size_max = 26

    size_x = mathf.clamp("size_x", size_x, size_min, size_max)
    size_y = mathf.clamp("size_y", size_y, size_min, size_max)
    
def validate_ship_settings():
    global ship_size_max
    global ship_size_min
    global ships_count
    
    size_min = 2
    size_max = 5

    ship_size_max = mathf.clamp("ship_size_max", ship_size_max, size_min, size_max)
    ship_size_min = mathf.clamp("ship_size_min", ship_size_min, size_min, ship_size_max)

    ships_count_min = 1
    ships_count_max = math.floor(size_x * size_y / ship_size_max / 4)
    
    ships_count = mathf.clamp("ships_count", ships_count, ships_count_min, ships_count_max)
    
def validate_game_settings():
    global turns_count
        
    turns_count_min = ships_count * ship_size_max
    turns_count_max = size_x * size_y
    
    turns_count = mathf.clamp("turns_count", turns_count, turns_count_min, turns_count_max)