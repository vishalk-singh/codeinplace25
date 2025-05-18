from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
1. Karel to walk to the door of its house, 
2. pick up the newspaper (represented by a beeper)
3. Return to its initial position in the upper left corner of the house.
"""


def main():

    collect_newspaper()

def collect_newspaper():
    move_to_pick_beeper()
    return_to_home()

def move_to_pick_beeper():
    turn_right()
    move()
    turn_left()
    grab_beeper()

def grab_beeper():
    while front_is_clear():
        while beepers_present():
            pick_beeper()
        move()
    pick_beeper()

def return_to_home():
    move_backward()
    turn_right()
    move()
    turn_right()

def move_backward():
    turn_around()
    move_forward()

def move_forward():
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
