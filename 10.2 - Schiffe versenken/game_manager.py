import random, settings
import grid_generator, ship_generator
from player_manager import fire

grid = [[]]
ships = [[]]

ships_left = settings.ships_count
turns_left = settings.turns_count

game_over = False

def main():
    global ships_left

    settings.validate_settings()
    
    display_header()
    
    initialize_game()

    while game_over is False:
        grid_generator.print_grid(grid)
        
        display_stats()
        
        ships_left -= fire(grid, ships)
        
        try_end_game()

def initialize_game():
    global grid
    global ships
    
    grid = grid_generator.create_grid(grid)
    ships = ship_generator.create_ships(grid, ships)
    
def display_header():
    print("Schiffe versenken:")
    print("Sie haben {} Schüsse, um {} Schiffe zu zerstören.".format(settings.turns_count, settings.ships_count))
    print("")

def display_stats():
    print("Anzahl der verbleibenden Schiffe: " + str(ships_left))
    print("NAnzahl der verbleibenden Runden: " + str(turns_left))
    print("")

def try_end_game():
    global turns_left
    global game_over

    if ships_left <= 0:
        print("Herzlichen Glückwunsch, Sie haben gewonnen!")
        game_over = True
        
    else:
        turns_left -= 1
        
        if turns_left <= 0:
            print("Leider haben Sie verloren.")
            game_over = True

main()
