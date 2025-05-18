from karel.stanfordkarel import *

"""
File: InvertBeepersKarel.py
----------------------------
Karel completes a puzzle by:
1. Karel move farward 5 times.
2. If beepers are there then she picks it up otherwise she puts the beepers.
3. She returns to starting position (bottom-left corner) facing East.
"""
def main():
    invert_beeper()
    go_home()

def invert_beeper():
    while front_is_clear():
        pick_all_beepers()
        move_safely()
        put_all_beepers()
        move_safely()

def go_home():
    turn_around()
    move_to_wall()
    turn_around()

def turn_around():
    turn_left()
    turn_left()

def move_to_wall():
    while front_is_clear():
        move()

def move_safely():
    if front_is_clear():
        move()

def put_all_beepers():
    while beepers_in_bag():
        put_beeper()

def pick_all_beepers():
    while beepers_present():
        pick_beeper()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
