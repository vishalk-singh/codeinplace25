from karel.stanfordkarel import *

"""
File: 2025karel.py
----------------------------
Karel completes a puzzle by:
1. Karel picks two stacks of beepers (20 and 25)
2. Karel starts at position (1,1) facing East.
3. Karel picks up the beepers and places them in the correct position.
Note: Returning to starting position (bottom-left corner) will complete the puzzle.
"""
def main():
    pick_all_beepers()
    move()
    move()
    put_all_beepers_from_bag()
def put_all_beepers_from_bag():
    while beepers_in_bag():
            put_beeper()

def turn_around():
    turn_left()
    turn_left()

def move_safely():
    if front_is_clear():
        move()

def pick_all_beepers():
    while beepers_present():
        if beepers_present():
            pick_beeper()




# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
