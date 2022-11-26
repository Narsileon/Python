import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from localization import t

import random
import userinput

R0 = " ----- "
R1 = "|     |"
R2 = "| *   |"
R3 = "|  *  |"
R4 = "|   * |"
R5 = "| * * |"
R6 = "|  ?  |"

DICES = [
    [R0, R1, R6, R1, R0],
    [R0, R1, R3, R1, R0],
    [R0, R2, R1, R4, R0],
    [R0, R2, R3, R4, R0],
    [R0, R5, R1, R5, R0],
    [R0, R5, R3, R5, R0],
    [R0, R5, R5, R5, R0],
]

data = {}

def main():
    print("{}:".format(t("dices")))
    get_data()
    print("")
    display_dice()

def get_data():
    data["number"] = userinput.get_int(t("input_dice"))
    
def display_dice():
    if (1 <= data["number"] <= 6):
        print_dice(data["number"])
    else:
        print_dice(0)   
    
def print_dice(index):
    for i in DICES[index]:
        print(i)

def print_random_dice():
    print_dice(random.randint(1, 6))
        
main()
    