from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
1. Karel to walk to the door of its house, 
2. pick up the newspaper (represented by beepers). Total 3 beepers needs to be picked up.
3. Return to its initial position in the upper left corner of the house.
"""


def main():
    # Karel will walk to the door of its house to collect the newspaper.(Beepers)
    collect_newspaper()

def collect_newspaper():
    move_to_pick_beeper()
    return_to_home()
# Move to the door of Karel's house.'
def move_to_pick_beeper():
    turn_right()
    move()
    turn_left()
    grab_beeper()

# Pick up beeper that is outside of Karel's house.'
# Moving till front is clear.
# Picking up beeper if present.
# Move till front is clear to pick up beeper.
# Picking up beeper.
def grab_beeper():
    while front_is_clear():
        while beepers_present():
            pick_beeper()
        move()
    pick_beeper()

# Return to initial position.
def return_to_home():
    move_backward()
    turn_right()
    move()
    turn_right()

# Move backward while front is clear.
def move_backward():
    turn_around()
    move_forward()

# Move forward until front is clear
def move_forward():
    while front_is_clear():
        move()
# Turn left twice
def turn_around():
    turn_left()
    turn_left()

# Turn left 3 times
def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
